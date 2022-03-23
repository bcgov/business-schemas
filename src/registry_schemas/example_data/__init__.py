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
"""Example JSON segments and filings that are known to work.

These can be used in other tests as basis for the JSON filings.
"""
from .schema_data import (
    ADDRESS,
    ALL_FILINGS,
    ALTERATION,
    ALTERATION_FILING_TEMPLATE,
    ANNUAL_REPORT,
    BUSINESS,
    BUSINESS_HISTORICAL,
    CHANGE_OF_ADDRESS,
    CHANGE_OF_DIRECTORS,
    CHANGE_OF_DIRECTORS_MAILING,
    CHANGE_OF_NAME,
    CHANGE_OF_REGISTRATION,
    CHANGE_OF_REGISTRATION_TEMPLATE,
    COMMENT_BUSINESS,
    COMMENT_FILING,
    CONVERSION,
    CONVERSION_FILING_TEMPLATE,
    COOP_INCORPORATION,
    COOP_INCORPORATION_FILING_TEMPLATE,
    CORP_CHANGE_OF_ADDRESS,
    CORRECTION_AR,
    CORRECTION_COA,
    CORRECTION_COD,
    CORRECTION_COMBINED_AR,
    CORRECTION_INCORPORATION,
    COURT_ORDER,
    COURT_ORDER_FILING_TEMPLATE,
    CP_SPECIAL_RESOLUTION_TEMPLATE,
    DISSOLUTION,
    FILING_HEADER,
    FILING_TEMPLATE,
    FILINGS_WITH_TYPES,
    INCORPORATION,
    INCORPORATION_FILING_TEMPLATE,
    REGISTRARS_NOTATION,
    REGISTRARS_NOTATION_FILING_TEMPLATE,
    REGISTRARS_ORDER,
    REGISTRARS_ORDER_FILING_TEMPLATE,
    REGISTRATION,
    RESTORATION,
    SPECIAL_RESOLUTION,
    STUB_FILING,
    TRANSITION,
    TRANSITION_FILING_TEMPLATE,
    UNMANAGED,
)


__all__ = [
    'ALL_FILINGS',
    'ANNUAL_REPORT',
    'BUSINESS',
    'BUSINESS_HISTORICAL',
    'CHANGE_OF_ADDRESS',
    'CHANGE_OF_DIRECTORS',
    'CHANGE_OF_NAME',
    'CHANGE_OF_REGISTRATION',
    'CHANGE_OF_REGISTRATION_TEMPLATE',
    'COMMENT_BUSINESS',
    'COMMENT_FILING',
    'COOP_INCORPORATION',
    'COOP_INCORPORATION_FILING_TEMPLATE',
    'CORP_CHANGE_OF_ADDRESS',
    'CORRECTION_AR',
    'CORRECTION_COA',
    'CORRECTION_COD',
    'CORRECTION_COMBINED_AR',
    'CORRECTION_INCORPORATION',
    'COURT_ORDER',
    'COURT_ORDER_FILING_TEMPLATE',
    'DISSOLUTION',
    'FILING_HEADER',
    'FILING_TEMPLATE',
    'FILINGS_WITH_TYPES',
    'INCORPORATION',
    'INCORPORATION_FILING_TEMPLATE',
    'REGISTRARS_NOTATION',
    'REGISTRARS_NOTATION_FILING_TEMPLATE',
    'REGISTRARS_ORDER',
    'REGISTRARS_ORDER_FILING_TEMPLATE',
    'REGISTRATION',
    'RESTORATION',
    'SPECIAL_RESOLUTION',
    'STUB_FILING',
    'ALTERATION',
    'ALTERATION_FILING_TEMPLATE',
    'CONVERSION',
    'CONVERSION_FILING_TEMPLATE',
    'TRANSITION',
    'TRANSITION_FILING_TEMPLATE',
    'UNMANAGED',
]
