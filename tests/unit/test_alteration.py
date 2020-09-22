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
"""Test Suite to ensure alteration schemas are valid."""

import copy

from registry_schemas import validate
from registry_schemas.example_data import ALTERATION


def test_alteration_schema():
    """Assert that the JSONSchema validator is working."""
    is_valid, errors = validate(ALTERATION, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_valid_alteration_with_any_required_element():
    """Assert valid if all of the required alterations is present."""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['nameRequest']
    del alteration_json['provisionsRemoved']
    del alteration_json['nameTranslations']
    del alteration_json['shareStructure']

    is_valid, errors = validate(alteration_json, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_valid_alteration_with_unknown_legal_type():
    """Assert invalid if legal type is not defined in business json."""
    alteration_json = copy.deepcopy(ALTERATION)
    alteration_json['business']['legalType'] = 'benefitCompany'

    is_valid, errors = validate(alteration_json, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_alteration_with_no_business():
    """Assert not valid if business is not present."""
    alteration_no_business_json = copy.deepcopy(ALTERATION)
    del alteration_no_business_json['business']

    is_valid, errors = validate(alteration_no_business_json, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_alteration_with_no_contact():
    """Assert not valid if contact point is not present."""
    alteration_no_contact_json = copy.deepcopy(ALTERATION)

    del alteration_no_contact_json['contactPoint']

    is_valid, errors = validate(alteration_no_contact_json, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)


def test_validate_invalid_corp_name_alteration():
    """Assert not valid if corp name alteration does not contain required elements."""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['nameRequest']['legalType']

    is_valid, errors = validate(alteration_json, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_name_translation_alteration():
    """Assert not valid if name translation alteration does not contain mandatory elements."""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['nameTranslations']['modified']
    del alteration_json['nameTranslations']['ceased']
    del alteration_json['nameTranslations']['new']

    is_valid, errors = validate(alteration_json, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_invalid_share_structure_alteration():
    """Assert not valid if share structure alteration does not contain required elements."""
    alteration_json = copy.deepcopy(ALTERATION)
    del alteration_json['shareStructure']['shareClasses']

    is_valid, errors = validate(alteration_json, 'alteration')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
