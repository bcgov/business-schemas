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
"""Test Suite to ensure comments added onto filings and businesses are valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data import COMMENT_BUSINESS, COMMENT_FILING


def test_valid_comment_filing():
    """Assert that the schema is performing as expected for filing comments."""
    is_valid, errors = validate(COMMENT_FILING, 'comment')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_comment_business():
    """Assert that the schema is performing as expected for business comments."""
    comment = copy.deepcopy(COMMENT_BUSINESS)

    is_valid, errors = validate(comment, 'comment')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_valid_no_timestamp():
    """Assert that the schema does not require a timestamp."""
    # check with timestamp set to null
    comment = copy.deepcopy(COMMENT_FILING)
    comment['comment']['timestamp'] = None
    is_valid, errors = validate(comment, 'comment')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)
    assert is_valid

    # check with timestamp removed entirely
    del comment['comment']['timestamp']
    is_valid, errors = validate(comment, 'comment')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)
    assert is_valid


def test_invalid_filing_and_business_id():
    """Assert that schema fails with both filing and business id set."""
    comment = copy.deepcopy(COMMENT_FILING)
    comment['comment']['businessId'] = 1
    is_valid, errors = validate(comment, 'comment')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_invalid_no_filing_or_business_id():
    """Assert that one of business or filing id is required."""
    # check that setting an id to null fails
    comment = copy.deepcopy(COMMENT_FILING)
    comment['comment']['filingId'] = None
    is_valid, errors = validate(comment, 'comment')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)
    assert not is_valid

    # check that having neither id in the json at all fails
    del comment['comment']['filingId']
    is_valid, errors = validate(comment, 'comment')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)
    assert not is_valid


def test_valid_null_submitter():
    """Assert that submitter id cannot be null."""
    comment = copy.deepcopy(COMMENT_FILING)
    comment['comment']['submitterDisplayName'] = None
    is_valid, errors = validate(comment, 'comment')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)
    assert is_valid


def test_valid_no_submitter():
    """Assert that submitter id is not required."""
    comment = copy.deepcopy(COMMENT_FILING)
    del comment['comment']['submitterDisplayName']
    is_valid, errors = validate(comment, 'comment')
    if errors:
        for err in errors:
            print(err.message)
    print(errors)
    assert is_valid
