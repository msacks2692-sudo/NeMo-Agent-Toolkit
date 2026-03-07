# Copyright (c) 2025-2026, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from pathlib import Path

def test_start_local_sandbox_security():
    """
    Test that the start_local_sandbox.sh script does not use host networking
    and properly maps ports for security.
    """
    # tests/nat/tools/test_sandbox_script_security.py -> tests/nat/tools -> tests/nat -> tests -> root
    repo_root = Path(__file__).resolve().parents[3]
    script_path = repo_root / "src/nat/tool/code_execution/local_sandbox/start_local_sandbox.sh"

    assert script_path.exists(), f"Script not found at {script_path}"

    with open(script_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Filter out comments and empty lines
    code_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]
    content_no_comments = "\n".join(code_lines)

    # Check for insecure host networking in actual code
    assert "--network=host" not in content_no_comments, (
        "Found --network=host in start_local_sandbox.sh (excluding comments). "
        "This is insecure as it exposes the container to the host network."
    )

    # Check for secure port mapping (binding to localhost only)
    # We expect -p 127.0.0.1:6000:6000 or similar in the actual code
    assert "-p 127.0.0.1:6000:6000" in content_no_comments, (
        "Did not find secure port mapping (-p 127.0.0.1:6000:6000) in start_local_sandbox.sh (excluding comments). "
        "The sandbox should only be accessible from localhost."
    )
