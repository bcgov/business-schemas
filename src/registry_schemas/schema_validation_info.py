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
"""SchemaValidationInfo stores info relevant to a specific schema validation.

Created to provide an easier way to pass schema validation info to a
validator and other areas of code which has a use for the schema
validation info.
"""


class SchemaValidationInfo:  # pylint: disable=too-few-public-methods
    """SchemaValidationInfo object."""

    schema_id = None
    schema_search_path = None
    schema_store = None
    validate_schema = False
    schema_file_path = None
    schema = None
    resolver = None

    def __init__(self, **attributes):
        """__init__ method."""
        self.__dict__.update(attributes)
