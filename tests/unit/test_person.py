# Copyright © 2025 Province of British Columbia
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
"""Test suite to ensure the Person schema is valid."""
import copy

import pytest

from registry_schemas import validate

test_scenarios = [
    # valid scenarios
    (
        "valid_empty_object",
        {},
        True
    ),
    (
        "valid_all_fields",
        {
            "identifier": "123e4567-e89b-12d3-a456-426614174000",
            "givenName": "Alice",
            "familyName": "Smith",
            "additionalName": "Marie",
            "middleInitial": "M",
            "alternateName": "Ally",
            "fullName": "Alice Marie Smith",
            "email": "alice.smith@example.com"
        },
        True
    ),
    (
        "valid_some_fields",
        {
            "givenName": "Alice",
            "familyName": "Smith",
            "additionalName": "Marie"
        },
        True
    ),
    (
        "valid_only_one_field",
        {
            "familyName": "Smith"
        },
        True
    ),
    (
        "valid_empty_strings", # except email
        {
            "identifier": "",
            "givenName": "",
            "familyName": "",
            "additionalName": "",
            "middleInitial": "",
            "alternateName": "",
            "fullName": ""
        },
        True
    ),
    (
        "valid_max_length",
        {
            "identifier": "i" * 36,
            "givenName": "g" * 30,
            "familyName": "f" * 30,
            "additionalName": "a" * 30,
            "middleInitial": "m" * 30,
            "alternateName": "a" * 90,
            "fullName": "f" * 90,
            "email": "test@example.com"
        },
        True
    ),
    (
        "valid_with_extra_properties",
        {
            "givenName": "David",
            "age": 42,
            "title": "Engineer"
        },
        True
    ),
    # invalid scenarios
    (
        "invalid_max_length",
        {
            "identifier": "i" * 37,
            "givenName": "g" * 31,
            "familyName": "f" * 31,
            "additionalName": "a" * 31,
            "middleInitial": "m" * 31,
            "alternateName": "a" * 91,
            "fullName": "f" * 91,
            "email": "test@example.com"
        },
        False
    )
]

@pytest.mark.parametrize("test_name, scenario_data, valid", test_scenarios)
def test_person_schema_scenarios(test_name, scenario_data, valid):
    """Assert that the JSON is valid/invalid the provided scenarios."""
    filing = copy.deepcopy(scenario_data)

    is_valid, errors = validate(filing, 'person')

    if errors:
        for err in errors:
            print(f"{test_name}: {err.message}")
    print(errors)

    assert is_valid == valid

