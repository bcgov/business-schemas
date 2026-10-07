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
"""Test suite to ensure the Review Imported Data schema is valid."""

import copy

from registry_schemas import validate
from registry_schemas.example_data import FILING_HEADER, REVIEW_IMPORTED_DATA


def test_review_imported_data_schema():
    """Assert that the Review Imported Data schema is valid."""
    filing = {'reviewImportedData': copy.deepcopy(REVIEW_IMPORTED_DATA)}
    is_valid, errors = validate(filing, 'review_imported_data')

    assert is_valid


def test_review_imported_data_offices_only():
    """Assert that the Review Imported Data schema is valid with offices only."""
    filing = {
        'reviewImportedData': {
            'offices': copy.deepcopy(REVIEW_IMPORTED_DATA['offices'])
        }
    }

    is_valid, errors = validate(filing, 'review_imported_data')

    assert is_valid


def test_review_imported_data_relationships_only():
    """Assert that the Review Imported Data schema is valid with relationships only."""
    filing = {
        'reviewImportedData': {
            'relationships': copy.deepcopy(REVIEW_IMPORTED_DATA['relationships'])
        }
    }

    is_valid, errors = validate(filing, 'review_imported_data')

    assert is_valid


def test_review_imported_data_requires_offices_or_relationships():
    """Assert that the Review Imported Data schema requires offices or relationships."""
    filing = {'reviewImportedData': {}}

    is_valid, errors = validate(filing, 'review_imported_data')

    assert not is_valid


def test_review_imported_data_empty_relationships():
    """Assert that the Review Imported Data schema rejects empty relationships."""
    filing = {
        'reviewImportedData': {
            'relationships': []
        }
    }

    is_valid, errors = validate(filing, 'review_imported_data')

    assert not is_valid


def test_review_imported_data_empty_offices():
    """Assert that the Review Imported Data schema rejects empty offices."""
    filing = {
        'reviewImportedData': {
            'offices': {}
        }
    }

    is_valid, errors = validate(filing, 'review_imported_data')

    assert not is_valid


def test_review_imported_data_requires_director_identifier():
    """Assert that the Review Imported Data schema requires a director identifier."""
    filing = {
        'reviewImportedData': {
            'relationships': copy.deepcopy(
                REVIEW_IMPORTED_DATA['relationships']
            )
        }
    }
    del filing['reviewImportedData']['relationships'][0]['entity']['identifier']

    is_valid, errors = validate(filing, 'review_imported_data')

    assert not is_valid


def test_review_imported_data_allows_empty_director_name():
    """Assert that the Review Imported Data schema allows an empty director name."""
    filing = {
        'reviewImportedData': {
            'relationships': copy.deepcopy(
                REVIEW_IMPORTED_DATA['relationships']
            )
        }
    }
    filing['reviewImportedData']['relationships'][0]['entity']['givenName'] = ''
    filing['reviewImportedData']['relationships'][0]['entity']['familyName'] = ''

    is_valid, errors = validate(filing, 'review_imported_data')

    assert is_valid


def test_review_imported_data_requires_director_role():
    """Assert that Review Imported Data relationships require a Director role."""
    filing = {
        'reviewImportedData': {
            'relationships': copy.deepcopy(
                REVIEW_IMPORTED_DATA['relationships']
            )
        }
    }
    filing['reviewImportedData']['relationships'][0]['roles'][0]['roleType'] = 'Officer'

    is_valid, errors = validate(filing, 'review_imported_data')

    assert not is_valid


def test_review_imported_data_full_filing():
    """Assert that the JSONSchema validator is working for the full filing."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'reviewImportedData'
    filing['filing']['reviewImportedData'] = copy.deepcopy(REVIEW_IMPORTED_DATA)

    is_valid, errors = validate(filing, 'filing')

    assert is_valid
