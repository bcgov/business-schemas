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
"""Test suite to ensure the Relationship schema is valid."""
import copy

import pytest

from registry_schemas import validate

VALID_ENTITY = {
    'givenName': 'Phillip Tandy',
    'familyName': 'Miller',
    'alternateName': 'Phil Miller'
}

VALID_ADDRESS = {
    'streetAddress': 'address line one',
    'addressCity': 'address city',
    'addressCountry': 'Canada',
    'postalCode': 'H0H0H0',
    'addressRegion': 'BC'
}

test_scenarios = [
    # valid scenarios
    (
        "valid_relationship",
        {
            "relationships": [
                {
                    "entity": VALID_ENTITY,
                    "deliveryAddress": VALID_ADDRESS,
                    "roles": [
                        {
                            "appointmentDate": "2020-01-01",
                            "roleType": "CEO"
                        }
                    ]
                }
            ]
        },
        True
    ),
    (
        "valid_optional_fields",
        {
            "relationships": [
                {
                    "entity": VALID_ENTITY,
                    "deliveryAddress": VALID_ADDRESS,
                    "mailingAddress": VALID_ADDRESS,
                    "roles": [
                        {
                            "appointmentDate": "2020-01-01",
                            "cessationDate": "2022-01-01",
                            "roleType": "President"
                        }
                    ]
                }
            ]
        },
        True
    ),
    (
        "valid_multiple_relationships",
        {
            "relationships": [
                {
                    "entity": VALID_ENTITY,
                    "deliveryAddress": VALID_ADDRESS,
                    "roles": [
                        {
                            "appointmentDate": "2020-01-01",
                            "roleType": "CEO"
                        }
                    ]
                },
                {
                    "entity": {"familyName": "Smith"},
                    "deliveryAddress": VALID_ADDRESS,
                    "roles": [
                        {
                            "appointmentDate": "2023-05-10",
                            "roleType": "Secretary"
                        }
                    ]
                }
            ]
        },
        True
    ),
    # invalid scenarios
    (
        "invalid_empty_relationships_list",
        {
            "relationships": []
        },
        False
    ),
    (
        "invalid_missing_data",
        {},
        False
    ),
    (
        "invalid_missing_entity",
        {
            "relationships": [
                {
                    # "entity": VALID_ENTITY, # Missing
                    "deliveryAddress": VALID_ADDRESS,
                    "roles": [
                        {
                            "appointmentDate": "2020-01-01",
                            "roleType": "CEO"
                        }
                    ]
                }
            ]
        },
        False
    ),
    (
        "invalid_missing_familyName",
        {
            "relationships": [
                {
                    "entity": {"givenName": "MissingFamilyName"}, # Missing required familyName
                    "deliveryAddress": VALID_ADDRESS,
                    "roles": [
                        {
                            "appointmentDate": "2020-01-01",
                            "roleType": "CEO"
                        }
                    ]
                }
            ]
        },
        False
    ),
    (
        "invalid_missing_deliveryAddress",
        {
            "relationships": [
                {
                    "entity": VALID_ENTITY,
                    # "deliveryAddress": VALID_ADDRESS, # Missing
                    "roles": [
                        {
                            "appointmentDate": "2020-01-01",
                            "roleType": "CEO"
                        }
                    ]
                }
            ]
        },
        False
    ),
    (
        "invalid_missing_appointmentDate",
        {
            "relationships": [
                {
                    "entity": VALID_ENTITY,
                    "deliveryAddress": VALID_ADDRESS,
                    "roles": [
                        {
                            # "appointmentDate": "2020-01-01", # Missing
                            "roleType": "CEO"
                        }
                    ]
                }
            ]
        },
        False
    ),
    (
        "invalid_appointmentDate_format",
        {
            "relationships": [
                {
                    "entity": VALID_ENTITY,
                    "deliveryAddress": VALID_ADDRESS,
                    "roles": [
                        {
                            "appointmentDate": "2020/01/01", # Invalid format
                            "roleType": "CEO"
                        }
                    ]
                }
            ]
        },
        False
    ),
    (
        "invalid_cessationDate_format",
        {
            "relationships": [
                {
                    "entity": VALID_ENTITY,
                    "deliveryAddress": VALID_ADDRESS,
                    "roles": [
                        {
                            "appointmentDate": "2020-01-01",
                            "cessationDate": "2020/01/01", # Invalid format
                            "roleType": "CEO"
                        }
                    ]
                }
            ]
        },
        False
    ),
    (
        "invalid_missing_roles",
        {
            "relationships": [
                {
                    "entity": VALID_ENTITY,
                    "deliveryAddress": VALID_ADDRESS,
                    # "roles": "[]" # Missing
                }
            ]
        },
        False
    ),
    (
        "invalid_roles_empty",
        {
            "relationships": [
                {
                    "entity": VALID_ENTITY,
                    "deliveryAddress": VALID_ADDRESS,
                    "roles": []
                }
            ]
        },
        False
    ),
]

@pytest.mark.parametrize("test_name, scenario_data, valid", test_scenarios)
def test_relationship_schema_scenarios(test_name, scenario_data, valid):
    """Assert that the JSON is valid/invalid the provided scenarios."""
    filing = copy.deepcopy(scenario_data)

    is_valid, errors = validate(filing, 'relationship')

    if errors:
        for err in errors:
            print(f"{test_name}: {err.message}")
    print(errors)

    assert is_valid == valid

test_roles = [
    # valid roles   
    (
        "valid_role_CEO",
        "CEO",
        True
    ),
    (
        "valid_role_CFO",
        "CFO",
        True
    ),
    (
        "valid_role_President",
        "President",
        True
    ),
    (
        "valid_role_Vice_President",
        "Vice President",
        True
    ),
    (
        "valid_role_Chair",
        "Chair",
        True
    ),
    (
        "valid_role_Treasurer",
        "Treasurer",
        True
    ),
    (
        "valid_role_Secretary",
        "Secretary",
        True
    ),
    (
        "valid_role_Assistant_Secretary",
        "Assistant Secretary",
        True
    ),
    (
        "valid_role_Other",
        "Other",
        True
    ),
    # invalid roles
    (
        "invalid_role_random",
        "Random",
        False
    ),
    (
        "invalid_role_typo",
        "CDO",
        False
    ),
    (
        "invalid_role_typo2",
        "Secretaty",
        False
    )
]

@pytest.mark.parametrize("test_name, role, valid", test_roles)
def test_relationship_schema_roles(test_name, role, valid):
    """Assert that the JSON is valid/invalid with the provided roles."""
    filing = {
        "relationships": [
            {
                "entity": VALID_ENTITY,
                "deliveryAddress": VALID_ADDRESS,
                "roles": [
                    {
                        "appointmentDate": "2020-01-01",
                        "roleType": role
                    }
                ]
            }
        ]
    }

    is_valid, errors = validate(filing, 'relationship')

    if errors:
        for err in errors:
            print(f"{test_name}: {err.message}")
    print(errors)

    assert is_valid == valid
