# Copyright © 2023 Province of British Columbia
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
"""Test Suite to ensure continuation out schemas are valid."""

import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import CONTINUATION_OUT


def test_continuation_out_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'continuationOut': copy.deepcopy(CONTINUATION_OUT)}

    is_valid, errors = validate(legal_filing, 'continuation_out')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('element', [
    'continuationOutDate',
    'foreignJurisdiction',
    'legalName'
])
def test_continuation_out_invalid_schema(element):
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'continuationOut': copy.deepcopy(CONTINUATION_OUT)}
    del legal_filing['continuationOut'][element]

    is_valid, errors = validate(legal_filing, 'continuation_out')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_continuation_out_invalid_jurisdiction():
    """Assert that the JSONSchema is validating jurisdiction."""
    legal_filing = {'continuationOut': copy.deepcopy(CONTINUATION_OUT)}
    del legal_filing['continuationOut']['foreignJurisdiction']['country']

    is_valid, errors = validate(legal_filing, 'continuation_out')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
