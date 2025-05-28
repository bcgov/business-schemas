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

import pytest

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


@pytest.mark.parametrize('approval_type', [
    'courtOrder',
    'registrar'
])
def test_full_restoration(approval_type):
    """Assert that the JSONSchema validator is working."""
    restoration_json = copy.deepcopy(RESTORATION)
    restoration_json['approvalType'] = approval_type
    if approval_type == 'registrar':
        del restoration_json['courtOrder']
        restoration_json['noticeDate'] = '2023-01-18'
        restoration_json['applicationDate'] = '2023-01-18'
    restoration_json['relationships'] = ['Heir or Legal Representative', 'Officer', 'Director']

    legal_filing = {'restoration': restoration_json}
    is_valid, errors = validate(legal_filing, 'restoration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('approval_type', [
    'courtOrder',
    'registrar'
])
def test_limited_restoration(approval_type):
    """Assert that the JSONSchema validator is working."""
    restoration_json = copy.deepcopy(RESTORATION)
    restoration_json['type'] = 'limitedRestoration'
    restoration_json['expiry'] = '2023-01-18'

    restoration_json['approvalType'] = approval_type
    if approval_type == 'registrar':
        del restoration_json['courtOrder']
        restoration_json['noticeDate'] = '2023-01-18'
        restoration_json['applicationDate'] = '2023-01-18'

    legal_filing = {'restoration': restoration_json}
    is_valid, errors = validate(legal_filing, 'restoration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_limited_restoration_extension():
    """Assert that the JSONSchema validator is working."""
    restoration_json = copy.deepcopy(RESTORATION)
    restoration_json['type'] = 'limitedRestorationExtension'
    restoration_json['expiry'] = '2023-01-18'
    del restoration_json['nameRequest']
    del restoration_json['nameTranslations']

    legal_filing = {'restoration': restoration_json}
    is_valid, errors = validate(legal_filing, 'restoration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


@pytest.mark.parametrize('approval_type', [
    'courtOrder',
    'registrar'
])
def test_limited__to_full_restoration(approval_type):
    """Assert that the JSONSchema validator is working."""
    restoration_json = copy.deepcopy(RESTORATION)
    restoration_json['type'] = 'limitedRestorationToFull'

    restoration_json['approvalType'] = approval_type
    if approval_type == 'registrar':
        del restoration_json['courtOrder']
        restoration_json['noticeDate'] = '2023-01-18'
        restoration_json['applicationDate'] = '2023-01-18'

    restoration_json['relationships'] = ['Heir or Legal Representative', 'Officer', 'Director']

    legal_filing = {'restoration': restoration_json}
    is_valid, errors = validate(legal_filing, 'restoration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_restoration_invalid_registered_office_mailing_address():
    """Assert that a restoration is invalid if the registered office mailingAddress is missing."""
    restoration_json = copy.deepcopy(RESTORATION)
    restoration_json['type'] = 'fullRestoration' 
    restoration_json['approvalType'] = 'courtOrder' 
    del restoration_json['offices']['registeredOffice']['mailingAddress']
    legal_filing = {'restoration': restoration_json}

    is_valid, errors = validate(legal_filing, 'restoration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
