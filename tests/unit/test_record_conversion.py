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
"""Test Suite to ensure record conversion schemas are valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data import FIRMS_RECORD_CONVERSION, FILING_HEADER


def test_record_conversion_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'recordConversion': FIRMS_RECORD_CONVERSION}

    is_valid, errors = validate(legal_filing, 'record_conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_filing_record_conversion_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'recordConversion'
    filing['filing']['recordConversion'] = copy.deepcopy(FIRMS_RECORD_CONVERSION)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_valid_record_conversion_with_any_required_element():
    """Assert valid if all of the required elements are present."""
    record_conversion_json = copy.deepcopy(FIRMS_RECORD_CONVERSION)
    del record_conversion_json['nameRequest']
    del record_conversion_json['offices']
    del record_conversion_json['parties']
    legal_filing = {'recordConversion': record_conversion_json}

    is_valid, errors = validate(legal_filing, 'record_conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_invalid_record_conversion_with_no_required_element():
    """Assert not valid if required elements are not present."""
    record_conversion_json = copy.deepcopy(FIRMS_RECORD_CONVERSION)
    del record_conversion_json['nameRequest']
    del record_conversion_json['offices']
    del record_conversion_json['parties']
    del record_conversion_json['business']
    legal_filing = {'recordConversion': record_conversion_json}

    is_valid, errors = validate(legal_filing, 'record_conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_record_conversion_with_no_contact():
    """Assert not valid if contact point is not present."""
    record_conversion_no_business_json = copy.deepcopy(FIRMS_RECORD_CONVERSION)
    del record_conversion_no_business_json['contactPoint']
    legal_filing = {'recordConversion': record_conversion_no_business_json}

    is_valid, errors = validate(legal_filing, 'record_conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_name_request_record_conversion():
    """Assert not valid if name request does not contain required elements."""
    record_conversion_json = copy.deepcopy(FIRMS_RECORD_CONVERSION)
    del record_conversion_json['nameRequest']['legalType']
    legal_filing = {'recordConversion': record_conversion_json}

    is_valid, errors = validate(legal_filing, 'record_conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
