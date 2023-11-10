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

"""Test Suite to ensure agm extension schemas are valid."""
import copy
from registry_schemas import validate
from registry_schemas.example_data import AGM_EXTENSION 


def test_agm_extension_schema():
    """Assert that the JSONSchema validator is working."""
    agm_extension = copy.deepcopy(AGM_EXTENSION)
    ae_json = {'agmExtension': copy.deepcopy(agm_extension)}

    is_valid, errors = validate(ae_json, 'agm_extension')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert is_valid

def test_validate_no_agm_year():
    """Assert that an year node is present in the agm extension."""
    agm_extension = copy.deepcopy(AGM_EXTENSION)
    ale_json = {'agmExtension': agm_extension}
    del ale_json['agmExtension']['year']

    is_valid, errors = validate(ale_json, 'agm_extension')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_is_first_agm():
    """Assert that an isFirstAgm node is present in the agm extension."""
    agm_extension = copy.deepcopy(AGM_EXTENSION)
    ale_json = {'agmExtension': agm_extension}
    del ale_json['agmExtension']['isFirstAgm']

    is_valid, errors = validate(ale_json, 'agm_extension')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid


def test_validate_no_ext_req_for_agm_year():
    """Assert that an extReqForAgmYear node is present in the agm extension."""
    agm_extension = copy.deepcopy(AGM_EXTENSION)
    ale_json = {'agmExtension': agm_extension}
    del ale_json['agmExtension']['extReqForAgmYear']

    is_valid, errors = validate(ale_json, 'agm_extension')

    if errors:
        for err in errors:
            print(err.message)
    print(errors)

    assert not is_valid
