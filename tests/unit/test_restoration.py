# Copyright © 2021 Province of British Columbia
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
"""Test Suite to ensure restoration schemas are valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data import FILING_HEADER, RESTORATION


def test_minimal_restoration_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'restoration'
    filing['filing']['restoration'] = RESTORATION

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_restoration_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'restoration': RESTORATION}

    is_valid, errors = validate(legal_filing, 'restoration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid
