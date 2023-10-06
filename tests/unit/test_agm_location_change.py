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
from registry_schemas import validate
from registry_schemas.example_data import AGM_LOCATION_CHANGE


def test_agm_location_change_schema():
    """Assert that the JSONSchema validator is working."""
    alc_json = {'agmLocationChange': AGM_LOCATION_CHANGE}

    is_valid, errors = validate(alc_json, 'agm_location_change')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_no_agm_year():
    """Assert that an offices node is present in the Annual Report."""
    alc_json = {'agmLocationChange': AGM_LOCATION_CHANGE}
    del alc_json['agmLocationChange']['year']

    is_valid, errors = validate(alc_json, 'agm_location_change')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid

def test_validate_no_BC():
    """Assert that an offices node is present in the Annual Report."""
    alc_json = {'agmLocationChange': AGM_LOCATION_CHANGE}
    alc_json['agmLocationChange']['newAgmLocation']['addressRegion'] = 'ON'

    updated_alc_json = alc_json

    is_valid, errors = validate(updated_alc_json, 'agm_location_change')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
