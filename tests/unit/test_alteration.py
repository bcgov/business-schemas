# Copyright © 2019 Province of British Columbia
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
"""Test Suite to ensure alteration schemas are valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import ALTERATION, FILING_HEADER


def test_alteration_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'alteration': ALTERATION}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_filing_alteration_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['alteration'] = copy.deepcopy(ALTERATION)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_valid_alteration_with_any_required_element():
    """Assert valid if all of the required alterations is present."""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['nameRequest']
    del alteration_json['provisionsRemoved']
    del alteration_json['nameTranslations']
    del alteration_json['shareStructure']
    del alteration_json['courtOrder']
    legal_filing = {'alteration': alteration_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_invalid_alteration_with_unknown_legal_type():
    """Assert invalid if legal type is not defined in business json."""
    alteration_json = copy.deepcopy(ALTERATION)
    alteration_json['business']['legalType'] = 'benefitCompany'
    legal_filing = {'alteration': alteration_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_alteration_with_no_business():
    """Assert not valid if business is not present."""
    alteration_no_business_json = copy.deepcopy(ALTERATION)
    del alteration_no_business_json['business']
    legal_filing = {'alteration': alteration_no_business_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_alteration_with_no_contact():
    """Assert not valid if contact point is not present."""
    alteration_no_contact_json = copy.deepcopy(ALTERATION)
    del alteration_no_contact_json['contactPoint']
    legal_filing = {'alteration': alteration_no_contact_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)


def test_validate_invalid_corp_name_alteration():
    """Assert not valid if corp name alteration does not contain required elements."""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['nameRequest']['legalType']
    legal_filing = {'alteration': alteration_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_name_translation_alteration():
    """Assert not valid if name translation alteration does not contain mandatory elements."""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['nameTranslations'][0]['name']
    legal_filing = {'alteration': alteration_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_valid_share_structure_alteration():
    """Assert valid if share structure alteration does not contain share classes."""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['shareStructure']
    legal_filing = {'alteration': alteration_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)
    assert is_valid

    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['shareStructure']['shareClasses']
    legal_filing = {'alteration': alteration_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)
    assert is_valid


@pytest.mark.parametrize('invalid_court_order', [
    *[{'orderDate': '2021-01-30T09:56:01+08:00',
       'effectOfOrder': 'valid effect of order'}],
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
    alteration_json = copy.deepcopy(ALTERATION)
    alteration_json['courtOrder'] = invalid_court_order
    legal_filing = {'alteration': alteration_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

def test_validate_valid_coop_alteration():
    """ Assert valid coop alteration"""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['nameRequest']
    del alteration_json['nameTranslations']
    del alteration_json['shareStructure']
    del alteration_json['courtOrder']

    alteration_json['association_type'] = 'CP'

    legal_filing = {'alteration': alteration_json}

    is_valid, errors = validate(legal_filing, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)
    assert is_valid
