# Copyright © 2022 Province of British Columbia
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
"""Test Suite to ensure put back on schemas are valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import PUT_BACK_ON, FILING_HEADER


def test_minimal_put_back_on_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'putBackOn'
    filing['filing']['putBackOn'] = PUT_BACK_ON

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_put_back_on_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'putBackOn': PUT_BACK_ON}

    is_valid, errors = validate(legal_filing, 'put_back_on')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_put_back_on_court_order():
    """Assert a valid court orders."""
    legal_filing = {'putBackOn': copy.deepcopy(PUT_BACK_ON)}
    legal_filing['putBackOn']['courtOrder'] = {
        'fileNumber': '12345',
        'effectOfOrder': 'planOfArrangement'
    }

    is_valid, errors = validate(legal_filing, 'put_back_on')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('invalid_court_order', [
    *[{'orderDate': '2021-01-30T09:56:01+08:00',
       'effectOfOrder': 'invalid effect of order'}],
    *[{
        'fileNumber': invalid_file_number,
        'orderDate': '2021-01-30T09:56:01+08:00'
    } for invalid_file_number in ['1234', '123456789012345678901']],
    *[{
        'fileNumber': '12345',
        'orderDate': invalid_order_date
    } for invalid_order_date in ['2021-01-30T09:56:01', '2021-01-30']],
    *[{
        'fileNumber': '12345',
        'orderDate': '2021-01-30T09:56:01+08:00',
        'effectOfOrder': invalid_effect_of_order
    } for invalid_effect_of_order in [('a' * 501)]],  # long effectOfOrder
    *[{
        'fileNumber': '12345',
        'orderDate': '2021-01-30T09:56:01+08:00',
        'effectOfOrder': 'planOfArrangement',
        'orderDetails': invalid_order_details
    } for invalid_order_details in [('a' * 2001)]],  # long orderDetails
])
def test_validate_invalid_court_orders(invalid_court_order):
    """Assert not valid court orders."""
    legal_filing = {'putBackOn': copy.deepcopy(PUT_BACK_ON)}
    legal_filing['putBackOn']['courtOrder'] = invalid_court_order

    is_valid, errors = validate(legal_filing, 'put_back_on')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
