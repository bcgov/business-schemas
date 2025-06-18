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
"""Test Suite to ensure legal filing schemas are valid.

This suite should have at least 1 test for every filing type allowed.
"""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import ADDRESS


def test_valid_address():
    """Assert that the schema is performing as expected."""
    is_valid, errors = validate(ADDRESS, 'address')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_address_null_region():
    """Assert that region is allowed to be null."""
    address = copy.deepcopy(ADDRESS)
    address['addressRegion'] = None

    is_valid, errors = validate(address, 'address')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('field,value', [
    ('streetAddress', 'This is a really long string, over the 50 char maximum'),
    ('streetAddressAdditional', 
     'This is a really long string, over the maximum limit (105 char), which should cause the validation to fail.')
])
def test_invalid_address(field, value):
    """Assert that an invalid address fails."""
    address = copy.deepcopy(ADDRESS)
    address[field] = value

    is_valid, errors = validate(address, 'address')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize('field', [
    'streetAddress',
    'addressCity',
    'addressCountry'
])
def test_invalid_address_missing_field(field):
    """Assert that an invalid address fails - missing required field."""
    address = copy.deepcopy(ADDRESS)
    del address[field]

    is_valid, errors = validate(address, 'address')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize('delete', [
    True,
    False
])
def test_address_optional_field(delete):
    """Assert that an address does not fails - missing optional field."""
    address = copy.deepcopy(ADDRESS)
    if delete:
        del address['deliveryInstructions']
        del address['postalCode']
        del address['addressRegion']
        del address['streetAddressAdditional']
    else:
        address['deliveryInstructions'] = None
        address['postalCode'] = None
        address['addressRegion'] = None
        address['streetAddressAdditional'] = None

    is_valid, errors = validate(address, 'address')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid
