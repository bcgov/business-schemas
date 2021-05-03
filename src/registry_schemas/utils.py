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
"""Utilities to load and validate against JSONSchemas.

Test helper functions to load and assert that a JSON payload validates against a defined schema.
"""
import json
from itertools import chain
from os import listdir, path
from typing import Tuple

from jsonschema import Draft7Validator, SchemaError, draft7_format_checker

from registry_schemas.schema_validation_info import SchemaValidationInfo
from registry_schemas.schema_validation_info_factory import SchemaValidationInfoFactory


BASE_URI = 'https://bcrs.gov.bc.ca/.well_known/schemas'


def get_schema(filename: str) -> dict:
    """Return the given schema file identified by filename."""
    return _load_json_schema(filename)


def _load_json_schema(filename: str):
    """Return the given schema file identified by filename."""
    relative_path = path.join('schemas', filename)
    absolute_path = path.join(path.dirname(__file__), relative_path)

    with open(absolute_path, 'r') as schema_file:
        schema = json.loads(schema_file.read())

        return schema


def get_schema_store(validate_schema: bool = False, schema_search_path: str = None) -> dict:
    """Return a schema_store as a dict.

    The default returns schema_store of the default schemas found in this package.
    """
    try:
        if not schema_search_path:
            schema_search_path = path.join(path.dirname(__file__), 'schemas')
        schemastore = {}
        fnames = listdir(schema_search_path)
        for fname in fnames:
            fpath = path.join(schema_search_path, fname)
            if fpath[-5:] == '.json':
                with open(fpath, 'r') as schema_fd:
                    schema = json.load(schema_fd)
                    if '$id' in schema:
                        schemastore[schema['$id']] = schema

        if validate_schema:
            for _, schema in schemastore.items():
                Draft7Validator.check_schema(schema)

        return schemastore
    except (SchemaError, json.JSONDecodeError) as error:
        # handle schema error
        raise error


def validate(json_data: json,
             schema_id: str,
             schema_store: dict = None,
             validate_schema: bool = False,
             schema_search_path: str = None
             ) -> Tuple[bool, iter]:
    """Load the json file and validate against loaded schema."""
    try:

        schema_store = get_schema_store(validate_schema, schema_search_path)
        svi_factory = SchemaValidationInfoFactory(schema_store, validate_schema, schema_search_path)
        svi = svi_factory.get_schema_validation_info(schema_id)

        is_valid, errors = validate_json(json_data, svi)

        # validate filing type against specific filing type schema if supported.
        # This is needed to provide error messages to the specific filing in the
        # returned validation error messages.  The filing schema as it is defined
        # currently with the anyOf condition will only indicate that the validated
        # json is not valid under any of the given schemas.

        filing_type = get_filing_type(json_data)

        if schema_id == 'filing' and filing_type and nested_filing_validation_supported(filing_type):
            filing_svi = svi_factory.get_schema_validation_info(filing_type)
            is_valid_filing, filing_errors = \
                validate_json(json_data['filing'][filing_type],
                              filing_svi,
                              path.join('filing', filing_type))
            if not is_valid_filing:
                # merge errors from base filing schema validation errors
                errors = filing_errors if is_valid else chain(errors, filing_errors)
                return False, errors

        return is_valid, errors

    except SchemaError as error:
        # handle schema error
        return False, error


def validate_json(json_data: json,
                  svi: SchemaValidationInfo,
                  custom_schema_path_prefix: str = None
                  ) -> Tuple[bool, iter]:
    """Validate json data against schema."""
    if svi.validate_schema:
        Draft7Validator.check_schema(svi.schema)

    if Draft7Validator(svi.schema,
                       format_checker=draft7_format_checker,
                       resolver=svi.resolver
                       ) \
            .is_valid(json_data):
        return True, None

    errors = Draft7Validator(svi.schema,
                             format_checker=draft7_format_checker,
                             resolver=svi.resolver
                             ) \
        .iter_errors(json_data)

    if custom_schema_path_prefix:
        errors = update_errors_with_custom_path_prefix(custom_schema_path_prefix, errors)

    return False, errors


def get_filing_type(filing_json: json):
    """Get filing type from filing json."""
    filing = filing_json.get('filing', None)
    if not filing:
        return None

    return \
        next((x for x in filing.keys() if x in
              ['annualReport', 'changeOfDirectors', 'changeOfAddress',
               'voluntaryDissolution', 'specialResolution', 'changeOfName',
               'incorporationApplication', 'amalgamationApplication',
               'dissolved', 'amendedAGM', 'restorationApplication',
               'amendedAnnualReport', 'amendedChangeOfDirectors',
               'voluntaryLiquidation', 'appointReceiver', 'continuedOut',
               'correction', 'alteration', 'conversion', 'transition']), None)


def nested_filing_validation_supported(filing_type):
    """Determine if nested filing validation is supported for given filing type."""
    return filing_type in ['alteration']


def update_errors_with_custom_path_prefix(custom_schema_path_prefix: str, errors: iter):
    """Update errors with provided custom prefix path.

    This is required in cases where there is custom logic in place to validate
    properties within json data as a separately.  The appending of the custom
    prefix path will allow the final error message to have context relevant
    to the top level schema being validated.  e.g. /filing/alteration/courtOrder
    as opposed to /courtOrder
    """
    return map(lambda x: append_path_prefix_to_error(custom_schema_path_prefix, x), errors)


def append_path_prefix_to_error(custom_schema_path_prefix: str, error: any):
    """Append custom schema prefix to start of error path."""
    error.path.appendleft(custom_schema_path_prefix)
    return error
