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
"""Common schema segments for Business Documents."""

BUSINESS = {
    'adminFreeze': False,
    'arMaxDate': '2022-08-05',
    'arMinDate': '2022-12-15',
    'associationType': None,
    'complianceWarnings': [],
    'coopType': 'Not Available',
    'epochFilingDate': '2021-12-16T20:03:33.857887+00:00',
    'fiscalYearEndDate': '2021-12-15',
    'foundingDate': '2021-12-15T19:54:10.809174+00:00',
    'goodStanding': False,
    'hasCorrections': False,
    'hasRestrictions': False,
    'identifier': 'BC0870884',
    'lastAddressChangeDate': '2021-12-15',
    'lastAnnualGeneralMeetingDate': '',
    'lastAnnualReportDate': '',
    'lastDirectorChangeDate': '2021-12-15',
    'lastLedgerTimestamp': '2021-12-15T19:54:33.898570+00:00',
    'lastModified': '2021-12-15T19:54:33.898532+00:00',
    'legalName': '0870884 B.C. LTD.',
    'legalType': 'BEN',
    'naicsCode': None,
    'naicsDescription': None,
    'naicsKey': None,
    'nextAnnualReport': '2022-12-15T08:00:00+00:00',
    'state': 'HISTORICAL',
    'stateFiling': 'https://LEGAL_API_BASE_URL/api/v1/businesses/BC0870884/filings/113730',
    'warnings': []
}

OFFICES = {
    'custodialOffice': {
        'deliveryAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'CA',
            'addressRegion': 'BC',
            'addressType': 'delivery',
            'deliveryInstructions': '',
            'id': 2334725,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        },
        'mailingAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'CA',
            'addressRegion': 'BC',
            'addressType': 'mailing',
            'deliveryInstructions': '',
            'id': 2334724,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        }
    },
    'recordsOffice': {
        'deliveryAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'addressType': 'delivery',
            'deliveryInstructions': '',
            'id': 2317157,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        },
        'mailingAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'addressType': 'mailing',
            'deliveryInstructions': '',
            'id': 2317156,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        }
    },
    'registeredOffice': {
        'deliveryAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'addressType': 'delivery',
            'deliveryInstructions': '',
            'id': 2317159,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        },
        'mailingAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'addressType': 'mailing',
            'deliveryInstructions': '',
            'id': 2317158,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        }
    }
}

OFFICES_BUS = {
    'businessOffice': {
        'deliveryAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'CA',
            'addressRegion': 'BC',
            'addressType': 'delivery',
            'deliveryInstructions': '',
            'id': 2334725,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        },
        'mailingAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'CA',
            'addressRegion': 'BC',
            'addressType': 'mailing',
            'deliveryInstructions': '',
            'id': 2334724,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        }
    }
}

PARTIES = [
    {
        'deliveryAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'deliveryInstructions': '',
            'id': 2334722,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        },
        'mailingAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'deliveryInstructions': '',
            'id': 2334723,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3950 Helen Rd',
            'streetAddressAdditional': ''
        },
        'officer': {
            'firstName': 'LEKSHMI',
            'id': 474411,
            'lastName': 'MALLIKA',
            'partyType': 'person'
        },
        'roles': [
            {
                'appointmentDate': '2022-01-11',
                'cessationDate': None,
                'roleType': 'Custodian'
            }
        ]
    },
    {
        'deliveryAddress': {
            'addressCity': 'AB1',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'deliveryInstructions': None,
            'id': 2317160,
            'postalCode': 'V8X 5J8',
            'streetAddress': '#400A - 4000 SEYMOUR PLACE',
            'streetAddressAdditional': 'PENTHOUSE'
        },
        'mailingAddress': {
            'addressCity': 'AB1',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'deliveryInstructions': None,
            'id': 2317161,
            'postalCode': 'V8X 5J8',
            'streetAddress': '#400A - 4000 SEYMOUR PLACE',
            'streetAddressAdditional': 'PENTHOUSE'
        },
        'officer': {
            'firstName': 'BCREGTEST DALIA',
            'id': 468575,
            'lastName': 'ONE',
            'partyType': 'person'
        },
        'roles': [
            {
                'appointmentDate': '2021-12-15',
                'cessationDate': None,
                'roleType': 'Completing Party'
            },
            {
                'appointmentDate': '2021-12-15',
                'cessationDate': None,
                'roleType': 'Incorporator'
            },
            {
                'appointmentDate': '2021-12-15',
                'cessationDate': None,
                'roleType': 'Director'
            }
        ]
    },
    {
        'deliveryAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'deliveryInstructions': None,
            'id': 2317162,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3948 Helen Rd',
            'streetAddressAdditional': ''
        },
        'mailingAddress': {
            'addressCity': 'Victoria',
            'addressCountry': 'Canada',
            'addressCountryDescription': 'Canada',
            'addressRegion': 'BC',
            'deliveryInstructions': None,
            'id': 2317163,
            'postalCode': 'V8Z 5C5',
            'streetAddress': '3948 Helen Rd',
            'streetAddressAdditional': ''
        },
        'officer': {
            'firstName': 'LEKSHMI',
            'id': 468576,
            'lastName': 'GOKUL',
            'partyType': 'person'
        },
        'roles': [
            {
                'appointmentDate': '2021-12-15',
                'cessationDate': None,
                'roleType': 'Director'
            }
        ]
    }
]

REGISTRAR_INFO = {
    'endDate': None,
    'name': 'T.K. SPARKS',
    'startDate': '2022-06-01T00:00:00',
    'title': 'Registrar of Companies'
}

STATE_FILINGS = [
    {
        'effectiveDateTime': '2022-01-11T20:03:51.343818+00:00',
        'filingDateTime': '2022-01-11T20:03:33.857807+00:00',
        'filingName': 'Voluntary Dissolution'
    }
]
