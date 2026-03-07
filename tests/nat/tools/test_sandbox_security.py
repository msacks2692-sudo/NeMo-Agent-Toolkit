# SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import requests
import socket
import threading
import time

@pytest.mark.integration
def test_sandbox_runs_as_non_root(local_sandbox_url: str):
    """
    Verify that the code in the sandbox is NOT executed as root.
    """
    url = f"{local_sandbox_url.rstrip('/')}/execute"
    code = "import os; print(f'UID: {os.getuid()}')"
    payload = {
        "generated_code": code,
        "timeout": 5,
        "language": "python"
    }

    response = requests.post(url, json=payload, timeout=10)
    assert response.status_code == 200

    result = response.json()
    assert result["process_status"] == "completed"

    stdout = result["stdout"].strip()
    # Check that output contains UID and it is NOT 0
    assert "UID:" in stdout
    # Ensure it's not UID: 0 (allow spaces)
    uid_val = stdout.split("UID:")[1].strip()
    assert uid_val != "0", f"Security Alert: Sandbox is running as root (UID 0)! Output: {stdout}"


@pytest.mark.integration
def test_sandbox_network_isolation(local_sandbox_url: str):
    """
    Verify that the sandbox has network isolation (does not share host network).
    We check this by binding a port inside the sandbox and attempting to connect to it from the host.
    If --network=host is used, the port will be accessible on localhost.
    If isolated, it should not be accessible (unless explicitly mapped, which this random port won't be).
    """

    # 1. Find a free port on the host to use for testing
    s = socket.socket()
    s.bind(('', 0))
    test_port = s.getsockname()[1]
    s.close()

    url = f"{local_sandbox_url.rstrip('/')}/execute"

    # Code to bind the port and sleep, keeping it open
    # We use a short sleep that is long enough for our probe
    code = f"""
import socket, time
try:
    s = socket.socket()
    s.bind(('', {test_port}))
    s.listen(1)
    print("BOUND")
    time.sleep(3)
except Exception as e:
    print(f"ERROR: {{e}}")
finally:
    s.close()
"""
    payload = {
        "generated_code": code,
        "timeout": 5,
        "language": "python"
    }

    # 2. Start the sandbox execution in a separate thread because requests.post blocks
    execution_result = {}
    def run_sandbox():
        try:
            resp = requests.post(url, json=payload, timeout=10)
            if resp.status_code == 200:
                execution_result['json'] = resp.json()
            else:
                execution_result['error'] = f"Status {resp.status_code}"
        except Exception as e:
            execution_result['error'] = str(e)

    t = threading.Thread(target=run_sandbox)
    t.start()

    # 3. Wait a moment for sandbox to start execution and bind port
    time.sleep(1.5)

    # 4. Attempt to connect to the port from the host
    connected_to_sandbox = False
    try:
        # Try to connect
        sock = socket.create_connection(("localhost", test_port), timeout=1)
        # If we reach here, we connected successfully
        connected_to_sandbox = True
        sock.close()
    except (ConnectionRefusedError, socket.timeout):
        # This is expected if isolated
        pass
    except Exception as e:
        # Other errors might occur
        print(f"Unexpected error probing port: {e}")

    # 5. Wait for execution to finish
    t.join()

    # Verify sandbox actually ran successfully
    res = execution_result.get('json', {})
    stdout = res.get('stdout', '')

    # If sandbox failed to bind, the test is invalid (we can't determine isolation)
    # But if it printed BOUND, it bound the port.
    if "BOUND" not in stdout:
        # If execution failed, we can't be sure.
        # But if it failed with "Address already in use", then the port was taken?
        # Since we picked a free port on host, if host networking is ON, it should be free.
        # If isolated, it should definitely be free inside container.
        pytest.skip(f"Sandbox failed to bind port {test_port}. Output: {stdout}. Cannot verify isolation.")

    # 6. Assert isolation
    assert not connected_to_sandbox, (
        f"Security Alert: Successfully connected to sandbox port {test_port} from host! "
        "This indicates host networking is active (vulnerable)."
    )
