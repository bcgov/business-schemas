# Copyright © 2026 Province of British Columbia
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
"""Test suite to ensure the Change of Directors schema is valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import CHANGE_OF_DIRECTORS, CHANGE_OF_DIRECTORS_RELATIONSHIPS, FILING_HEADER


@pytest.mark.parametrize('cod_data', [CHANGE_OF_DIRECTORS, CHANGE_OF_DIRECTORS_RELATIONSHIPS])
def test_change_of_directors_schema(cod_data):
    """Assert that the Change of Directors schema is valid."""
    filing = {'changeOfDirectors': copy.deepcopy(cod_data)}

    is_valid, errors = validate(filing, 'change_of_directors')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_change_of_directors_relationships_no_actions_schema():
    """Assert that relationship items are valid without an actions array."""
    cod = copy.deepcopy(CHANGE_OF_DIRECTORS_RELATIONSHIPS)
    for relationship in cod['relationships']:
        del relationship['actions']
    filing = {'changeOfDirectors': cod}

    is_valid, errors = validate(filing, 'change_of_directors')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_change_of_directors_missing_both_schema():
    """Assert that a changeOfDirectors without directors or relationships is invalid."""
    filing = {'changeOfDirectors': {}}

    is_valid, errors = validate(filing, 'change_of_directors')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize('array_name', ['directors', 'relationships'])
def test_change_of_directors_empty_array_schema(array_name):
    """Assert that an empty directors or relationships array is invalid."""
    filing = {
        'changeOfDirectors': {
            array_name: []
        }
    }

    is_valid, errors = validate(filing, 'change_of_directors')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize('missing_prop', ['entity', 'roles', 'deliveryAddress', 'mailingAddress'])
def test_change_of_directors_relationship_missing_prop_schema(missing_prop):
    """Assert that a relationship item missing a required property is invalid."""
    cod = copy.deepcopy(CHANGE_OF_DIRECTORS_RELATIONSHIPS)
    del cod['relationships'][0][missing_prop]
    filing = {'changeOfDirectors': cod}

    is_valid, errors = validate(filing, 'change_of_directors')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize('action', ['appointed', 'ceased', 'nameChanged', 'addressChanged',
                                    'ROLES_CHANGED', 'EMAIL_CHANGED', 'CORRECTED'])
def test_change_of_directors_relationship_invalid_action_schema(action):
    """Assert that lowercase legacy actions and unhandled ActionType values are invalid."""
    cod = copy.deepcopy(CHANGE_OF_DIRECTORS_RELATIONSHIPS)
    cod['relationships'][0]['actions'] = [action]
    filing = {'changeOfDirectors': cod}

    is_valid, errors = validate(filing, 'change_of_directors')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_change_of_directors_relationship_invalid_role_type_schema():
    """Assert that a roleType outside the relationship enum is invalid."""
    cod = copy.deepcopy(CHANGE_OF_DIRECTORS_RELATIONSHIPS)
    cod['relationships'][0]['roles'][0]['roleType'] = 'Head Director'
    filing = {'changeOfDirectors': cod}

    is_valid, errors = validate(filing, 'change_of_directors')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize('cod_data', [CHANGE_OF_DIRECTORS, CHANGE_OF_DIRECTORS_RELATIONSHIPS])
def test_change_of_directors_filing(cod_data):
    """Assert that a complete filing envelope validates with either shape."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'changeOfDirectors'
    filing['filing']['changeOfDirectors'] = copy.deepcopy(cod_data)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid
