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
"""Test Suite data used across many tests.

Test array used in multiple pytests, and several filings that can be used in tests.
"""
# testdata pattern is ({str: environment}, {expected return value})
TEST_SCHEMAS_DATA = [
    ('address.json'),
    ('admin_freeze.json'),
    ('affiliated_businesses.json'),
    ('agm_extension.json'),
    ('agm_location_change.json'),
    ('agreement_type.json'),
    ('alteration.json'),
    ('amalgamation_application.json'),
    ('amalgamation_out.json'),
    ('annual_report.json'),
    ('business_document.json'),
    ('business.json'),
    ('change_of_address.json'),
    ('change_of_directors.json'),
    ('change_of_liquidators.json'),
    ('change_of_name.json'),
    ('change_of_officers.json'),
    ('change_of_receivers.json'),
    ('change_of_registration.json'),
    ('comment.json'),
    ('consent_amalgamation_out.json'),
    ('consent_continuation_out.json'),
    ('contact_point.json'),
    ('continuation_in.json'),
    ('continuation_out.json'),
    ('conversion.json'),
    ('cooperative.json'),
    ('correction_amalgamation.json'),
    ('correction_continuation_in.json'),
    ('correction_out.json'),
    ('correction.json'),
    ('court_order.json'),
    ('diff.json'),
    ('directors.json'),
    ('dissolution.json'),
    ('filing_group_combined_ar.json'),
    ('filing_group_coop_dissolution.json'),
    ('filing_group_singular.json'),
    ('filing_group_special_resolution.json'),
    ('filing.json'),
    ('foreign_jurisdiction.json'),
    ('header.json'),
    ('incorporation_application.json'),
    ('naics.json'),
    ('name_request.json'),
    ('name_translations.json'),
    ('notice_of_withdrawal.json'),
    ('office.json'),
    ('organization.json'),
    ('party.json'),
    ('person.json'),
    ('put_back_off.json'),
    ('put_back_on.json'),
    ('registrars_notation.json'),
    ('registrars_order.json'),
    ('registration.json'),
    ('relationship.json'),
    ('restoration.json'),
    ('share_structure.json'),
    ('special_resolution.json'),
    ('stub_filing.json'),
    ('task.json'),
    ('todo.json'),
    ('transition.json'),
    ('transparency_register.json'),
    ('unmanaged.json')
]
