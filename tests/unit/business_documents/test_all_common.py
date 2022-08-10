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
"""Test Suite to ensure common functionality across all business document schemas are valid."""
import copy

import pytest

from registry_schemas import validate
from registry_schemas.example_data import COGS, CSTAT, LSEAL, SUMMARY
from registry_schemas.example_data.business_documents.common import OFFICES_BUS


BUSINESS_DOCUMENT_SCHEMAS = [COGS, CSTAT, LSEAL, SUMMARY]


@pytest.mark.parametrize('schema', BUSINESS_DOCUMENT_SCHEMAS)
def test_valid_schema(schema):
    """Assert that the schema is performing as expected."""
    is_valid, errors = validate(schema, 'business_document')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid


# @pytest.mark.parametrize('schema', BUSINESS_DOCUMENT_SCHEMAS)
# def test_valid_schema_business_office(schema):
#     """Assert that the schema is performing as expected with business office."""
#     schema_bus_office = copy.deepcopy(schema)
#     schema_bus_office['offices'] = OFFICES_BUS
#     is_valid, errors = validate(schema_bus_office, 'business_document')

#     if errors:
#         for err in errors:
#             print(err.message)
#     print(errors)

#     assert is_valid


# @pytest.mark.parametrize('schema', BUSINESS_DOCUMENT_SCHEMAS)
# def test_invalid_schema_missing_field(schema):
#     """Assert that the business document schema is invalid when missing required fields."""
#     required_fields = ['business', 'entityAct', 'entityDescription', 'registrarInfo', 'reportDateTime', 'reportType']
    
#     for field in required_fields:
#         invalid_schema = copy.deepcopy(schema)
#         del invalid_schema[field]

#         is_valid, errors = validate(invalid_schema, 'business_document')
#         assert not is_valid


# @pytest.mark.parametrize('schema', BUSINESS_DOCUMENT_SCHEMAS)
# def test_invalid_schema_business(schema):
#     """Assert that the business document schema is invalid when business is invalid."""
#     invalid_schema = copy.deepcopy(schema)
#     del invalid_schema['business']['identifier']

#     is_valid, errors = validate(invalid_schema, 'business_document')
#     assert not is_valid


# @pytest.mark.parametrize('schema', BUSINESS_DOCUMENT_SCHEMAS)
# def test_invalid_schema_registrar_info(schema):
#     """Assert that the business document schema is invalid when registrar info is invalid."""
#     invalid_schema = copy.deepcopy(schema)
#     del invalid_schema['registrarInfo']['name']

#     is_valid, errors = validate(invalid_schema, 'business_document')
#     assert not is_valid


# @pytest.mark.parametrize('schema', [LSEAL, SUMMARY])
# def test_invalid_schema_offices(schema):
#     """Assert that the business document schema is invalid when offices are invalid."""
#     invalid_schema = copy.deepcopy(schema)
#     del invalid_schema['offices']['registeredOffice']['streetAddress']

#     is_valid, errors = validate(invalid_schema, 'business_document')
#     assert not is_valid


# @pytest.mark.parametrize('schema', [LSEAL, SUMMARY])
# def test_invalid_schema_state_filings(schema):
#     """Assert that the business document schema is invalid when state filings are invalid."""
#     invalid_schema = copy.deepcopy(schema)
#     del invalid_schema['stateFilings']['filingName']

#     is_valid, errors = validate(invalid_schema, 'business_document')
#     assert not is_valid


# @pytest.mark.parametrize('schema', [SUMMARY])
# def test_invalid_schema_parties(schema):
#     """Assert that the business document schema is invalid when parties are invalid."""
#     invalid_schema = copy.deepcopy(schema)
#     del invalid_schema['parties'][0]['officer']

#     is_valid, errors = validate(invalid_schema, 'business_document')
#     assert not is_valid
