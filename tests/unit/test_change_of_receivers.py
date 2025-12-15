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
"""Test suite to ensure the Change of Receivers schema is valid."""
import copy
import pytest

from registry_schemas import validate
from registry_schemas.example_data import CHANGE_OF_RECEIVERS, FILING_HEADER


@pytest.mark.parametrize("sub_type", [
    ('amendReceiver'),
    ('appointReceiver'),
    ('ceaseReceiver'),
    ('changeAddressReceiver'),
])
def test_change_of_receivers_schema(sub_type):
    """Assert that the JSONSchema validator is working for all sub types."""
    filing = {'changeOfReceivers': copy.deepcopy(CHANGE_OF_RECEIVERS)}
    filing['changeOfReceivers']['type'] = sub_type

    is_valid, errors = validate(filing, 'change_of_receivers')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

def test_change_of_receivers_empty_relationships_schema():
    """Assert that the JSONSchema validator is working."""
    filing = {
        'changeOfReceivers': {
            'type': 'amendReceiver',
            'relationships': []
        }
    }

    is_valid, errors = validate(filing, 'change_of_receivers')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

# def test_change_of_receivers_filing():
#     """Assert that the JSONSchema validator is working."""
#     filing = copy.deepcopy(FILING_HEADER)
#     filing['filing']['header']['name'] = 'changeOfReceivers'
#     filing['filing']['changeOfReceivers'] = copy.deepcopy(CHANGE_OF_RECEIVERS)

#     is_valid, errors = validate(filing, 'filing')

#     if errors:
#         for err in errors:
#             print(err.message)
#     print(errors)

#     assert is_valid