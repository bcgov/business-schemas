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
"""Test Suite to ensure alteration schemas are valid."""

import copy

from registry_schemas import validate
from registry_schemas.example_data import ALTERATION


def test_alteration_schema():
    """Assert that the JSONSchema validator is working."""
    is_valid, errors = validate(ALTERATION, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_invalid_corp_name_alteration():
    """Assert not valid if name request node is not present."""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['alterCorpName']['legalName']

    is_valid, errors = validate(alteration_json, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_corp_type_alteration():
    """Assert not valid if legalType is not an accepted type."""
    alteration_json = copy.deepcopy(ALTERATION)
    alteration_json['alterCorpType']['corpType'] = 'ZZ'

    is_valid, errors = validate(alteration_json, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
