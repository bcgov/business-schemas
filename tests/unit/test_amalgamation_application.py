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
"""Test Suite to ensure amalgamation application schemas are valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import AMALGAMATION_APPLICATION, AMALGAMATION_APPLICATION_CP


def test_amalgamation_schema():
    """Assert that the JSONSchema validator is working."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_amalgamation_schema_no_type():
    """Assert not valid if type node is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication']['type']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_no_amalgamating_businesses():
    """Assert not valid if amalgamatingBusinesses node is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication']['amalgamatingBusinesses']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize('element,value', [
    ('legalName','removed'),
    ('legalName',''),
    ('foreignJurisdiction','removed'),
    ('identifier','removed'),
    ('identifier',''),
    ('identifier','12'),
    ('identifier','1'*41),
    ('identifier','123@')
])
def test_amalgamation_schema_not_valid_foreign(element, value):
    """Assert not valid if one of the field is not present or invalid."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}
    if value == 'removed':
        del aml_json['amalgamationApplication']['amalgamatingBusinesses'][1][element]
    else:
        aml_json['amalgamationApplication']['amalgamatingBusinesses'][1][element] = value

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_no_name_request():
    """Assert not valid if nameRequest node is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication']['nameRequest']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize('amalgamation_type,expected', [
    ('regular', False),
    ('vertical', False),
    ('horizontal', False),
])
def test_amalgamation_validate_required(amalgamation_type, expected):
    """Assert not valid if the required offices are not present."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}

    aml_json['amalgamationApplication']['type'] = amalgamation_type
    del aml_json['amalgamationApplication']['offices']
    del aml_json['amalgamationApplication']['shareStructure']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid == expected


def test_amalgamation_schema_no_parties():
    """Assert not valid if parties node is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication']['parties']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_no_contact():
    """Assert not valid if the required contact info is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication']['contactPoint']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_no_court_approval():
    """Assert not valid if courtApproval is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication']['courtApproval']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_invalid_registered_office_mailing_address():
    """Assert that a regular amalgamation application is invalid if the registered office mailingAddress is missing."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication']['offices']['registeredOffice']['mailingAddress']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_coop():
    """Assert a cooperative amalgamation with cooperative docs and no share structure is valid."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION_CP)
    aml_json = {'amalgamationApplication': amalgamation}

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('element', [
    'cooperative',
    'offices'
])
def test_amalgamation_schema_coop_missing_required(element):
    """Assert a cooperative amalgamation is invalid without its cooperative docs or offices."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION_CP)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication'][element]

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_coop_cooperative_contents():
    """Assert the cooperative section requires its file keys."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION_CP)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication']['cooperative']['rulesFileKey']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_non_coop_requires_share_structure():
    """Assert a non-coop amalgamation is still invalid without a share structure."""
    amalgamation = copy.deepcopy(AMALGAMATION_APPLICATION)
    aml_json = {'amalgamationApplication': amalgamation}
    del aml_json['amalgamationApplication']['shareStructure']

    is_valid, errors = validate(aml_json, 'amalgamation_application')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
