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
"""Test Suite to ensure business document schemas are valid for letter under seal."""
import copy

from registry_schemas import validate
from registry_schemas.example_data import LSEAL


def test_valid_lseal_empty_values():
    """Assert allowable empty fields."""
    lseal = copy.deepcopy(LSEAL)
    lseal['stateFilings'] = []

    is_valid, errors = validate(lseal, 'business_document')
    assert is_valid


def test_invalid_lseal_missing_fields():
    """Assert that a summary schema fails when missing required fields."""
    required_fields = [
        'offices',
        'stateFilings'
    ]
    for field in required_fields:
        invalid_schema = copy.deepcopy(LSEAL)
        del invalid_schema[field]

        is_valid, errors = validate(invalid_schema, 'business_document')
        assert not is_valid