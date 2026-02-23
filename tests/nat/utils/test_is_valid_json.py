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

from nat.utils.type_utils import is_valid_json


def test_is_valid_json_standard():
    """Test standard valid JSON with double quotes."""
    assert is_valid_json('{"key": "value", "list": [1, 2, 3]}') is True
    assert is_valid_json('123') is True
    assert is_valid_json('"string"') is True
    assert is_valid_json('true') is True
    assert is_valid_json('null') is True


def test_is_valid_json_lenient():
    """Test lenient JSON parsing (single quotes)."""
    # This relies on the fallback behavior
    assert is_valid_json("{'key': 'value'}") is True
    assert is_valid_json("['a', 'b']") is True


def test_is_valid_json_invalid():
    """Test truly invalid JSON."""
    assert is_valid_json('{key: value}') is False  # Missing quotes
    assert is_valid_json('{"key": "value"') is False  # Missing closing brace
    assert is_valid_json('undefined') is False


def test_is_valid_json_single_quote_in_string():
    """Test valid JSON containing single quotes within strings."""
    # This was the bug in the previous implementation
    # The string is valid JSON: {"msg": "I'm here"}
    # The old implementation would replace ' with " making it: {"msg": "I"m here"} -> Invalid
    json_str = '{"msg": "I\'m here"}'
    assert is_valid_json(json_str) is True


def test_is_valid_json_complex():
    """Test complex nested JSON."""
    json_str = '{"a": [1, {"b": "val"}], "c": null}'
    assert is_valid_json(json_str) is True
