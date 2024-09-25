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
from registry_schemas.example_data import FILING_HEADER, NOTICE_OF_WITHDRAWAL


def test_minimal_notice_of_withdrawal():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'noticeOfWithdrawal'
    filing['filing']['noticeOfWithdrawal'] = NOTICE_OF_WITHDRAWAL

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_admin_freeze_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'noticeOfWithdrawal': NOTICE_OF_WITHDRAWAL}

    is_valid, errors = validate(legal_filing, 'notice_of_withdrawal')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

