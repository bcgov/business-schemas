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
"""Test Suite to ensure correction schemas are valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data import (
    CORRECTION_CHANGE_OF_REGISTRATION,
    CORRECTION_COA,
    CORRECTION_CP_SPECIAL_RESOLUTION,
    CORRECTION_INCORPORATION,
    CORRECTION_REGISTRATION,
)
from registry_schemas.example_data.schema_data import FILING_HEADER


def test_correction_schema_valid_ia():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(CORRECTION_INCORPORATION)
    correction_json = {'correction': filing.get('filing').get('correction')}
    is_valid, errors = validate(correction_json, 'correction')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_correction_schema_invalid_ia():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(CORRECTION_INCORPORATION)
    correction_json = {'correction': filing.get('filing').get('correction')}
    del correction_json['correction']['parties']
    is_valid, errors = validate(correction_json, 'correction')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_correction_schema_valid_change_of_registration():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(CORRECTION_CHANGE_OF_REGISTRATION)
    correction_json = {'correction': filing.get('filing').get('correction')}
    is_valid, errors = validate(correction_json, 'correction')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_correction_schema_invalid_change_of_registration():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(CORRECTION_CHANGE_OF_REGISTRATION)
    correction_json = {'correction': filing.get('filing').get('correction')}
    del correction_json['correction']['parties']
    is_valid, errors = validate(correction_json, 'correction')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_correction_schema_registration():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(CORRECTION_REGISTRATION)
    correction_json = {'correction': filing.get('filing').get('correction')}
    is_valid, errors = validate(correction_json, 'correction')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_correction_schema_invalid_registration():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(CORRECTION_REGISTRATION)
    correction_json = {'correction': filing.get('filing').get('correction')}
    del correction_json['correction']['parties']
    is_valid, errors = validate(correction_json, 'correction')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_correction_schema_coa():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(CORRECTION_COA)
    correction_json = {'correction': filing.get('filing').get('correction')}
    is_valid, errors = validate(correction_json, 'correction')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_correction_schema_cp_special_resolution():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['correction'] = copy.deepcopy(CORRECTION_CP_SPECIAL_RESOLUTION)
    correction_json = {'correction': filing.get('filing').get('correction')}

    is_valid, errors = validate(correction_json, 'correction')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_correction_schema_invalid_cp_special_resolution():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['correction'] = copy.deepcopy(CORRECTION_CP_SPECIAL_RESOLUTION)
    correction_json = {'correction': filing.get('filing').get('correction')}
    del correction_json['correction']['business']
    is_valid, errors = validate(correction_json, 'correction')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
