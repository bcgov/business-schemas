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
from registry_schemas import validate
from registry_schemas.example_data import AMALGAMATION


def test_amalgamation_schema():
    """Assert that the JSONSchema validator is working."""
    amalgamation = copy.deepcopy(AMALGAMATION)
    aml_json = {'amalgamation': amalgamation}

    is_valid, errors = validate(aml_json, 'amalgamation')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_amalgamation_schema_no_type():
    """Assert not valid if type node is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION)
    aml_json = {'amalgamation': amalgamation}
    del aml_json['amalgamation']['type']

    is_valid, errors = validate(aml_json, 'amalgamation')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_no_amalgamating_businesses():
    """Assert not valid if amalgamatingBusinesses node is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION)
    aml_json = {'amalgamation': amalgamation}
    del aml_json['amalgamation']['amalgamatingBusinesses']

    is_valid, errors = validate(aml_json, 'amalgamation')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_no_name_request():
    """Assert not valid if nameRequest node is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION)
    aml_json = {'amalgamation': amalgamation}
    del aml_json['amalgamation']['nameRequest']

    is_valid, errors = validate(aml_json, 'amalgamation')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_no_offices():
    """Assert not valid if the required offices are not present."""
    amalgamation = copy.deepcopy(AMALGAMATION)
    aml_json = {'amalgamation': amalgamation}
    del aml_json['amalgamation']['offices']['registeredOffice']

    is_valid, errors = validate(aml_json, 'amalgamation')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_no_parties():
    """Assert not valid if parties node is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION)
    aml_json = {'amalgamation': amalgamation}
    del aml_json['amalgamation']['parties']

    is_valid, errors = validate(aml_json, 'amalgamation')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_amalgamation_schema_no_contact():
    """Assert not valid if the required contact info is not present."""
    amalgamation = copy.deepcopy(AMALGAMATION)
    aml_json = {'amalgamation': amalgamation}
    del aml_json['amalgamation']['contactPoint']

    is_valid, errors = validate(aml_json, 'amalgamation')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
