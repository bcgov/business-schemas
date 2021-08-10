# Copyright © 2020 Province of British Columbia
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
"""Test Suite to ensure transition schemas are valid."""

import copy

from registry_schemas import validate
from registry_schemas.example_data import FILING_HEADER, TRANSITION


def test_transition_schema():
    """Assert that the JSONSchema validator is working."""
    transition = {'transition': TRANSITION}
    is_valid, errors = validate(transition, 'transition')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

def test_filing_transition_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['transition'] = copy.deepcopy(TRANSITION)
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

def test_validate_no_offices():
    """Assert not valid if the required offices are not present."""
    transition_json = copy.deepcopy(TRANSITION)
    del transition_json['offices']['registeredOffice']

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_optional_contact():
    """Assert valid if the required contact info is not present."""
    transition = {'transition':  copy.deepcopy(TRANSITION)}

    del transition['transition']['contactPoint']

    is_valid, errors = validate(transition, 'transition')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_no_parties():
    """Assert not valid if parties are omitted."""
    transition_json = copy.deepcopy(TRANSITION)
    del transition_json['parties']

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_party_type():
    """Assert party types are required."""
    transition_json = copy.deepcopy(TRANSITION)

    transition_json['parties'][0]['officer']['partyType'] = 'Invalid'

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)

    print(errors)

    assert not is_valid


def test_validate_no_share_classes():
    """Assert not valid if share classes are not present."""
    transition_json ={'transition': copy.deepcopy(TRANSITION)}
    del transition_json['transition']['shareStructure']

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)

    assert not is_valid


def test_validate_valid_share_classes():
    """Assert valid if share classes are have all required fields."""
    transition_json ={'transition': copy.deepcopy(TRANSITION)}

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)

    assert is_valid


def test_validate_share_classes_no_name():
    """Assert not valid if mandatory fields are not present."""
    transition_json = copy.deepcopy(TRANSITION)
    del transition_json['shareStructure']['shareClasses'][0]['name']

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_share_classes_no_resolution_dates():
    """Assert valid if optional resolution dates is not present."""
    transition_json = copy.deepcopy(TRANSITION)
    del transition_json['shareStructure']['shareClasses'][0]['name']

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_name_translations():
    """Assert not valid if name translations contains numbers."""
    transition_json = copy.deepcopy(TRANSITION)
    transition_json['nameTranslations'] = {'new': ['Abc 123 Ltd']}

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_name_translations_long_name():
    """Assert not valid if name translations has more than 150 characters."""
    transition_json = copy.deepcopy(TRANSITION)
    transition_json['nameTranslations'] =\
        {'new': ['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA' +
                 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA']
         }

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_existing_company_provisions():
    """Assert not valid if pre-existing company provisions is not present."""
    transition_json = copy.deepcopy(TRANSITION)
    del transition_json['hasProvisions']

    is_valid, errors = validate(transition_json, 'transition')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
