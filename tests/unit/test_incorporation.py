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
"""Test Suite to ensure annual report schemas are valid."""

import copy

from registry_schemas import validate
from registry_schemas.example_data import INCORPORATION, FILING_HEADER, INCORPORATION_FILING_TEMPLATE


def test_incorporation_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'incorporationApplication': INCORPORATION}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_no_name_request():
    """Assert not valid if name request node is not present."""
    inc_json = copy.deepcopy(INCORPORATION)
    del inc_json['nameRequest']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_name_request_type():
    """Assert valid if name request legalType node is present."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = 'BC'
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_invalid_name_request_type():
    """Assert not valid if legalType is not an accepted type."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = 'ZZ'

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_offices():
    """Assert not valid if the required offices are not present."""
    inc_json = copy.deepcopy(INCORPORATION)
    del inc_json['offices']['registeredOffice']

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_contact():
    """Assert not valid if the required contact info is not present."""
    inc_json = copy.deepcopy(INCORPORATION)
    del inc_json['contactPoint']

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_parties():
    """Assert not valid if parties are ommited."""
    inc_json = copy.deepcopy(INCORPORATION)
    del inc_json['parties']

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_party_type():
    """Assert party types are required."""
    inc_json = copy.deepcopy(INCORPORATION)

    del inc_json['parties'][0]['officer']['partyType']

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)

    print(errors)

    assert not is_valid


def test_validate_person():
    """Assert conditional required fields present."""
    inc_json = copy.deepcopy(INCORPORATION)

    del inc_json['parties'][0]['officer']['orgName']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)

    print(errors)

    assert is_valid

    del inc_json['parties'][1]['officer']['orgName']

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)

    print(errors)

    assert not is_valid


def test_validate_no_share_classes():
    """Assert not valid if share classes are not present."""
    inc_json = copy.deepcopy(INCORPORATION)
    del inc_json['shareStructure']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_validate_valid_share_classes():
    """Assert valid if share classes are have all required fields."""
    inc_json = copy.deepcopy(INCORPORATION)
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)

    assert is_valid


def test_validate_share_classes_no_name():
    """Assert not valid if mandatory fields are not present."""
    inc_json = copy.deepcopy(INCORPORATION)
    del inc_json['shareStructure']['shareClasses'][0]['name']

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_agreement_type_invalid():
    """Assert not valid if agreement type is invalid."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['incorporationAgreement']['agreementType'] = 'invalid'

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_name_translations():
    """Assert not valid if name translations contains numbers."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameTranslations'] = {'new': ['Abc 123 Ltd']}

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_name_translations_long_name():
    """Assert not valid if name translations has more than 150 characters."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameTranslations'] =\
        {'new': ['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' +
                 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA']
         }

    is_valid, errors = validate(inc_json, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
