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
"""Test Suite to ensure firms conversion schemas are valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data import FIRMS_CONVERSION, FILING_HEADER


def test_firms_conversion_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'conversion': FIRMS_CONVERSION}

    is_valid, errors = validate(legal_filing, 'conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_filing_firms_conversion_schema():
    """Assert that the JSONSchema validator is working."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'conversion'
    filing['filing']['conversion'] = copy.deepcopy(FIRMS_CONVERSION)

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_valid_firms_conversion_with_any_required_element():
    """Assert valid if all of the required elements are present."""
    firms_conversion_json = copy.deepcopy(FIRMS_CONVERSION)
    del firms_conversion_json['nameRequest']
    del firms_conversion_json['offices']
    del firms_conversion_json['parties']
    legal_filing = {'conversion': firms_conversion_json}

    is_valid, errors = validate(legal_filing, 'conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_invalid_firms_conversion_with_no_required_element():
    """Assert not valid if required elements are not present."""
    firms_conversion_json = copy.deepcopy(FIRMS_CONVERSION)
    del firms_conversion_json['nameRequest']
    del firms_conversion_json['offices']
    del firms_conversion_json['parties']
    del firms_conversion_json['business']
    del firms_conversion_json['startDate']
    legal_filing = {'conversion': firms_conversion_json}

    is_valid, errors = validate(legal_filing, 'conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_firms_conversion_with_no_contact():
    """Assert not valid if contact point is not present."""
    firms_conversion_no_business_json = copy.deepcopy(FIRMS_CONVERSION)
    del firms_conversion_no_business_json['contactPoint']
    legal_filing = {'conversion': firms_conversion_no_business_json}

    is_valid, errors = validate(legal_filing, 'conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_name_request_firms_conversion():
    """Assert not valid if name request does not contain required elements."""
    firms_conversion_json = copy.deepcopy(FIRMS_CONVERSION)
    del firms_conversion_json['nameRequest']['legalType']
    legal_filing = {'conversion': firms_conversion_json}

    is_valid, errors = validate(legal_filing, 'conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_firms_conversion_with_invalid_date():
    """Assert not valid if required elements are not present."""
    firms_conversion_json = copy.deepcopy(FIRMS_CONVERSION)
    firms_conversion_json['startDate'] = "test"
    legal_filing = {'conversion': firms_conversion_json}

    is_valid, errors = validate(legal_filing, 'conversion')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
