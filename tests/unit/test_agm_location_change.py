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
"""Test Suite to ensure agm location change schemas are valid."""
import copy
from registry_schemas import validate
from registry_schemas.example_data import AGM_LOCATION_CHANGE


def test_agm_location_change_schema():
    """Assert that the JSONSchema validator is working."""
    agm_location_change = copy.deepcopy(AGM_LOCATION_CHANGE)
    alc_json = {'agmLocationChange': copy.deepcopy(agm_location_change)}

    is_valid, errors = validate(alc_json, 'agm_location_change')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_no_agm_year():
    """Assert that an year node is present in the agm location change."""
    agm_location_change = copy.deepcopy(AGM_LOCATION_CHANGE)
    alc_json = {'agmLocationChange': agm_location_change}
    del alc_json['agmLocationChange']['year']

    is_valid, errors = validate(alc_json, 'agm_location_change')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_reason():
    """Assert that a reason node is present in the agm location change."""
    agm_location_change = copy.deepcopy(AGM_LOCATION_CHANGE)
    alc_json = {'agmLocationChange': agm_location_change}
    del alc_json['agmLocationChange']['reason']

    is_valid, errors = validate(alc_json, 'agm_location_change')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_agm_location():
    """Assert that an agmLocation node is present in the agm location change."""
    agm_location_change = copy.deepcopy(AGM_LOCATION_CHANGE)
    alc_json = {'agmLocationChange': agm_location_change}
    del alc_json['agmLocationChange']['agmLocation']

    is_valid, errors = validate(alc_json, 'agm_location_change')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_reason():
    """Assert not valid if reason exceeds maximum length."""
    agm_location_change = copy.deepcopy(AGM_LOCATION_CHANGE)
    alc_json = {'agmLocationChange': agm_location_change}
    alc_json['agmLocationChange']['reason'] = 'a'*2001

    is_valid, errors = validate(alc_json, 'agm_location_change')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_agm_location():
    """Assert not valid if agmLocation exceeds maximum length."""
    agm_location_change = copy.deepcopy(AGM_LOCATION_CHANGE)
    alc_json = {'agmLocationChange': agm_location_change}
    alc_json['agmLocationChange']['agmLocation'] = 'a'*101

    is_valid, errors = validate(alc_json, 'agm_location_change')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid