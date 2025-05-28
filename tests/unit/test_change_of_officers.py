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
"""Test suite to ensure the Change of Officers schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import CHANGE_OF_OFFICERS, FILING_HEADER

def test_change_of_officers_schema():
    """Assert that the JSONSchema validator is working."""
    filing = {'changeOfOfficers': copy.deepcopy(CHANGE_OF_OFFICERS)}

    is_valid, errors = validate(filing, 'change_of_officers')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

def test_change_of_officers_empty_relationships_schema():
    """Assert that the JSONSchema validator is working."""
    filing = {
        'changeOfOfficers': {
            'relationships': []
        }
    }

    is_valid, errors = validate(filing, 'change_of_officers')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

def test_change_of_officers_filing():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'changeOfOfficers'
    filing['filing']['header']['type'] = 'NON_LEGAL'
    filing['filing']['changeOfOfficers'] = copy.deepcopy(CHANGE_OF_OFFICERS)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid