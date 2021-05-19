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
"""Factory class for retrieving schema validation related info."""

from os import path

from jsonschema import RefResolver

from registry_schemas.schema_validation_info import SchemaValidationInfo


BASE_URI = 'https://bcrs.gov.bc.ca/.well_known/schemas'


class SchemaValidationInfoFactory:  # pylint: disable=too-few-public-methods
    """SchemaValidationInfoFactory object.

    Factory class to help with retrieving schema validation related info
    """

    def __init__(self,
                 schema_store: dict = None,
                 validate_schema: bool = False,
                 schema_search_path: str = None):
        """Initialize SchemaValidationInfoFactory object."""
        self._schema_search_path = schema_search_path
        self._schema_store = schema_store
        self._validate_schema = validate_schema
        self._init()

    def _init(self):
        if not self._schema_search_path:
            self._schema_search_path = path.join(path.dirname(__file__), 'schemas')

    def get_schema_validation_info(self, schema_id: str):
        """Get schema valiation info specific to a schema_id."""
        schema = self._schema_store.get(f'{BASE_URI}/{schema_id}')
        schema_file_path = path.join(self._schema_search_path, schema_id)
        resolver = RefResolver(f'file://{schema_file_path}.json', schema, self._schema_store)
        return SchemaValidationInfo(schema_id=schema_id,
                                    schema_search_path=self._schema_search_path,
                                    schema_store=self._schema_store,
                                    validate_schema=self._validate_schema,
                                    schema_file_path=schema_file_path,
                                    schema=schema, resolver=resolver)
