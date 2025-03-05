# Copyright © 2025 Province of British Columbia
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
"""Test Suite to ensure cease receiver schemas are valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data import CEASE_RECEIVER


def test_cease_receiver_schema():
    """Assert that the JSONSchema validator is working."""
    cease_receiver_json = {'ceaseReceiver': copy.deepcopy(CEASE_RECEIVER)}

    is_valid, errors = validate(cease_receiver_json, 'cease_receiver')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_cease_receiver_schema_no_person():
    """Assert not valid if officer node is not present."""
    cease_receiver_json = {'ceaseReceiver': copy.deepcopy(CEASE_RECEIVER)}
    del cease_receiver_json['ceaseReceiver']['parties'][0]['officer']

    is_valid, errors = validate(cease_receiver_json, 'cease_receiver')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
