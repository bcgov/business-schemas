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
"""Assert required string fields reject empty/whitespace-only values.

Required string fields carry a ``\\S`` pattern so that a blank or
whitespace-only value fails schema validation instead of being accepted as
valid-but-empty data. The pattern only requires at least one non-whitespace
character anywhere in the value, so leading/trailing whitespace and multi-line
content are still allowed.
"""
import copy

import pytest

import registry_schemas.example_data as ed
from registry_schemas.example_data import ADDRESS, AGM_EXTENSION, AGM_LOCATION_CHANGE
from registry_schemas.utils import validate


BLANK_VALUES = ['', ' ', '   ', '\t', '\n', '  \t \n ']


def test_address_baseline_valid():
    """Assert the example address validates."""
    valid, _ = validate(ADDRESS, 'address')
    assert valid


def test_agm_extension_baseline_valid():
    """Assert the example agm_extension validates."""
    valid, _ = validate({'agmExtension': AGM_EXTENSION}, 'agm_extension')
    assert valid


def test_agm_location_change_baseline_valid():
    """Assert the example agm_location_change validates."""
    valid, _ = validate({'agmLocationChange': AGM_LOCATION_CHANGE}, 'agm_location_change')
    assert valid


@pytest.mark.parametrize('field', ['streetAddress', 'addressCity', 'addressCountry'])
@pytest.mark.parametrize('blank', BLANK_VALUES)
def test_address_required_strings_reject_blank(field, blank):
    """Assert blank/whitespace-only required address fields fail validation."""
    address = copy.deepcopy(ADDRESS)
    address[field] = blank

    valid, _ = validate(address, 'address')

    assert not valid


@pytest.mark.parametrize('blank', BLANK_VALUES)
def test_agm_extension_year_rejects_blank(blank):
    """Assert a blank/whitespace-only agmExtension.year fails validation."""
    agm_extension = copy.deepcopy(AGM_EXTENSION)
    agm_extension['year'] = blank

    valid, _ = validate({'agmExtension': agm_extension}, 'agm_extension')

    assert not valid


@pytest.mark.parametrize('field', ['year', 'reason', 'agmLocation'])
@pytest.mark.parametrize('blank', BLANK_VALUES)
def test_agm_location_change_required_strings_reject_blank(field, blank):
    """Assert blank/whitespace-only required agmLocationChange fields fail validation."""
    agm_location_change = copy.deepcopy(AGM_LOCATION_CHANGE)
    agm_location_change[field] = blank

    valid, _ = validate({'agmLocationChange': agm_location_change}, 'agm_location_change')

    assert not valid


def _party(officer):
    """Build a minimal-but-valid party around the given officer."""
    return {
        'officer': officer,
        'roles': [{'roleType': 'Director', 'appointmentDate': '2020-01-01'}],
        'mailingAddress': {
            'streetAddress': '123 Main St',
            'addressCity': 'Victoria',
            'addressCountry': 'CA'
        }
    }


def test_party_baseline_valid():
    """Assert minimal person and organization parties validate."""
    person = _party({'partyType': 'person', 'firstName': 'Joe', 'lastName': 'Swanson'})
    org = _party({'partyType': 'organization', 'organizationName': 'Acme Inc'})

    assert validate({'parties': [person, org]}, 'parties')[0]


@pytest.mark.parametrize('blank', BLANK_VALUES)
def test_party_person_lastname_rejects_blank(blank):
    """Assert a blank/whitespace-only lastName fails for a person party."""
    person = _party({'partyType': 'person', 'firstName': 'Joe', 'lastName': blank})

    valid, _ = validate({'parties': [person]}, 'parties')

    assert not valid


@pytest.mark.parametrize('blank', BLANK_VALUES)
def test_party_org_organizationname_rejects_blank(blank):
    """Assert a blank/whitespace-only organizationName fails for an organization party."""
    org = _party({'partyType': 'organization', 'organizationName': blank})

    valid, _ = validate({'parties': [org]}, 'parties')

    assert not valid


def test_party_person_allows_empty_organizationname():
    """Assert the conditional pattern does not reject a person carrying an empty organizationName.

    organizationName is only required for organizations; a person party that
    still carries ``organizationName: ''`` (as real submissions do) must remain
    valid. This guards against applying the non-empty pattern unconditionally.
    """
    person = _party({
        'partyType': 'person',
        'firstName': 'Joe',
        'lastName': 'Swanson',
        'organizationName': ''
    })

    assert validate({'parties': [person]}, 'parties')[0]


# ---------------------------------------------------------------------------
# Exhaustive sweep: every required string field that carries the \S pattern.
#
# Each case validates a document with the target field present and asserts a
# pattern ("does not match") error fires at that field's path. This proves the
# pattern is wired up without needing a fully-valid baseline (so it is robust
# to conditional branches and to fields that are deeply nested).
# ---------------------------------------------------------------------------

def _flatten_errors(errors):
    """Flatten a jsonschema error iterator, descending into anyOf/oneOf/allOf context."""
    flat = []
    for err in errors or []:
        flat.append(err)
        flat.extend(_flatten_errors(err.context))
    return flat


def _has_pattern_error(document, schema_name, field):
    """Return True if validation reports a pattern error at the given leaf field."""
    valid, errors = validate(document, schema_name)
    if valid:
        return False
    return any(
        'does not match' in err.message and err.absolute_path and err.absolute_path[-1] == field
        for err in _flatten_errors(errors)
    )


_ADDRESS_OK = {'streetAddress': '123 Main St', 'addressCity': 'Victoria', 'addressCountry': 'CA'}


def _address(field, value):
    return {**_ADDRESS_OK, field: value}


def _amalgamation_application(value):
    doc = copy.deepcopy(ed.AMALGAMATION_APPLICATION)
    doc['amalgamatingBusinesses'] = [{
        'role': 'amalgamating',
        'identifier': 'BC1234567',
        'foreignJurisdiction': {'country': 'CA', 'region': 'AB'},
        'legalName': value
    }]
    return {'amalgamationApplication': doc}


def _business_document_registrar(value):
    return {'registrarInfo': {
        'endDate': None, 'name': value,
        'startDate': '2022-06-01T00:00:00', 'title': 'Registrar of Companies'
    }}


def _continuation_in_fj(field, value):
    doc = copy.deepcopy(ed.CONTINUATION_IN)
    doc['foreignJurisdiction'][field] = value
    return {'continuationIn': doc}


def _continuation_in_file(field, value):
    doc = copy.deepcopy(ed.CONTINUATION_IN)
    doc['authorization']['files'][0][field] = value
    return {'continuationIn': doc}


def _director(field, value):
    officer = {'firstName': 'Joe', 'lastName': 'Swanson'}
    officer[field] = value
    return {'directors': [{
        'officer': officer,
        'deliveryAddress': _ADDRESS_OK,
        'appointmentDate': '2020-01-01',
        'cessationDate': None
    }]}


def _filing_certified_by(value):
    doc = copy.deepcopy(ed.FILING_HEADER)
    doc['filing']['header']['certifiedBy'] = value
    return doc


def _share_structure(which, value):
    series = {
        'name': 'Series A', 'priority': 1, 'maxNumberOfShares': 10,
        'hasMaximumShares': True, 'hasRightsOrRestrictions': False
    }
    share_class = {
        'name': 'Common', 'priority': 1, 'maxNumberOfShares': 100, 'parValue': 1,
        'currency': 'CAD', 'hasMaximumShares': True, 'hasParValue': True,
        'hasRightsOrRestrictions': True, 'series': [series]
    }
    if which == 'class':
        share_class['name'] = value
    else:
        series['name'] = value
    return {'shareClasses': [share_class]}


# (id, schema_name, builder(value) -> document, leaf_field)
PATTERNED_FIELDS = [
    ('address.streetAddress', 'address', lambda v: _address('streetAddress', v), 'streetAddress'),
    ('address.addressCity', 'address', lambda v: _address('addressCity', v), 'addressCity'),
    ('address.addressCountry', 'address', lambda v: _address('addressCountry', v), 'addressCountry'),
    ('agm_extension.year', 'agm_extension',
     lambda v: {'agmExtension': {'year': v, 'isFirstAgm': True, 'extReqForAgmYear': True}}, 'year'),
    ('agm_location_change.year', 'agm_location_change',
     lambda v: {'agmLocationChange': {'year': v, 'reason': 'r', 'agmLocation': 'loc'}}, 'year'),
    ('agm_location_change.reason', 'agm_location_change',
     lambda v: {'agmLocationChange': {'year': '2023', 'reason': v, 'agmLocation': 'loc'}}, 'reason'),
    ('agm_location_change.agmLocation', 'agm_location_change',
     lambda v: {'agmLocationChange': {'year': '2023', 'reason': 'r', 'agmLocation': v}}, 'agmLocation'),
    ('amalgamation_application.legalName', 'amalgamation_application',
     _amalgamation_application, 'legalName'),
    ('amalgamation_out.details', 'amalgamation_out',
     lambda v: {'amalgamationOut': {**copy.deepcopy(ed.AMALGAMATION_OUT), 'details': v}}, 'details'),
    ('amalgamation_out.legalName', 'amalgamation_out',
     lambda v: {'amalgamationOut': {**copy.deepcopy(ed.AMALGAMATION_OUT), 'legalName': v}}, 'legalName'),
    ('business_document.entityAct', 'business_document', lambda v: {'entityAct': v}, 'entityAct'),
    ('business_document.entityDescription', 'business_document',
     lambda v: {'entityDescription': v}, 'entityDescription'),
    ('business_document.registrarInfo.name', 'business_document', _business_document_registrar, 'name'),
    ('comment.comment', 'comment', lambda v: {'comment': {'comment': v, 'filingId': 1}}, 'comment'),
    ('contact_point.email', 'contactPoint', lambda v: {'email': v}, 'email'),
    ('continuation_in.foreignJurisdiction.identifier', 'continuation_in',
     lambda v: _continuation_in_fj('identifier', v), 'identifier'),
    ('continuation_in.foreignJurisdiction.legalName', 'continuation_in',
     lambda v: _continuation_in_fj('legalName', v), 'legalName'),
    ('continuation_in.authorization.fileKey', 'continuation_in',
     lambda v: _continuation_in_file('fileKey', v), 'fileKey'),
    ('continuation_in.authorization.fileName', 'continuation_in',
     lambda v: _continuation_in_file('fileName', v), 'fileName'),
    ('continuation_out.legalName', 'continuation_out',
     lambda v: {'continuationOut': {**copy.deepcopy(ed.CONTINUATION_OUT), 'legalName': v}}, 'legalName'),
    ('cooperative.rulesFileKey', 'cooperative',
     lambda v: {**copy.deepcopy(ed.COOPERATIVE), 'rulesFileKey': v}, 'rulesFileKey'),
    ('cooperative.memorandumFileKey', 'cooperative',
     lambda v: {**copy.deepcopy(ed.COOPERATIVE), 'memorandumFileKey': v}, 'memorandumFileKey'),
    ('correction.comment', 'correction',
     lambda v: {'correction': {'correctedFilingId': 1, 'correctedFilingType': 'changeOfAddress', 'comment': v}},
     'comment'),
    ('diff.path', 'diff', lambda v: {'diff': [{'oldValue': 1, 'newValue': 2, 'path': v}]}, 'path'),
    ('directors.firstName', 'directors', lambda v: _director('firstName', v), 'firstName'),
    ('directors.lastName', 'directors', lambda v: _director('lastName', v), 'lastName'),
    ('filing.certifiedBy', 'filing', _filing_certified_by, 'certifiedBy'),
    ('foreign_jurisdiction.country', 'foreign_jurisdiction', lambda v: {'country': v}, 'country'),
    ('registrars_notation.orderDetails', 'registrars_notation',
     lambda v: {'registrarsNotation': {'orderDetails': v}}, 'orderDetails'),
    ('registrars_order.orderDetails', 'registrars_order',
     lambda v: {'registrarsOrder': {'orderDetails': v}}, 'orderDetails'),
    ('share_structure.shareClass.name', 'share_structure', lambda v: _share_structure('class', v), 'name'),
    ('share_structure.shareSeries.name', 'share_structure', lambda v: _share_structure('series', v), 'name'),
    ('transparency_register.ledgerReferenceNumber', 'transparency_register',
     lambda v: {'transparencyRegister': {'type': 'initial', 'ledgerReferenceNumber': v}}, 'ledgerReferenceNumber'),
    ('unmanaged.displayName', 'unmanaged', lambda v: {'unManaged': {'displayName': v}}, 'displayName'),
]

_SWEEP_PARAMS = [(schema, builder, field) for _id, schema, builder, field in PATTERNED_FIELDS]
_SWEEP_IDS = [case[0] for case in PATTERNED_FIELDS]


@pytest.mark.parametrize('schema_name,builder,field', _SWEEP_PARAMS, ids=_SWEEP_IDS)
@pytest.mark.parametrize('blank', ['', '   ', '\t'])
def test_patterned_field_rejects_blank(schema_name, builder, field, blank):
    """Assert every patterned field rejects blank/whitespace-only values."""
    assert _has_pattern_error(builder(blank), schema_name, field)


@pytest.mark.parametrize('schema_name,builder,field', _SWEEP_PARAMS, ids=_SWEEP_IDS)
def test_patterned_field_accepts_nonblank(schema_name, builder, field):
    """Assert a non-blank value does not trip the non-empty pattern at the field."""
    assert not _has_pattern_error(builder('Valid value'), schema_name, field)
