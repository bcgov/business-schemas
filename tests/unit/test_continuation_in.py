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
"""Test Suite to ensure continuation in schemas are valid."""

import copy

from registry_schemas import validate
from registry_schemas.example_data import CONTINUATION_IN


def test_continuation_in_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'continuationIn': CONTINUATION_IN}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_no_jurisdiction_info():
    """Assert not valid if jurisdiction info is not present."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    del continuation_in_json['foreignJurisdiction']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_jurisdiction_invalid_name():
    """Assert not valid if jurisdiction info has invalid name."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    continuation_in_json['foreignJurisdiction']['name'] = 'Test'
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_offices():
    """Assert not valid if the required offices are not present."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    del continuation_in_json['offices']['registeredOffice']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_parties():
    """Assert not valid if parties are ommited."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    del continuation_in_json['parties']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_share_classes_no_name():
    """Assert not valid if mandatory fields are not present."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    del continuation_in_json['shareStructure']['shareClasses'][0]['name']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
