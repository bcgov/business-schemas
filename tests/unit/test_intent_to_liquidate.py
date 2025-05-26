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
"""Test suite to ensure the Intent to Liquidate schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import (
    COURT_ORDER,
    INTENT_TO_LIQUIDATE
)


def test_intent_to_liquidate_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'intentToLiquidate': copy.deepcopy(INTENT_TO_LIQUIDATE)}

    is_valid, errors = validate(legal_filing, 'intent_to_liquidate')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize(
    'element',
    [
        'liquidator',
        'liquidationRecordsOffice',
        'dateOfCommencementOfLiquidation',
    ]
)
def test_intent_to_liquidate_invalid_schema(element):
    """Assert that the JSONSchema is validating top-level required fields."""
    legal_filing = {'intentToLiquidate': copy.deepcopy(INTENT_TO_LIQUIDATE)}
    del legal_filing['intentToLiquidate'][element]

    is_valid, errors = validate(legal_filing, 'intent_to_liquidate')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_intent_to_liquidate_invalid_records_office_mailing_address():
    """Assert that the JSONSchema is validating records office mailing address requirement."""
    legal_filing = {'intentToLiquidate': copy.deepcopy(INTENT_TO_LIQUIDATE)}
    del legal_filing['intentToLiquidate']['liquidationRecordsOffice']['mailingAddress']
    is_valid, errors = validate(legal_filing, 'intent_to_liquidate')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_intent_to_liquidate_invalid_records_office_delivery_address():
    """Assert that the JSONSchema is validating records office delivery address requirement."""
    legal_filing = {'intentToLiquidate': copy.deepcopy(INTENT_TO_LIQUIDATE)}
    del legal_filing['intentToLiquidate']['liquidationRecordsOffice']['deliveryAddress']
    is_valid, errors = validate(legal_filing, 'intent_to_liquidate')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_intent_to_liquidate_invalid_liquidator_officer():
    """Assert that the JSONSchema is validating liquidator officer requirement."""
    legal_filing = {'intentToLiquidate': copy.deepcopy(INTENT_TO_LIQUIDATE)}
    del legal_filing['intentToLiquidate']['liquidator']['officer']
    is_valid, errors = validate(legal_filing, 'intent_to_liquidate')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_intent_to_liquidate_invalid_liquidator_roles():
    """Assert that the JSONSchema is validating liquidator roles requirement."""
    legal_filing = {'intentToLiquidate': copy.deepcopy(INTENT_TO_LIQUIDATE)}
    del legal_filing['intentToLiquidate']['liquidator']['roles']
    is_valid, errors = validate(legal_filing, 'intent_to_liquidate')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_intent_to_liquidate_invalid_liquidator_mailing_address():
    """Assert that the JSONSchema is validating liquidator mailing address requirement."""
    legal_filing = {'intentToLiquidate': copy.deepcopy(INTENT_TO_LIQUIDATE)}
    del legal_filing['intentToLiquidate']['liquidator']['mailingAddress']
    is_valid, errors = validate(legal_filing, 'intent_to_liquidate')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_valid_intent_to_liquidate_optional_court_order():
    """Assert that an Intent to Liquidate filing is valid with and without the optional courtOrder."""
    filing_with_co = {'intentToLiquidate': copy.deepcopy(INTENT_TO_LIQUIDATE)}
    if 'courtOrder' not in filing_with_co['intentToLiquidate'] and COURT_ORDER:
         filing_with_co['intentToLiquidate']['courtOrder'] = copy.deepcopy(COURT_ORDER)
    
    is_valid, errors = validate(filing_with_co, 'intent_to_liquidate')
    if errors:
        for err in errors: print(err.message)
    assert is_valid

    intent_data_no_co = copy.deepcopy(INTENT_TO_LIQUIDATE)
    if 'courtOrder' in intent_data_no_co:
        del intent_data_no_co['courtOrder']
    filing_without_co = {'intentToLiquidate': intent_data_no_co}

    is_valid_no_co, errors_no_co = validate(filing_without_co, 'intent_to_liquidate')
    if errors_no_co:
        for err in errors_no_co: print(err.message)
    assert is_valid_no_co


def test_invalid_intent_to_liquidate_bad_date_format():
    """Assert that the JSONSchema is validating date format for dateOfCommencementOfLiquidation."""
    legal_filing = {'intentToLiquidate': copy.deepcopy(INTENT_TO_LIQUIDATE)}
    legal_filing['intentToLiquidate']['dateOfCommencementOfLiquidation'] = '2024/01/15'  # Invalid format

    is_valid, errors = validate(legal_filing, 'intent_to_liquidate')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
