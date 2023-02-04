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
"""Test Suite to ensure consent continuation out schemas are valid."""

import copy

from registry_schemas import validate
from registry_schemas.example_data import CONSENT_CONTINUATION_OUT


def test_consent_continuation_out_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'consentContinuationOut': copy.deepcopy(CONSENT_CONTINUATION_OUT)}

    is_valid, errors = validate(legal_filing, 'consent_continuation_out')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_consent_continuation_out_invalid_schema():
    """Assert that the JSONSchema validator is working."""
    legal_filing = {'consentContinuationOut': copy.deepcopy(CONSENT_CONTINUATION_OUT)}
    legal_filing['consentContinuationOut']['orderDetails'] = ''

    is_valid, errors = validate(legal_filing, 'consent_continuation_out')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
