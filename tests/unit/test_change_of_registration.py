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
"""Test Suite to ensure change of registration schemas are valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import CHANGE_OF_REGISTRATION, FILING_HEADER


def test_change_of_registration_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'changeOfRegistration': CHANGE_OF_REGISTRATION}

    is_valid, errors = validate(legal_filing, 'change_of_registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_filing_change_of_registration_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'changeOfRegistration'
    filing['filing']['changeOfRegistration'] = copy.deepcopy(CHANGE_OF_REGISTRATION)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('tax_id, expected', [
    ('123456789BC0001', True),
    ('123456789', True),
    ('12345678', False),
    ('1234567890', False),
    ('123456789BC', False),
    ('123456789BC00', False),
    ('1234567890BC0001', False),
    ('123456789BC00011', False)
])
def test_filing_business_tax_id_schema(tax_id, expected):
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'changeOfRegistration'
    filing['filing']['business']['taxId'] = tax_id
    filing['filing']['changeOfRegistration'] = copy.deepcopy(CHANGE_OF_REGISTRATION)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid == expected


def test_validate_valid_change_of_registration_with_any_required_element():
    """Assert valid if all of the required elements are present."""
    change_of_registration_json = copy.deepcopy(CHANGE_OF_REGISTRATION)
    del change_of_registration_json['nameRequest']
    del change_of_registration_json['offices']
    del change_of_registration_json['parties']
    del change_of_registration_json['courtOrder']
    legal_filing = {'changeOfRegistration': change_of_registration_json}

    is_valid, errors = validate(legal_filing, 'change_of_registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_invalid_change_of_registration_with_no_required_element():
    """Assert not valid if required elements are not present."""
    change_of_registration_json = copy.deepcopy(CHANGE_OF_REGISTRATION)
    del change_of_registration_json['nameRequest']
    del change_of_registration_json['offices']
    del change_of_registration_json['parties']
    del change_of_registration_json['business']
    legal_filing = {'changeOfRegistration': change_of_registration_json}

    is_valid, errors = validate(legal_filing, 'change_of_registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_change_of_registration_with_no_contact():
    """Assert not valid if contact point is not present."""
    change_of_registration_no_business_json = copy.deepcopy(CHANGE_OF_REGISTRATION)
    del change_of_registration_no_business_json['contactPoint']
    legal_filing = {'changeOfRegistration': change_of_registration_no_business_json}

    is_valid, errors = validate(legal_filing, 'change_of_registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_name_request_change_of_registration():
    """Assert not valid if name request does not contain required elements."""
    change_of_registration_json = copy.deepcopy(CHANGE_OF_REGISTRATION)
    del change_of_registration_json['nameRequest']['legalType']
    legal_filing = {'changeOfRegistration': change_of_registration_json}

    is_valid, errors = validate(legal_filing, 'change_of_registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_change_of_registration_invalid_business_office_mailing_address():
    """Assert that a changeOfRegistration is invalid if the business office mailingAddress is missing."""
    change_of_registration_json = copy.deepcopy(CHANGE_OF_REGISTRATION)
    del change_of_registration_json['offices']['businessOffice']['mailingAddress']
    legal_filing = {'changeOfRegistration': change_of_registration_json}

    is_valid, errors = validate(legal_filing, 'change_of_registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
