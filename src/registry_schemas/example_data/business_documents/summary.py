# Copyright © 2022 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Example JSON segments of Business Summary."""
from .common import BUSINESS, OFFICES, PARTIES, REGISTRAR_INFO, STATE_FILINGS

SUMMARY = {
    'alterations': [
        {
            'filingDateTime': '2021-12-16T00:02:59.809174+00:00',
            'fromLegalName': 'Test Name 1',
            'toLegalName': 'Test Name 2',
            'fromLegalType': 'BEN',
            'toLegalType': 'BC'
        },
        {
            'filingDateTime': '2021-12-17T23:59:00.809174+00:00',
            'fromLegalType': 'BC',
            'toLegalType': 'BEN'
        }
    ],
    'amalgamatedEntities': [
        {
            'identifier': 'BC1234567',
            'name': 'Amalgamated Entity'
        },
        {
            'identifier': 'Not Available',
            'name': 'Not Available'
        }
    ],
    'business': BUSINESS,
    'entityAct': 'Business Corporations Act',
    'entityDescription': 'BC Benefit Company',
    'liquidation': {
        'filingDateTime': '2022-01-30T00:00:00.999999+00:00'
    },
    'listOfTranslations': [
        {
            'id': '319',
            'name': 'TEST TRANSLATION A',
            'type': 'TRANSLATION'
        },
        {
            'id': '320',
            'name': 'TEST TRANSLATION B',
            'type': 'TRANSLATION'
        }
    ],
    'nameChanges': [
        {
            'filingDateTime': '2021-12-28T21:40:16.696239+00:00',
            'fromLegalName': 'LM LOGISTICS INC.',
            'toLegalName': '0870884 B.C. LTD.'
        },
        {
            'filingDateTime': '2021-12-23T00:34:34.520725+00:00',
            'fromLegalName': '0870884 B.C. LTD.',
            'toLegalName': 'LM LOGISTICS INC.'
        }
    ],
    'offices': OFFICES,
    'parties': PARTIES,
    'registrarInfo': REGISTRAR_INFO,
    'reportDateTime': '2022-08-05T18:30:42.147556+00:00',
    'reportType': 'summary',
    'stateFilings': STATE_FILINGS
}
