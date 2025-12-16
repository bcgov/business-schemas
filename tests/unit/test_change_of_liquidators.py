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
from registry_schemas.example_data import CHANGE_OF_LIQUIDATORS, FILING_HEADER


@pytest.mark.parametrize("test_name, sub_type, rmv_filing_sections", [
    ('appointLiquidator', 'appointLiquidator', ['changeOfLiquidatorsDate', 'offices']),
    ('ceaseLiquidator', 'ceaseLiquidator', ['changeOfLiquidatorsDate', 'offices']),
    ('changeAddressLiquidator', 'changeAddressLiquidator', ['changeOfLiquidatorsDate']),
    ('changeAddressLiquidator-no-offices', 'changeAddressLiquidator', ['changeOfLiquidatorsDate', 'offices']),
    ('changeAddressLiquidator-no-relationships', 'changeAddressLiquidator', ['changeOfLiquidatorsDate', 'relationships']),
    ('intentToLiquidate', 'intentToLiquidate', []),
    ('liquidationReport', 'liquidationReport', ['changeOfLiquidatorsDate', 'offices'])
])
def test_change_of_liquidators_schema(test_name, sub_type, rmv_filing_sections):
    """Assert that the JSONSchema validator is working for all sub types."""
    filing = {'changeOfLiquidators': copy.deepcopy(CHANGE_OF_LIQUIDATORS)}
    filing['changeOfLiquidators']['type'] = sub_type
    
    for section in rmv_filing_sections:
        del filing['changeOfLiquidators'][section]

    is_valid, errors = validate(filing, 'change_of_liquidators')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize("test_name, sub_type, filing_replacement", [
    ('appointLiquidator', 'appointLiquidator', [{ 'key': 'relationships', 'value': [] }]),
    ('ceaseLiquidator', 'ceaseLiquidator', [{ 'key': 'relationships', 'value': [] }]),
    ('changeAddressLiquidator', 'changeAddressLiquidator', [{ 'key': 'relationships', 'value': [] }, { 'key': 'offices', 'value': {} }]),
    ('intentToLiquidate-no-relationships', 'intentToLiquidate', [{ 'key': 'relationships', 'value': [] }]),
    ('intentToLiquidate-no-date', 'intentToLiquidate', [{ 'key': 'changeOfLiquidatorsDate', 'value': None }]),
    ('intentToLiquidate-no-offices', 'intentToLiquidate', [{ 'key': 'offices', 'value': {} }]),
    ('liquidationReport', 'liquidationReport', [{ 'key': 'relationships', 'value': [] }])
])
def test_change_of_liquidators_invalid_schema(test_name, sub_type, filing_replacement):
    """Assert that the JSONSchema validator is working."""
    filing = {'changeOfLiquidators': copy.deepcopy(CHANGE_OF_LIQUIDATORS)}
    filing['changeOfLiquidators']['type'] = sub_type
    
    for replacement in filing_replacement:
        section = replacement['key']
        filing['changeOfLiquidators'][section] = replacement['value']

    is_valid, errors = validate(filing, 'change_of_liquidators')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

def test_change_of_liquidators_full_filing():
    """Assert that the JSONSchema validator is working for the full filing."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'changeOfLiquidators'
    filing['filing']['changeOfLiquidators'] = copy.deepcopy(CHANGE_OF_LIQUIDATORS)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid