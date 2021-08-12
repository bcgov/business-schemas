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
"""Test Suite to ensure order schemas are valid."""

import copy

from registry_schemas import validate
from registry_schemas.example_data import COURT_ORDER


def test_court_order_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'courtOrder': COURT_ORDER}
    is_valid, errors = validate(legal_filing, 'court_order')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_valid_court_order():
    """Assert valid if all of the required fields are present."""
    order_json = copy.deepcopy(COURT_ORDER)
    del order_json['effectOfOrder']
    del order_json['orderDate']
    del order_json['orderDetails']
    legal_filing = {'courtOrder': order_json}

    is_valid, errors = validate(legal_filing, 'court_order')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_validate_invalid_court_order():
    """Assert invalid if required fields are missing."""
    order_json = copy.deepcopy(COURT_ORDER)
    del order_json['fileNumber']

    is_valid, errors = validate(order_json, 'court_order')

    assert not is_valid
