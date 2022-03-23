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
"""Test Suite to ensure CP special resolution schemas are valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data import BUSINESS, CHANGE_OF_NAME, SPECIAL_RESOLUTION, FILING_HEADER


NAME_REQUEST_JSON = {
    'nrNumber': 'NR 8798956',
    'legalName': 'HAULER MEDIA INC.',
    'legalType': 'BC'
}


def test_cp_special_resolution_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'specialResolution'
    filing['filing']['business'] = BUSINESS
    filing['filing']['changeOfName'] = CHANGE_OF_NAME
    filing['filing']['specialResolution'] = SPECIAL_RESOLUTION
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_cp_special_resolution_schema_with_name_request():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'specialResolution'
    filing['filing']['business'] = BUSINESS
    filing['filing']['changeOfName'] = {}
    filing['filing']['nameRequest'] = NAME_REQUEST_JSON
    filing['filing']['specialResolution'] = SPECIAL_RESOLUTION
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


