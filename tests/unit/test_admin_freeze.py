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
"""Test Suite to ensure admin freeze on schemas are valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import ADMIN_FREEZE, FILING_HEADER


def test_minimal_admin_freeze_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'adminFreeze'
    filing['filing']['adminFreeze'] = ADMIN_FREEZE

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_admin_freeze_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'adminFreeze': ADMIN_FREEZE}

    is_valid, errors = validate(legal_filing, 'admin_freeze')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_admin_freeze_filing_group_validates_admin_freeze_ref():
    """Assert that a singular filing validates its admin freeze payload."""
    filing = copy.deepcopy(FILING_HEADER['filing'])
    filing['header']['name'] = 'adminFreeze'
    filing['adminFreeze'] = ADMIN_FREEZE

    is_valid, errors = validate(filing, 'filing_group_singular')

    assert is_valid, list(errors or [])


def test_admin_freeze_filing_group_rejects_invalid_admin_freeze_payload():
    """Assert that the referenced admin freeze schema is enforced."""
    filing = copy.deepcopy(FILING_HEADER['filing'])
    filing['header']['name'] = 'adminFreeze'
    filing['adminFreeze'] = {}

    is_valid, errors = validate(filing, 'filing_group_singular')

    assert not is_valid
    errors = list(errors)
    assert len(errors) == 1
    assert errors[0].validator == 'required'
    assert errors[0].message == "'freeze' is a required property"


def test_admin_freeze_filing_preserves_header_and_schema_errors():
    """Assert that selected schema errors do not hide header validation errors."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'adminFreeze'
    filing['filing']['header'].pop('date')
    filing['filing']['adminFreeze'] = {}

    is_valid, errors = validate(filing, 'filing')

    assert not is_valid
    messages = {error.message for error in errors}
    assert "'date' is a required property" in messages
    assert "'freeze' is a required property" in messages

