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
"""Test Suite to ensure continuation in schemas are valid."""

import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import CONTINUATION_IN, CONTINUATION_IN_RELATIONSHIPS, FILING_HEADER


@pytest.mark.parametrize('continuation_in_data', [CONTINUATION_IN, CONTINUATION_IN_RELATIONSHIPS])
def test_continuation_in_schema(continuation_in_data):
    """Assert that the JSONSchema validator is working for both party shapes."""
    legal_filing = {'continuationIn': copy.deepcopy(continuation_in_data)}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_no_jurisdiction_info():
    """Assert not valid if jurisdiction info is not present."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    del continuation_in_json['foreignJurisdiction']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_continuation_in_invalid_jurisdiction():
    """Assert that the JSONSchema is validating jurisdiction."""
    legal_filing = {'continuationIn': copy.deepcopy(CONTINUATION_IN)}
    del legal_filing['continuationIn']['foreignJurisdiction']['country']

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_continuation_in_invalid_authorization():
    """Assert that the JSONSchema is validating authorization."""
    legal_filing = {'continuationIn': copy.deepcopy(CONTINUATION_IN)}
    legal_filing['continuationIn']['authorization']['files'] = None 
    legal_filing['continuationIn']['authorization']['date'] = None 

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_continuation_in_invalid_authorization_files():
    """Assert that the JSONSchema is validating authorization files."""
    legal_filing = {'continuationIn': copy.deepcopy(CONTINUATION_IN)}
    legal_filing['continuationIn']['authorization']['files'] = [] 

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_offices():
    """Assert not valid if the required offices are not present."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    del continuation_in_json['offices']['registeredOffice']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_parties():
    """Assert not valid if parties are ommited."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    continuation_in_json['isApproved'] = True
    del continuation_in_json['parties']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_share_classes_no_name():
    """Assert not valid if mandatory fields are not present."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    del continuation_in_json['shareStructure']['shareClasses'][0]['name']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_continuation_in_submit_authorization():
    """Assert valid if continuation in can be submitted for approval without these props."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    del continuation_in_json['isApproved']  # removing isApproved will trigger 'then' (equivalent to False)
    del continuation_in_json['offices']
    del continuation_in_json['parties']
    del continuation_in_json['shareStructure']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_continuation_in_submit_after_approval():
    """Assert not valid if these are ommited."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    continuation_in_json['isApproved'] = True
    del continuation_in_json['offices']
    del continuation_in_json['parties']
    del continuation_in_json['shareStructure']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_continuation_in_invalid_registered_office_mailing_address():
    """Assert that a continuationIn is invalid if the registered office mailingAddress is missing."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN)
    continuation_in_json['isApproved'] = True
    del continuation_in_json['offices']['registeredOffice']['mailingAddress']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_relationships_not_approved_without_party_shape():
    """Assert valid when isApproved is false and neither parties nor relationships are present."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN_RELATIONSHIPS)
    continuation_in_json['isApproved'] = False
    del continuation_in_json['relationships']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_approved_missing_both_party_shapes():
    """Assert not valid when isApproved is true and neither parties nor relationships are present."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN_RELATIONSHIPS)
    del continuation_in_json['relationships']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_empty_relationships():
    """Assert not valid if relationships is an empty array."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN_RELATIONSHIPS)
    continuation_in_json['relationships'] = []
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


@pytest.mark.parametrize('missing_prop', ['entity', 'roles', 'deliveryAddress', 'mailingAddress'])
def test_validate_relationship_missing_prop(missing_prop):
    """Assert not valid if a relationship item is missing a required property."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN_RELATIONSHIPS)
    del continuation_in_json['relationships'][0][missing_prop]
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_relationship_invalid_role_type():
    """Assert not valid if a relationship roleType is outside the relationship enum."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN_RELATIONSHIPS)
    continuation_in_json['relationships'][0]['roles'][0]['roleType'] = 'Head Director'
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_relationship_role_without_appointment_date():
    """Assert valid at the schema level without appointmentDate (legal-api enforces it for continuationIn)."""
    continuation_in_json = copy.deepcopy(CONTINUATION_IN_RELATIONSHIPS)
    del continuation_in_json['relationships'][1]['roles'][0]['appointmentDate']
    legal_filing = {'continuationIn': continuation_in_json}

    is_valid, errors = validate(legal_filing, 'continuation_in')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('continuation_in_data', [CONTINUATION_IN, CONTINUATION_IN_RELATIONSHIPS])
def test_continuation_in_filing(continuation_in_data):
    """Assert that a complete filing envelope validates with either party shape."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'continuationIn'
    filing['filing']['continuationIn'] = copy.deepcopy(continuation_in_data)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid
