# Copyright (c) 2026, Province of British Columbia

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.

# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.

# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""Test Suite to ensure multi filing schemas are valid or invalid as required."""
import copy
from datetime import datetime

import pytest

from registry_schemas import validate
from registry_schemas.example_data import (
    ALTERATION,
    ANNUAL_REPORT,
    CHANGE_OF_ADDRESS,
    CHANGE_OF_DIRECTORS,
    CHANGE_OF_NAME,
    CHANGE_OF_REGISTRATION,
    CORRECTION_COL,
    INCORPORATION,
    REGISTRATION,
    SPECIAL_RESOLUTION,
    get_filing_template
)

FILING_TYPE_MAPPER = {
    'alteration': ALTERATION,
    'annualReport': ANNUAL_REPORT['filing']['annualReport'],
    'changeOfAddress': CHANGE_OF_ADDRESS,
    'changeOfDirectors': CHANGE_OF_DIRECTORS,
    'changeOfName': CHANGE_OF_NAME,
    'changeOfRegistration': CHANGE_OF_REGISTRATION,
    'correction': CORRECTION_COL['filing']['correction'],
    'incorporationApplication': INCORPORATION,
    'registration': REGISTRATION,
    'specialResolution': SPECIAL_RESOLUTION,
}


@pytest.mark.parametrize('identifier, filing_type, extra_filing_types, expected',[
    ('CP1234567', 'annualReport', [], True),
    ('CP1234567', 'annualReport', ['changeOfAddress'], True),
    ('CP1234567', 'annualReport', ['changeOfDirectors'], True),
    ('CP1234567', 'annualReport', ['changeOfAddress', 'changeOfDirectors'], True),
    ('CP1234567', 'annualReport', ['alteration'], False),
    ('CP1234567', 'annualReport', ['correction'], False),
    ('CP1234567', 'annualReport', ['correction'], False),
    ('CP1234567', 'annualReport', ['incorporationApplication'], False),
    ('CP1234567', 'changeOfAddress', [], True),
    ('CP1234567', 'changeOfAddress', ['alteration'], False),
    ('CP1234567', 'changeOfAddress', ['changeOfDirectors'], False),
    ('CP1234567', 'changeOfAddress', ['incorporationApplication'], False),
    ('CP1234567', 'changeOfAddress', ['specialResolution'], False),
    ('CP1234567', 'changeOfAddress', ['annualReport'], False),
    ('CP1234567', 'changeOfDirectors', [], True),
    ('CP1234567', 'changeOfDirectors', ['alteration'], False),
    ('CP1234567', 'changeOfDirectors', ['changeOfAddress'], False),
    ('CP1234567', 'changeOfDirectors', ['incorporationApplication'], False),
    ('CP1234567', 'changeOfDirectors', ['specialResolution'], False),
    ('CP1234567', 'changeOfDirectors', ['annualReport'], False),
    ('CP1234567', 'specialResolution', [], True),
    ('CP1234567', 'specialResolution', ['alteration'], True),
    ('CP1234567', 'specialResolution', ['changeOfName'], True),
    ('CP1234567', 'specialResolution', ['alteration','changeOfName'], True),
    ('BC1234567', 'annualReport', [], True),
    ('BC1234567', 'annualReport', ['changeOfAddress'], False),
    ('BC1234567', 'annualReport', ['changeOfDirectors'], False),
    ('BC1234567', 'changeOfAddress', [], True),
    ('BC1234567', 'changeOfAddress', ['changeOfDirectors'], False),
    ('BC1234567', 'changeOfDirectors', [], True),
    ('BC1234567', 'changeOfDirectors', ['changeOfAddress'], False),
    ('BC1234567', 'alteration', [], True),
    ('BC1234567', 'alteration', ['changeOfAddress'], False),
    ('BC1234567', 'alteration', ['specialResolution'], False),
    ('BC1234567', 'alteration', ['incorporationApplication'], False),
    ('BC1234567', 'alteration', ['correction'], False),
    ('BC1234567', 'incorporationApplication', [], True),
    ('BC1234567', 'incorporationApplication', ['correction'], False),
    ('BC1234567', 'correction', [], True),
    ('BC1234567', 'correction', ['annualReport'], False),
    ('FM1234567', 'registration', [], True),
    ('FM1234567', 'registration', ['correction'], False),
    ('FM1234567', 'changeOfRegistration', [], True),
    ('FM1234567', 'changeOfRegistration', ['correction'], False),
])
def test_multi_filings(identifier, filing_type, extra_filing_types, expected):
    """Assert that the schema is performing as expected for multi filings."""
    
    filing = get_filing_template(filing_type, identifier)
    filing['filing'][filing_type] = copy.deepcopy(FILING_TYPE_MAPPER[filing_type])
    for extra_filing_type in extra_filing_types:
        filing['filing'][extra_filing_type] = copy.deepcopy(FILING_TYPE_MAPPER[extra_filing_type])

    print(filing)
    is_valid, errors = validate(filing, 'filing')

    if errors:
        for err in errors:
            print(err.message)

    assert is_valid == expected
