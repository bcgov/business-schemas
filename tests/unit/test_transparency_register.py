# Copyright © 2025 Province of British Columbia
#
# Licensed under the BSD 3 Clause License, (the "License");
# you may not use this file except in compliance with the License.
# The template for the license can be found here
#    https://opensource.org/license/bsd-3-clause/
#
# Redistribution and use in source and binary forms,
# with or without modification, are permitted provided that the
# following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# 3. Neither the name of the copyright holder nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS”
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
"""Test Suite to ensure tranparency register schemas are valid."""
import copy

from registry_schemas import validate
from registry_schemas.example_data import BUSINESS, FILING_HEADER, TRANSPARENCY_REGISTER


def test_schema_success():
    """Assert the validator is working as expected when valid."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'transparencyRegister'
    filing['filing']['business'] = BUSINESS
    filing['filing']['transparencyRegister'] = TRANSPARENCY_REGISTER

    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


def test_wrong_type():
    """Assert the validator is working as expected when invalid type."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'transparencyRegister'
    filing['filing']['business'] = BUSINESS
    filing['filing']['transparencyRegister'] = TRANSPARENCY_REGISTER

    filing['filing']['transparencyRegister']['type'] = 'invalid'
    is_valid, _ = validate(filing, 'transparency_register')

    assert not is_valid


def test_no_reference_number():
    """Assert the validator is working as expected when invalid reference number."""
    filing = copy.deepcopy(FILING_HEADER)
    filing['filing']['header']['name'] = 'transparencyRegister'
    filing['filing']['business'] = BUSINESS
    filing['filing']['transparencyRegister'] = TRANSPARENCY_REGISTER

    del filing['filing']['transparencyRegister']['ledgerReferenceNumber']
    is_valid, _ = validate(filing, 'transparency_register')

    assert not is_valid
