# SPDX-FileCopyrightText: Copyright (c) 2025-2026, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import pytest
import base64
import os
from unittest.mock import MagicMock, patch
from nat.registry_handlers.rest.rest_handler import RestRegistryHandler
from nat.registry_handlers.schemas.pull import PullRequestPackages
from nat.registry_handlers.schemas.status import StatusEnum

@pytest.mark.asyncio
async def test_pull_path_traversal():
    """
    Test that RestRegistryHandler.pull detects malicious filename containing path traversal characters.
    It should return a response with ERROR status.
    """
    # Setup
    handler = RestRegistryHandler(endpoint="http://example.com", token="fake")

    # Create a malicious package response
    # We use a filename that attempts to traverse up
    malicious_filename = "../evil.whl"
    whl_content = b"malicious content"
    whl_base64 = base64.b64encode(whl_content).decode('utf-8')

    pull_response = {
        "status": {"status": "success", "message": "", "action": "pull"},
        "packages": [
            {
                "whl": whl_base64,
                "whl_name": malicious_filename,
                "version": "1.0",
                "name": "evil-pkg"
            }
        ]
    }

    # Mock httpx.AsyncClient.post
    with patch("httpx.AsyncClient.post") as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = pull_response
        mock_post.return_value = mock_response

        # Mock subprocess.run
        with patch("subprocess.run") as mock_run:
            mock_run.return_value.returncode = 0

            # Mock open to prevent file creation (though validation should prevent it reaching here)
            with patch("builtins.open", new_callable=MagicMock) as mock_file:

                packages = PullRequestPackages(packages=[])

                response_received = None
                async with handler.pull(packages) as response:
                    response_received = response

                # Check that we got an ERROR response
                assert response_received.status.status == StatusEnum.ERROR
                assert "Invalid filename" in response_received.status.message
                assert "../evil.whl" in response_received.status.message

                # Verify open was NOT called (extra safety check)
                mock_file.assert_not_called()
