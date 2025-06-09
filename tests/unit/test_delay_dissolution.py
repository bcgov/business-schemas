# Copyright © 2021 Province of British Columbia
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
"""Test Suite to ensure dissolution schemas are valid."""
import copy

import pytest
from registry_schemas import validate

# Example minimal valid delay dissolution data
DELAY_DISSOLUTION = {
    'dissolution': {
        'dissolutionDate': '2025-12-31',
        'dissolutionType': 'voluntary'
    }
}

def test_minimal_delay_dissolution_schema():
    """Assert the minimal delay dissolution schema is valid."""
    is_valid, errors = validate(copy.deepcopy(DELAY_DISSOLUTION), 'delayDissolution')

    if errors:
        for err in errors:
            print(err.message)
    assert is_valid

def test_delay_dissolution_with_all_fields():
    """Assert delay dissolution with all fields is valid."""
    full_data = copy.deepcopy(DELAY_DISSOLUTION)
    full_data['dissolution']

    is_valid, errors = validate(full_data, 'delayDissolution')

    if errors:
        for err in errors:
            print(err.message)
    assert is_valid

@pytest.mark.parametrize('invalid_delay', [
    # Invalid date format
    {'dissolutionDate': '2025/12/31', 'dissolutionType': 'voluntary'},
    # Invalid type
    {'dissolutionDate': '2025-12-31', 'dissolutionType': 'fakeType'},
    # Missing required fields
    {},
])
def test_invalid_delay_dissolution_date_format(invalid_delay):
    """Assert invalid delay dissolution schemas are caught."""
    is_valid, errors = validate({'delayDissolution': {'dissolution': invalid_delay}}, 'delayDissolution')

    if errors:
        for err in errors:
            print(err.message)
    assert not is_valid

@pytest.mark.parametrize('over_max_delays', [
    {
        'dissolution': {
            'numberOfDelays': 3,
            'dissolutionDate': '2025-12-31',
            'dissolutionType': 'voluntary'
        }
    }
])
def test_invalid_delay_dissolution_delays(over_max_delays):
    """Assert that going over the maximum number of delays is caught"""
    is_valid, errors = validate(over_max_delays, 'delayDissolution')

    if errors:
        for err in errors:
            print(err.message)
    assert not is_valid
