# Copyright © 2023 Province of British Columbia
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
"""Sample data for affiliated businesses."""
AFFILIATED_BUSINESSES = {
  'businessAffiliations': [
    {
      'adminFreeze': False,
      'goodStanding': False,
      'identifier': 'BC0693666',
      'legalName': 'GEER & SPICE INSURANCE AGENCIES LTD.',
      'legalType': 'BC',
      'state': 'ACTIVE',
      'taxId': '123456789BC0001'
    },
    {
      'adminFreeze': False,
      'goodStanding': True,
      'identifier': 'BC0702216',
      'legalName': 'M & D NEALIS CONTRACTING LTD.',
      'legalType': 'BC',
      'state': 'ACTIVE'
    },
    {
      'adminFreeze': False,
      'goodStanding': True,
      'identifier': 'BC0870788',
      'legalName': '0870788 B.C. LTD.',
      'legalType': 'BEN',
      'state': 'HISTORICAL'
    },
    {
      'adminFreeze': False,
      'goodStanding': True,
      'identifier': 'FM0272695',
      'legalName': 'MOBOCAF FOOD SERVICES',
      'legalType': 'SP',
      'state': 'ACTIVE'
    }
  ],
  'draftAffiliations': [
    {
      'identifier': 'TQEXcl60sA',
      'legalType': 'GP',
      'nrNumber': 'NR 5930775'
    },
    {
      'identifier': 'Tzgibt8rN4',
      'legalType': 'BEN'
    }
  ]
}
