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
"""Test Suite to ensure registeration schemas are valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import FILING_HEADER, REGISTRATION


def test_gp_registration_schema():
    """Assert that the general partnership registration is valid."""
    legal_filing = {'registration': REGISTRATION}

    is_valid, errors = validate(legal_filing, 'registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_sp_registration_schema():
    """Assert that the sole proprietor registration is valid."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'registration'
    del filing['filing']['business']
    registration_json = copy.deepcopy(REGISTRATION)
    registration_json['nameRequest']['legalType'] = 'SP'
    registration_json['businessType'] = 'SP'

    registration_json['parties'][0]['roles'] = [
        {
            'roleType': 'Completing Party',
            'appointmentDate': '2022-01-01'

        },
        {
            'roleType': 'Proprietor',
            'appointmentDate': '2022-01-01'

        }
    ]
    del registration_json['parties'][1]

    filing['filing']['registration'] = registration_json
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_dba_registration_schema():
    """Assert that the sole proprietor (DBA) registration is valid."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'registration'
    del filing['filing']['business']
    registration_json = copy.deepcopy(REGISTRATION)
    registration_json['nameRequest']['legalType'] = 'SP'
    registration_json['businessType'] = 'DBA'

    registration_json['parties'][0]['roles'] = [
        {
            'roleType': 'Completing Party',
            'appointmentDate': '2022-01-01'

        }
    ]

    registration_json['parties'][1] = {
        'officer': {
            'id': 2,
            'organizationName': 'Xyz Inc.',
            'identifier': 'BC1234567',
            'email': 'peter@email.com',
            'partyType': 'organization'
        },
        'mailingAddress': {
            'streetAddress': 'mailing_address - address line one',
            'streetAddressAdditional': '',
            'addressCity': 'mailing_address city',
            'addressCountry': 'CA',
            'postalCode': 'H0H0H0',
            'addressRegion': 'BC'
        },
        'roles': [
            {
                'roleType': 'Proprietor',
                'appointmentDate': '2022-01-01'
            }
        ]
    }

    filing['filing']['registration'] = registration_json
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_filing_registration_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'registration'
    del filing['filing']['business']
    filing['filing']['registration'] = copy.deepcopy(REGISTRATION)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_valid_registration_with_any_required_element():
    """Assert valid if all of the required registrations is present."""
    registration_json = copy.deepcopy(REGISTRATION)
    del registration_json['courtOrder']
    legal_filing = {'registration': registration_json}

    is_valid, errors = validate(legal_filing, 'registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('element', [
    'contactPoint',
    'parties',
    'offices',
    'nameRequest',
    'startDate'
])
def test_validate_invalid_registration_with_required(element):
    """Assert not valid if contact point is not present."""
    registration_json = copy.deepcopy(REGISTRATION)
    del registration_json[element]
    legal_filing = {'registration': registration_json}

    is_valid, errors = validate(legal_filing, 'registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_corp_name_registration():
    """Assert not valid if corp name registration does not contain required elements."""
    registration_json = copy.deepcopy(REGISTRATION)
    del registration_json['nameRequest']['legalType']
    legal_filing = {'registration': registration_json}

    is_valid, errors = validate(legal_filing, 'registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


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
    registration_json = copy.deepcopy(REGISTRATION)
    registration_json['courtOrder'] = invalid_court_order
    legal_filing = {'registration': registration_json}

    is_valid, errors = validate(legal_filing, 'registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

@pytest.mark.parametrize(
        'first_name, last_name, expected', [
            ('Joe', 'Swanson', True),
            ('', 'Swanson', True),
            ('Joe', '', False),
            ('', '', False),
            ('', 'asdfghasdfghasdfghasdfghasdfghasdfgh', False)
        ]
)
def test_validate_single_name(first_name, last_name, expected):
    registration_json = copy.deepcopy(REGISTRATION)
    registration_json['parties'][0]['officer']['firstName'] = first_name
    registration_json['parties'][0]['officer']['lastName'] = last_name
    del registration_json['parties'][0]['roles'][1]
    legal_filing = {'registration': registration_json}

    is_valid, errors = validate(legal_filing, 'registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid == expected

def test_validate_invalid_single_name_for_non_completing_party():
    registration_json = copy.deepcopy(REGISTRATION)
    registration_json['parties'][1]['officer']['firstName'] = ''
    legal_filing = {'registration': registration_json}

    is_valid, errors = validate(legal_filing, 'registration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid