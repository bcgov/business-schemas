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
"""Test Suite to ensure incorporation application schemas are valid."""

import copy
import pytest

from registry_schemas import validate
from registry_schemas.example_data import COURT_ORDER, INCORPORATION


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_incorporation_schema(test_name, legal_type):
    """Assert that the JSONSchema validator is working."""
    incorporation_application = copy.deepcopy(INCORPORATION)
    incorporation_application['nameRequest']['legalType'] = legal_type
    if legal_type != 'BEN':
        incorporation_application['courtOrder'] = COURT_ORDER

    legal_filing = {'incorporationApplication': incorporation_application}

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


def test_validate_invalid_name_request_type():
    """Assert not valid if legalType is not an accepted type."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = 'ZZ'
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_no_offices(test_name, legal_type):
    """Assert not valid if the required offices are not present."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    del inc_json['offices']['registeredOffice']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_no_contact(test_name, legal_type):
    """Assert not valid if the required contact info is not present."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    del inc_json['contactPoint']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_no_parties(test_name, legal_type):
    """Assert not valid if parties are ommited."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    del inc_json['parties']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_party_type(test_name, legal_type):
    """Assert party types are required."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    del inc_json['parties'][0]['officer']['partyType']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)

    print(errors)

    assert not is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_person(test_name, legal_type):
    """Assert conditional required fields present."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    del inc_json['parties'][0]['officer']['organizationName']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)

    print(errors)

    assert is_valid

    del inc_json['parties'][1]['officer']['organizationName']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)

    print(errors)

    assert not is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_valid_share_classes(test_name, legal_type):
    """Assert valid if share classes are have all required fields."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)

    assert is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_share_classes_no_name(test_name, legal_type):
    """Assert not valid if mandatory fields are not present."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    del inc_json['shareStructure']['shareClasses'][0]['name']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_agreement_type_invalid(test_name, legal_type):
    """Assert not valid if agreement type is invalid."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    inc_json['incorporationAgreement']['agreementType'] = 'invalid'
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_invalid_name_translations(test_name, legal_type):
    """Assert not valid if name translations contains numbers."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    inc_json['nameTranslations'] = {'new': ['Abc 123 Ltd']}
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize(
    'test_name, legal_type', [
        ('Benefit Company IA', 'BEN'),
        ('BC Limited Company', 'BC'),
        ('BC Community Contribution Company', 'CC'),
        ('BC Unlimited Liability Company', 'ULC'),
    ])
def test_validate_invalid_name_translations_long_name(test_name, legal_type):
    """Assert not valid if name translations has more than 150 characters."""
    inc_json = copy.deepcopy(INCORPORATION)
    inc_json['nameRequest']['legalType'] = legal_type
    inc_json['nameTranslations'] =\
        {'new': ['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' +
                 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA']
         }
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_cooperative_invalid():
    """Assert not valid if cooperative is invalid."""
    coop_ia = copy.deepcopy(INCORPORATION)
    del coop_ia['offices']['recordsOffice']
    del coop_ia['parties'][1]
    del coop_ia['shareStructure']
    del coop_ia['incorporationAgreement']
    coop_ia['cooperative'] = {}

    legal_filing = {'incorporationApplication': coop_ia}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_incorporation_invalid_registered_office_mailing_address():
    """Assert that an incorporation application is invalid if the registered office mailingAddress is missing."""
    inc_json = copy.deepcopy(INCORPORATION)
    del inc_json['offices']['registeredOffice']['mailingAddress']
    legal_filing = {'incorporationApplication': inc_json}

    is_valid, errors = validate(legal_filing, 'incorporation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
