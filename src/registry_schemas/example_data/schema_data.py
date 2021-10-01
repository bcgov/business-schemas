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
"""Sample data used across many tests."""
# pylint: disable=too-many-lines
import copy


FILING_HEADER = {
    'filing': {
        'header': {
            'name': 'annualReport',
            'availableOnPaperOnly': False,
            'inColinOnly': False,
            'date': '2019-04-08',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1,
            'routingSlipNumber': '123456789',
            'waiveFees': False,
            'priority': False
        },
        'business': {
            'cacheId': 1,
            'foundingDate': '2007-04-08T00:00:00+00:00',
            'identifier': 'CP1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'lastPreBobFilingTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'legalName': 'legal name - CP1234567',
            'legalType': 'CP'
        }
    }
}

BUSINESS = {
    'cacheId': 1,
    'foundingDate': '2007-04-08T00:00:00+00:00',
    'identifier': 'CP1234567',
    'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
    'lastPreBobFilingTimestamp': '2019-04-15T20:05:49.068272+00:00',
    'legalName': 'legal name - CP1234567',
    'legalType': 'CP'
}

ADDRESS = {
    'streetAddress': 'delivery_address - address line one',
    'streetAddressAdditional': 'line 2',
    'addressCity': 'delivery_address city',
    'addressCountry': 'delivery_address country',
    'postalCode': 'H0H0H0',
    'addressRegion': 'BC',
    'deliveryInstructions': 'some delivery instructions'
}

ANNUAL_REPORT = {
    'filing': {
        'header': {
            'name': 'annualReport',
            'availableOnPaperOnly': False,
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'date': '2019-04-08'
        },
        'business': {
            'cacheId': 1,
            'foundingDate': '2007-04-08T00:00:00+00:00',
            'identifier': 'CP1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'lastPreBobFilingTimestamp': '2019-01-01T20:05:49.068272+00:00',
            'legalName': 'legal name - CP1234567',
            'legalType': 'CP'
        },
        'annualReport': {
            'annualGeneralMeetingDate': '2018-04-08',
            'annualReportDate': '2018-04-08',
            'directors': [
                {
                    'officer': {
                        'firstName': 'Peter',
                        'lastName': 'Griffin',
                        'prevFirstName': 'Peter',
                        'prevMiddleInitial': 'G',
                        'prevLastName': 'Griffin'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'appointmentDate': '2018-01-01',
                    'cessationDate': None
                },
                {
                    'officer': {
                        'firstName': 'Joe',
                        'middleInitial': 'P',
                        'lastName': 'Swanson'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line #1',
                        'additionalStreetAddress': 'Kirkintiloch',
                        'addressCity': 'Glasgow',
                        'addressCountry': 'UK',
                        'postalCode': 'H0H 0H0',
                        'addressRegion': 'SC'
                    },
                    'title': 'Treasurer',
                    'cessationDate': None,
                    'appointmentDate': '2018-01-01'
                }
            ],
            'offices': {
                'registeredOffice': {
                    'deliveryAddress': {
                        'streetAddress': 'delivery_address - address line one',
                        'addressCity': 'delivery_address city',
                        'addressCountry': 'delivery_address country',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    }
                }
            }
        }
    }
}

CHANGE_OF_DIRECTORS = {
    'directors': [
        {
            'officer': {
                'firstName': 'Peter',
                'lastName': 'Griffin',
                'prevFirstName': 'Peter',
                'prevMiddleInitial': 'G',
                'prevLastName': 'Griffin'
            },
            'deliveryAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'Canada',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'appointmentDate': '2018-01-01',
            'cessationDate': '2019-04-03',
            'actions': ['addressChanged', 'nameChanged']
        },
        {
            'officer': {
                'firstName': 'Joe',
                'middleInitial': 'P',
                'lastName': 'Swanson'
            },
            'deliveryAddress': {
                'streetAddress': 'mailing_address - address line #1',
                'additionalStreetAddress': 'Kirkintiloch',
                'addressCity': 'Glasgow',
                'addressCountry': 'UK',
                'postalCode': 'H0H 0H0',
                'addressRegion': 'SC'
            },
            'title': 'Treasurer',
            'cessationDate': None,
            'appointmentDate': '2018-01-01',
            'actions': []
        }
    ]
}

CHANGE_OF_DIRECTORS_MAILING = {
    'directors': [
        {
            'officer': {
                'firstName': 'Peter',
                'lastName': 'Griffin',
                'prevFirstName': 'Peter',
                'prevMiddleInitial': 'G',
                'prevLastName': 'Griffin'
            },
            'deliveryAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'Canada',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line #2',
                'additionalStreetAddress': 'Kirkintiloch',
                'addressCity': 'Glasgow',
                'addressCountry': 'UK',
                'postalCode': 'H0H 0H0',
                'addressRegion': 'SC'
            },
            'appointmentDate': '2018-01-01',
            'cessationDate': '2019-04-03',
            'actions': ['addressChanged', 'nameChanged']
        },
        {
            'officer': {
                'firstName': 'Joe',
                'middleInitial': 'P',
                'lastName': 'Swanson'
            },
            'deliveryAddress': {
                'streetAddress': 'mailing_address - address line #1',
                'additionalStreetAddress': 'Kirkintiloch',
                'addressCity': 'Glasgow',
                'addressCountry': 'UK',
                'postalCode': 'H0H 0H0',
                'addressRegion': 'SC'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line #2',
                'additionalStreetAddress': 'Kirkintiloch',
                'addressCity': 'Glasgow',
                'addressCountry': 'UK',
                'postalCode': 'H0H 0H0',
                'addressRegion': 'SC'
            },
            'title': 'Treasurer',
            'cessationDate': None,
            'appointmentDate': '2018-01-01',
            'actions': []
        }
    ]
}

CHANGE_OF_ADDRESS = {
    'legalType': 'CP',
    'offices': {
        'registeredOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'Canada',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
                'actions': []
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'Canada',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
                'actions': ['addressChanged']
            }
        }
    }
}

CONTACT_POINT = {
    'email': 'no_one@never.get',
    'phone': '123-456-7890'
}

COMMENT_BUSINESS = {
    'comment': {
        'businessId': 'CP151151',
        'comment': 'This is a comment on a business.',
        'timestamp': '2020-02-10T20:05:49.068272+00:00'
    }
}

COMMENT_FILING = {
    'comment': {
        'comment': 'This is a comment on a filing.',
        'filingId': 1,
        'timestamp': '2020-02-10T20:05:49.068272+00:00',
        'submitterDisplayName': 'joefresh'
    }
}

CORP_CHANGE_OF_ADDRESS = {
    'legalType': 'BC',
    'offices': {
        'registeredOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'Canada',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
                'actions': []
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'Canada',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
                'actions': ['addressChanged']
            }
        },
        'recordsOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'delivery_address country',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
                'actions': []
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'Canada',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
                'actions': ['addressChanged']
            }
        }
    }
}

CORRECTION_AR = {
    'filing': {
        'header': {
            'name': 'correction',
            'availableOnPaperOnly': False,
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'date': '2020-02-18',
            'affectedFilings': [101, ],
            'waiveFees': True
        },
        'business': {
            'cacheId': 1,
            'foundingDate': '2007-04-08T00:00:00+00:00',
            'identifier': 'CP1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'lastPreBobFilingTimestamp': '2019-01-01T20:05:49.068272+00:00',
            'legalName': 'legal name - CP1234567',
            'legalType': 'CP'
        },
        'correction': {
            'correctedFilingId': 101,
            'correctedFilingType': 'annualReport',
            'correctedFilingDate': '2019-04-08',
            'comment': "User selected wrong agm date. ACTION ITEMS: change agm date to '2018-07-23'."
        },
        'annualReport': {
            'annualGeneralMeetingDate': '2018-07-23',
            'annualReportDate': '2018-07-23',
            'directors': [
                {
                    'officer': {
                        'firstName': 'Peter',
                        'lastName': 'Griffin',
                        'prevFirstName': 'Peter',
                        'prevMiddleInitial': 'G',
                        'prevLastName': 'Griffin'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'appointmentDate': '2018-01-01',
                    'cessationDate': None
                },
                {
                    'officer': {
                        'firstName': 'Joe',
                        'middleInitial': 'P',
                        'lastName': 'Swanson'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line #1',
                        'additionalStreetAddress': 'Kirkintiloch',
                        'addressCity': 'Glasgow',
                        'addressCountry': 'UK',
                        'postalCode': 'H0H 0H0',
                        'addressRegion': 'SC'
                    },
                    'title': 'Treasurer',
                    'cessationDate': None,
                    'appointmentDate': '2018-01-01'
                }
            ],
            'offices': {
                'registeredOffice': {
                    'deliveryAddress': {
                        'streetAddress': 'delivery_address - address line one',
                        'addressCity': 'delivery_address city',
                        'addressCountry': 'delivery_address country',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    }
                }
            }
        }
    }
}

CORRECTION_COA = {
    'filing': {
        'header': {
            'name': 'correction',
            'availableOnPaperOnly': False,
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'date': '2020-02-18',
            'routingSlipNumber': '123456789',
            'waiveFees': False,
            'priority': True
        },
        'business': {
            'cacheId': 1,
            'foundingDate': '2007-04-08T00:00:00+00:00',
            'identifier': 'CP1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'lastPreBobFilingTimestamp': '2019-01-01T20:05:49.068272+00:00',
            'legalName': 'legal name - CP1234567',
            'legalType': 'CP'
        },
        'correction': {
            'correctedFilingId': 1,
            'correctedFilingType': 'changeOfAddress',
            'correctedFilingDate': '2019-04-08',
            'comment': """
            Typo in delivery address line 1.
            ACTION ITEMS: change delivery address line 1 to 'corrected - address line one'
            """
        },
        'changeOfAddress': {
            'legalType': 'CP',
            'offices': {
                'registeredOffice': {
                    'deliveryAddress': {
                        'streetAddress': 'corrected - address line one',
                        'addressCity': 'delivery_address city',
                        'addressCountry': 'delivery_address country',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC',
                        'actions': ['addressChanged']
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC',
                        'actions': ['addressChanged']
                    }
                }
            }
        }
    }
}

CORRECTION_COD = {
    'filing': {
        'header': {
            'name': 'correction',
            'availableOnPaperOnly': False,
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'date': '2020-02-18',
            'routingSlipNumber': '123456789'
        },
        'business': {
            'cacheId': 1,
            'foundingDate': '2007-04-08T00:00:00+00:00',
            'identifier': 'CP1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'lastPreBobFilingTimestamp': '2019-01-01T20:05:49.068272+00:00',
            'legalName': 'legal name - CP1234567',
            'legalType': 'CP'
        },
        'correction': {
            'correctedFilingId': 2,
            'correctedFilingType': 'changeOfDirectors',
            'correctedFilingDate': '2019-04-08',
            'comment': "one director was missed. ACTION ITEMS: appoint 'New Missed Director'"
        },
        'changeOfDirectors': {
            'directors': [
                {
                    'officer': {
                        'firstName': 'Peter',
                        'lastName': 'Griffin',
                        'prevFirstName': 'Peter',
                        'prevMiddleInitial': 'G',
                        'prevLastName': 'Griffin'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line #2',
                        'additionalStreetAddress': 'Kirkintiloch',
                        'addressCity': 'Glasgow',
                        'addressCountry': 'UK',
                        'postalCode': 'H0H 0H0',
                        'addressRegion': 'SC'
                    },
                    'appointmentDate': '2018-01-01',
                    'cessationDate': '2019-04-03',
                    'actions': ['addressChanged', 'nameChanged']
                },
                {
                    'officer': {
                        'firstName': 'Joe',
                        'middleInitial': 'P',
                        'lastName': 'Swanson'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line #1',
                        'additionalStreetAddress': 'Kirkintiloch',
                        'addressCity': 'Glasgow',
                        'addressCountry': 'UK',
                        'postalCode': 'H0H 0H0',
                        'addressRegion': 'SC'
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line #2',
                        'additionalStreetAddress': 'Kirkintiloch',
                        'addressCity': 'Glasgow',
                        'addressCountry': 'UK',
                        'postalCode': 'H0H 0H0',
                        'addressRegion': 'SC'
                    },
                    'title': 'Treasurer',
                    'cessationDate': None,
                    'appointmentDate': '2018-01-01',
                    'actions': []
                },
                {
                    'officer': {
                        'firstName': 'New',
                        'middleInitial': 'Missed',
                        'lastName': 'Director'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line #1',
                        'additionalStreetAddress': 'Kirkintiloch',
                        'addressCity': 'Glasgow',
                        'addressCountry': 'UK',
                        'postalCode': 'H0H 0H0',
                        'addressRegion': 'SC'
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line #2',
                        'additionalStreetAddress': 'Kirkintiloch',
                        'addressCity': 'Glasgow',
                        'addressCountry': 'UK',
                        'postalCode': 'H0H 0H0',
                        'addressRegion': 'SC'
                    },
                    'cessationDate': None,
                    'appointmentDate': '2019-04-08',
                    'actions': ['appointed']
                }
            ]
        }
    }
}

CORRECTION_COMBINED_AR = {
    'filing': {
        'header': {
            'name': 'correction',
            'availableOnPaperOnly': False,
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'date': '2020-02-18',
            'routingSlipNumber': '123456789'
        },
        'business': {
            'cacheId': 1,
            'foundingDate': '2007-04-08T00:00:00+00:00',
            'identifier': 'CP1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'lastPreBobFilingTimestamp': '2019-01-01T20:05:49.068272+00:00',
            'legalName': 'legal name - CP1234567',
            'legalType': 'CP'
        },
        'correction': {
            'correctedFilingId': 4,
            'correctedFilingType': 'annualReport',
            'correctedFilingDate': '2019-04-08',
            'comment': """
            User selected wrong agm date, entered wrong name for a director, and typo in address line 1.
                ACTION ITEMS:
                    - change agm date to '2018-07-23'
                    - change director name 'Peter Griffin' to 'Corrected Griffin'
                    - change registered office delivery address line 1 to 'corrected - line 1
                    """
        },
        'annualReport': {
            'annualGeneralMeetingDate': '2018-07-23',
            'annualReportDate': '2018-07-23',
            'directors': [
                {
                    'officer': {
                        'firstName': 'Corrected',
                        'lastName': 'Griffin',
                        'middleInitial': '',
                        'prevFirstName': 'Peter',
                        'prevMiddleInitial': 'G',
                        'prevLastName': 'Griffin'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'appointmentDate': '2018-01-01',
                    'cessationDate': None
                },
                {
                    'officer': {
                        'firstName': 'Joe',
                        'middleInitial': 'P',
                        'lastName': 'Swanson'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line #1',
                        'additionalStreetAddress': 'Kirkintiloch',
                        'addressCity': 'Glasgow',
                        'addressCountry': 'UK',
                        'postalCode': 'H0H 0H0',
                        'addressRegion': 'SC'
                    },
                    'title': 'Treasurer',
                    'cessationDate': None,
                    'appointmentDate': '2018-01-01'
                }
            ],
            'offices': {
                'registeredOffice': {
                    'deliveryAddress': {
                        'streetAddress': 'corrected - line 1',
                        'addressCity': 'delivery_address city',
                        'addressCountry': 'delivery_address country',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    }
                }
            }
        },
        'changeOfAddress': {
            'legalType': 'CP',
            'offices': {
                'registeredOffice': {
                    'deliveryAddress': {
                        'streetAddress': 'corrected - line 1',
                        'addressCity': 'delivery_address city',
                        'addressCountry': 'delivery_address country',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC',
                        'actions': ['addressChanged']
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    }
                }
            }
        },
        'changeOfDirectors': {
            'directors': [
                {
                    'officer': {
                        'firstName': 'Corrected',
                        'lastName': 'Griffin',
                        'middleInitial': '',
                        'prevFirstName': 'Peter',
                        'prevMiddleInitial': 'G',
                        'prevLastName': 'Griffin'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'Canada',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'appointmentDate': '2018-01-01',
                    'cessationDate': None,
                    'actions': ['nameChanged']
                },
                {
                    'officer': {
                        'firstName': 'Joe',
                        'middleInitial': 'P',
                        'lastName': 'Swanson'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'mailing_address - address line #1',
                        'additionalStreetAddress': 'Kirkintiloch',
                        'addressCity': 'Glasgow',
                        'addressCountry': 'UK',
                        'postalCode': 'H0H 0H0',
                        'addressRegion': 'SC'
                    },
                    'title': 'Treasurer',
                    'cessationDate': None,
                    'appointmentDate': '2018-01-01',
                    'actions': []
                }
            ]
        }
    }
}

DISSOLUTION = {
    'dissolutionDate': '2018-04-08',
    'dissolutionType': 'voluntary',
    'dissolutionStatementType': '197NoAssetsNoLiabilities',
    'hasLiabilities': False,
    'parties': [
        {
            'officer': {
                'firstName': '',
                'lastName': '',
                'middleName': '',
                'orgName': 'Xyz Inc.',
                'partyType': 'org'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'roles': [
                {
                    'roleType': 'Custodian',
                    'appointmentDate': '2021-08-05'
                }
            ]
        }
    ],
    'custodialOffice': {
        'deliveryAddress': {
            'streetAddress': 'records - delivery_address',
            'addressCity': 'delivery_address city',
            'addressCountry': 'CA',
            'postalCode': 'H0H0H0',
            'addressRegion': 'BC'
        },
        'mailingAddress': {
            'streetAddress': 'records - mailing_address',
            'addressCity': 'mailing_address city',
            'addressCountry': 'CA',
            'postalCode': 'H0H0H0',
            'addressRegion': 'BC',
        }
    }
}

SPECIAL_RESOLUTION = {
    'resolution': 'Be in resolved that cookies are delicious.\n\nNom nom nom...'
}

CHANGE_OF_NAME = {
    'legalName': 'My New Entity Name'
}

INCORPORATION = {
    'nameRequest': {
        'legalType': 'BC'
    },
    'nameTranslations': [
        {'name': 'ABC Ltd.'},
        {'name': 'Financière de l’Odet'},
        {'name': 'Société Générale'}
    ],
    'offices': {
        'registeredOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
            }
        },
        'recordsOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
            }
        }
    },
    'parties': [
        {
            'officer': {
                'id': 1,
                'firstName': 'Joe',
                'lastName': 'Swanson',
                'middleName': 'P',
                'email': 'joe@email.com',
                'orgName': '',
                'partyType': 'person'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'roles': [
                {
                    'roleType': 'Completing Party',
                    'appointmentDate': '2018-01-01'

                },
                {
                    'roleType': 'Director',
                    'appointmentDate': '2018-01-01'

                }
            ]
        },
        {
            'officer': {
                'id': 2,
                'firstName': '',
                'lastName': '',
                'middleName': '',
                'orgName': 'Xyz Inc.',
                'partyType': 'org'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'roles': [
                {
                    'roleType': 'Incorporator',
                    'appointmentDate': '2018-01-01'
                }
            ]
        }
    ],
    'shareStructure': {
        'shareClasses': [
            {
                'id': 1,
                'name': 'Share Class 1',
                'priority': 1,
                'hasMaximumShares': True,
                'maxNumberOfShares': 100,
                'hasParValue': True,
                'parValue': 10,
                'currency': 'CAD',
                'hasRightsOrRestrictions': False,
                'series': [
                    {
                        'id': 1,
                        'name': 'Share Series 1',
                        'priority': 1,
                        'hasMaximumShares': True,
                        'maxNumberOfShares': 50,
                        'hasRightsOrRestrictions': False,
                    },
                    {
                        'id': 2,
                        'name': 'Share Series 2',
                        'priority': 2,
                        'hasMaximumShares': True,
                        'maxNumberOfShares': 100,
                        'hasRightsOrRestrictions': False,
                    }
                ]
            },
            {
                'id': 2,
                'name': 'Share Class 2',
                'priority': 1,
                'hasMaximumShares': False,
                'maxNumberOfShares': None,
                'hasParValue': False,
                'parValue': None,
                'currency': None,
                'hasRightsOrRestrictions': True,
                'series': []
            },
        ]
    },
    'contactPoint': {
        'email': 'no_one@never.get',
        'phone': '123-456-7890'
    },
    'incorporationAgreement': {
        'agreementType': 'sample'
    }
}

COOP_INCORPORATION = {
    'nameRequest': {
        'legalType': 'CP'
    },
    'nameTranslations': [
        {'name': 'ABC Ltd.'},
        {'name': 'Financière de l’Odet'},
        {'name': 'Société Générale'}
    ],
    'offices': {
        'registeredOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
            }
        }
    },
    'parties': [
        {
            'officer': {
                'id': 1,
                'firstName': 'Joe',
                'lastName': 'Swanson',
                'middleName': 'P',
                'email': 'joe@email.com',
                'orgName': '',
                'partyType': 'person'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'roles': [
                {
                    'roleType': 'Completing Party',
                    'appointmentDate': '2018-01-01'

                },
                {
                    'roleType': 'Director',
                    'appointmentDate': '2018-01-01'

                }
            ]
        }
    ],
    'contactPoint': {
        'email': 'no_one@never.get',
        'phone': '123-456-7890'
    },
    'cooperative': {
        'cooperativeAssociationType': 'CP',
        'rulesFileKey': 'cooperative/fa00c6bf-eaad-4a07-a3d2-4786ecd6b83b.jpg',
        'rulesFileName': 'rule_file.jpg',
        'memorandumFileKey': 'cooperative/f722bf16-86be-430d-928d-5529853a3a2c.pdf',
        'memorandumFileName': 'memorandum_file.pdf'
    }
}

CORRECTION_INCORPORATION = {
    'filing': {
        'header': {
            'name': 'correction',
            'availableOnPaperOnly': False,
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'date': '2020-02-18',
            'routingSlipNumber': '123456789'
        },
        'business': {
            'cacheId': 1,
            'foundingDate': '2007-04-08T00:00:00+00:00',
            'identifier': 'BC1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'lastPreBobFilingTimestamp': '2019-01-01T20:05:49.068272+00:00',
            'legalName': 'legal name - BC1234567',
            'legalType': 'BC'
        },
        'correction': {
            'correctedFilingId': 4,
            'correctedFilingType': 'incorporationApplication',
            'correctedFilingDate': '2019-04-08',
            'comment': """Sample Comment""",
            # diff is not expected to be the part of correction input. This will be populated by the API by comparing
            # correction json with the original filing.
            'diff': [
                {
                    # Example of a deleted record
                    'oldValue': {
                        'officer': {
                            'id': 2,
                            'firstName': '',
                            'lastName': '',
                            'middleName': '',
                            'orgName': 'Xyz Inc.',
                            'partyType': 'org'
                        },
                        'mailingAddress': {
                            'streetAddress': 'mailing_address - address line one',
                            'streetAddressAdditional': '',
                            'addressCity': 'mailing_address city',
                            'addressCountry': 'CA',
                            'postalCode': 'H0H0H0',
                            'addressRegion': 'BC'
                        },
                        'roles': [
                            {
                                'roleType': 'Incorporator',
                                'appointmentDate': '2018-01-01'
                            }
                        ]
                    },
                    'newValue': None,
                    'path': '/filing/incorporationApplication/parties/2'
                },
                {
                    # Example of a changed value
                    'oldValue': 'sample',
                    'newValue': 'custom',
                    'path': '/filing/incorporationApplication/incorporationAgreement/agreementType'
                }
            ]
        },
        'incorporationApplication': {
            'nameRequest': {
                'legalType': 'BC',
                'legalName': 'legal name change - BC1234567'
            },
            'nameTranslations': [
                {'id': '1', 'name': 'ABCD Ltd.'},  # Modified translation
                {'name': 'Financière de l’Odet'}  # New translation
            ],
            'offices': {
                'registeredOffice': {
                    'deliveryAddress': {
                        'streetAddress': 'delivery_address - address line one',
                        'addressCity': 'delivery_address city',
                        'addressCountry': 'CA',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'CA',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC',
                    }
                },
                'recordsOffice': {
                    'deliveryAddress': {
                        'streetAddress': 'delivery_address - address line one',
                        'addressCity': 'delivery_address city',
                        'addressCountry': 'CA',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'CA',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC',
                    }
                }
            },
            'parties': [
                {
                    'officer': {
                        'id': 1,
                        'firstName': 'Joe',
                        'lastName': 'Swanson',
                        'middleName': 'P',
                        'email': 'joe@email.com',
                        'orgName': '',
                        'partyType': 'person'
                    },
                    'mailingAddress': {
                        'streetAddress': 'mailing_address - address line one',
                        'streetAddressAdditional': '',
                        'addressCity': 'mailing_address city',
                        'addressCountry': 'CA',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'deliveryAddress': {
                        'streetAddress': 'delivery_address - address line one',
                        'streetAddressAdditional': '',
                        'addressCity': 'delivery_address city',
                        'addressCountry': 'CA',
                        'postalCode': 'H0H0H0',
                        'addressRegion': 'BC'
                    },
                    'roles': [
                        {
                            'roleType': 'Completing Party',
                            'appointmentDate': '2018-01-01'

                        },
                        {
                            'roleType': 'Director',
                            'appointmentDate': '2018-01-01'

                        }
                    ]
                }
            ],
            'shareStructure': {
                'shareClasses': [
                    {
                        'id': 1,
                        'name': 'Share Class 1',
                        'priority': 1,
                        'hasMaximumShares': True,
                        'maxNumberOfShares': 100,
                        'hasParValue': True,
                        'parValue': 10,
                        'currency': 'CAD',
                        'hasRightsOrRestrictions': False,
                        'series': [
                            {
                                'id': 1,
                                'name': 'Share Series 1',
                                'priority': 1,
                                'hasMaximumShares': True,
                                'maxNumberOfShares': 50,
                                'hasRightsOrRestrictions': False,
                            },
                            {
                                'id': 2,
                                'name': 'Share Series 2',
                                'priority': 2,
                                'hasMaximumShares': True,
                                'maxNumberOfShares': 100,
                                'hasRightsOrRestrictions': False,
                            }
                        ]
                    },
                    {
                        'id': 2,
                        'name': 'Share Class 2',
                        'priority': 1,
                        'hasMaximumShares': False,
                        'maxNumberOfShares': None,
                        'hasParValue': False,
                        'parValue': None,
                        'currency': None,
                        'hasRightsOrRestrictions': True,
                        'series': []
                    },
                ]
            },
            'incorporationAgreement': {
                'agreementType': 'custom'
            }
        }
    }
}

COURT_ORDER = {
    'fileNumber': '#1234-5678/90',
    'orderDate': '2021-01-30T09:56:01+08:00',
    'effectOfOrder': 'planOfArrangement',
    'orderDetails': 'A note about order'
}

REGISTRARS_NOTATION = {
    'fileNumber': '#1234-5678/90',
    'orderDate': '2021-01-30T09:56:01+08:00',
    'effectOfOrder': 'planOfArrangement',
    'orderDetails': 'A note about order'
}

REGISTRARS_ORDER = {
    'fileNumber': '#1234-5678/90',
    'orderDate': '2021-01-30T09:56:01+08:00',
    'effectOfOrder': 'planOfArrangement',
    'orderDetails': 'A note about order'
}

RESTORATION = {
    'date': '2021-01-30',
    'type': 'fullRestoration'
}

ALTERATION = {
    'provisionsRemoved': False,
    'business': {
        'identifier': 'BC1234567',
        'legalType': 'BEN'
    },
    'nameRequest': {
        'nrNumber': 'NR 8798956',
        'legalName': 'HAULER MEDIA INC.',
        'legalType': 'BC'
    },
    'nameTranslations': [
        {'id': '1', 'name': 'ABCD Ltd.'},  # Modified translation
        {'name': 'Financière de l’Odet'}  # New translation
    ],
    'shareStructure': {
        'resolutionDates': ['2020-05-23', '2020-06-01'],
        'shareClasses': [{
            'name': 'class1',
            'priority': 1,
            'maxNumberOfShares': 600,
            'parValue': 1,
            'currency': 'CAD',
            'hasMaximumShares': True,
            'hasParValue': True,
            'hasRightsOrRestrictions': False,
            'series': [{
                'name': 'series1',
                'priority': 1,
                'maxNumberOfShares': 600,
                'hasMaximumShares': True,
                'hasRightsOrRestrictions': False
            }]
        }]
    },
    'contactPoint': {
        'email': 'no_one@never.get'
    },
    'courtOrder': COURT_ORDER
}

CONVERSION = {
    'nameRequest': {
        'legalType': 'BC'
    },
    'offices': {
        'registeredOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
            }
        },
        'recordsOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
            }
        }
    },
    'parties': [
        {
            'officer': {
                'id': 1,
                'firstName': 'Joe',
                'lastName': 'Swanson',
                'middleName': 'P',
                'email': 'joe@email.com',
                'orgName': '',
                'partyType': 'person'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'roles': [
                {
                    'roleType': 'Completing Party',
                    'appointmentDate': '2018-01-01'

                },
                {
                    'roleType': 'Director',
                    'appointmentDate': '2018-01-01'

                }
            ]
        },
        {
            'officer': {
                'id': 2,
                'firstName': '',
                'lastName': '',
                'middleName': '',
                'orgName': 'Xyz Inc.',
                'partyType': 'org'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'roles': [
                {
                    'roleType': 'Incorporator',
                    'appointmentDate': '2018-01-01'
                }
            ]
        }
    ],
    'shareStructure': {
        'shareClasses': [
            {
                'id': 1,
                'name': 'Share Class 1',
                'priority': 1,
                'hasMaximumShares': True,
                'maxNumberOfShares': 100,
                'hasParValue': True,
                'parValue': 10,
                'currency': 'CAD',
                'hasRightsOrRestrictions': False,
                'series': [
                    {
                        'id': 1,
                        'name': 'Share Series 1',
                        'priority': 1,
                        'hasMaximumShares': True,
                        'maxNumberOfShares': 50,
                        'hasRightsOrRestrictions': False,
                    },
                    {
                        'id': 2,
                        'name': 'Share Series 2',
                        'priority': 2,
                        'hasMaximumShares': True,
                        'maxNumberOfShares': 100,
                        'hasRightsOrRestrictions': False,
                    }
                ]
            },
            {
                'id': 2,
                'name': 'Share Class 2',
                'priority': 1,
                'hasMaximumShares': False,
                'maxNumberOfShares': None,
                'hasParValue': False,
                'parValue': None,
                'currency': None,
                'hasRightsOrRestrictions': True,
                'series': []
            },
        ]
    },
    'contactPoint': {
        'email': 'no_one@never.get',
        'phone': '123-456-7890'
    },
    'incorporationAgreement': {
        'agreementType': 'sample'
    }
}

TRANSITION = {
    'nameTranslations': [
        {'name': 'ABC Ltd.'},
        {'name': 'Financière de l’Odet'},
        {'name': 'Société Générale'}
    ],
    'hasProvisions': False,
    'offices': {
        'registeredOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
            }
        },
        'recordsOffice': {
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
            }
        }
    },
    'parties': [
        {
            'officer': {
                'id': 1,
                'firstName': 'Joe',
                'lastName': 'Swanson',
                'middleName': 'P',
                'email': 'joe@email.com',
                'orgName': '',
                'partyType': 'person'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'deliveryAddress': {
                'streetAddress': 'delivery_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'delivery_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'roles': [
                {
                    'roleType': 'Director',
                    'appointmentDate': '2018-01-01'

                }
            ]
        },
        {
            'officer': {
                'id': 2,
                'firstName': '',
                'lastName': '',
                'middleName': '',
                'orgName': 'Xyz Inc.',
                'partyType': 'org'
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'streetAddressAdditional': '',
                'addressCity': 'mailing_address city',
                'addressCountry': 'CA',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC'
            },
            'roles': [
                {
                    'roleType': 'Director',
                    'appointmentDate': '2018-01-01'
                }
            ]
        }
    ],
    'shareStructure': {
        'resolutionDates': ['2020-05-23', '2020-06-01'],
        'shareClasses': [
            {
                'id': 1,
                'name': 'Share Class 1',
                'priority': 1,
                'hasMaximumShares': True,
                'maxNumberOfShares': 100,
                'hasParValue': True,
                'parValue': 10,
                'currency': 'CAD',
                'hasRightsOrRestrictions': False,
                'series': [
                    {
                        'id': 1,
                        'name': 'Share Series 1',
                        'priority': 1,
                        'hasMaximumShares': True,
                        'maxNumberOfShares': 50,
                        'hasRightsOrRestrictions': False,
                    },
                    {
                        'id': 2,
                        'name': 'Share Series 2',
                        'priority': 2,
                        'hasMaximumShares': True,
                        'maxNumberOfShares': 100,
                        'hasRightsOrRestrictions': False,
                    }
                ]
            },
            {
                'id': 2,
                'name': 'Share Class 2',
                'priority': 1,
                'hasMaximumShares': False,
                'maxNumberOfShares': None,
                'hasParValue': False,
                'parValue': None,
                'currency': None,
                'hasRightsOrRestrictions': True,
                'series': []
            },
        ]
    },
    'contactPoint': {
        'email': 'no_one@never.get',
        'phone': '123-456-7890'
    }
}

FILING_TEMPLATE = {
    'filing': {
        'header': {
            'name': None,
            'date': '2019-04-08',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1,
            'effectiveDate': '2019-04-15T00:00:00+00:00'
        },
        'business': {
            'cacheId': 1,
            'foundingDate': '2007-04-08T00:00:00+00:00',
            'identifier': 'CP1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'lastPreBobFilingTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'legalName': 'legal name - CP1234567',
            'legalType': 'CP'
        }
    }
}

INCORPORATION_FILING_TEMPLATE = {
    'filing': {
        'header': {
            'name': 'incorporationApplication',
            'date': '2019-04-08',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1,
            'effectiveDate': '2019-04-15T00:00:00+00:00'
        },
        'business': {
            'identifier': 'T1234567',
            'legalType': 'BC'
        },
        'incorporationApplication': INCORPORATION
    }
}

COOP_INCORPORATION_FILING_TEMPLATE = {
    'filing': {
        'header': {
            'name': 'incorporationApplication',
            'date': '2019-04-08',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1,
            'effectiveDate': '2019-04-15T00:00:00+00:00'
        },
        'business': {
            'identifier': 'T1234567',
            'legalType': 'CP'
        },
        'incorporationApplication': COOP_INCORPORATION
    }
}

ALTERATION_FILING_TEMPLATE = {
    'filing': {
        'header': {
            'name': 'alteration',
            'date': '2020-06-25',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1
        },
        'business': {
            'foundingDate': '2018-01-01T00:00:00+00:00',
            'identifier': 'U1234567',
            'legalName': 'legal name - Test',
            'legalType': 'BC'
        },
        'alteration': ALTERATION
    }
}

CONVERSION_FILING_TEMPLATE = {
    'filing': {
        'header': {
            'name': 'conversion',
            'date': '2020-06-25',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1
        },
        'business': {
            'foundingDate': '2018-01-01T00:00:00+00:00',
            'identifier': 'BC1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'legalName': 'legal name - BC1234567',
            'legalType': 'BC'
        },
        'conversion': CONVERSION
    }
}

TRANSITION_FILING_TEMPLATE = {
    'filing': {
        'header': {
            'name': 'transition',
            'date': '2020-10-19',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1,
            'paymentAccount': '746'
        },
        'business': {
            'foundingDate': '2018-01-01T00:00:00+00:00',
            'identifier': 'BC1234567',
            'lastLedgerTimestamp': '2019-04-15T20:05:49.068272+00:00',
            'legalName': 'legal name - BC1234567',
            'legalType': 'BC'
        },
        'transition': TRANSITION
    }
}

REGISTRARS_NOTATION_FILING_TEMPLATE = {
    'filing': {
        'header': {
            'name': 'registrarsNotation',
            'date': '2021-05-06',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1
        },
        'business': {
            'foundingDate': '2018-01-01T00:00:00+00:00',
            'identifier': 'U1234567',
            'legalName': 'legal name - Test',
            'legalType': 'BC'
        },
        'registrarsNotation': REGISTRARS_NOTATION
    }
}

REGISTRARS_ORDER_FILING_TEMPLATE = {
    'filing': {
        'header': {
            'name': 'registrarsOrder',
            'date': '2021-05-06',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1
        },
        'business': {
            'foundingDate': '2018-01-01T00:00:00+00:00',
            'identifier': 'U1234567',
            'legalName': 'legal name - Test',
            'legalType': 'BC'
        },
        'registrarsOrder': REGISTRARS_ORDER
    }
}

COURT_ORDER_FILING_TEMPLATE = {
    'filing': {
        'header': {
            'name': 'courtOrder',
            'date': '2021-05-06',
            'certifiedBy': 'full name',
            'email': 'no_one@never.get',
            'filingId': 1
        },
        'business': {
            'foundingDate': '2018-01-01T00:00:00+00:00',
            'identifier': 'U1234567',
            'legalName': 'legal name - Test',
            'legalType': 'BC'
        },
        'courtOrder': COURT_ORDER
    }
}

STUB_FILING = {
}

UNMANAGED = {
    'displayName': 'Some legacy filing.'
}

# build complete list of filings with names, for use in the generic test_valid_filing() test
# - not including AR or correction because they are already complete filings rather than the others that are snippets
# without header and business elements; prepended to list afterwards.
FILINGS_WITH_TYPES = [
    ('changeOfDirectors', CHANGE_OF_DIRECTORS),
    ('changeOfAddress', CHANGE_OF_ADDRESS),
    ('dissolution', DISSOLUTION),
    ('specialResolution', SPECIAL_RESOLUTION),
    ('changeOfName', CHANGE_OF_NAME),
    ('incorporationApplication', STUB_FILING),
    ('amalgamationApplication', STUB_FILING),
    ('dissolved', STUB_FILING),
    ('amendedAGM', STUB_FILING),
    ('restoration', RESTORATION),
    ('amendedAnnualReport', STUB_FILING),
    ('amendedChangeOfDirectors', STUB_FILING),
    ('appointReceiver', STUB_FILING),
    ('continuedOut', STUB_FILING),
    ('changeOfDirectors', CHANGE_OF_DIRECTORS_MAILING),  # bcorp-specific version of filing
    ('alteration', ALTERATION),
    ('conversion', CONVERSION),
    ('transition', TRANSITION),
    ('courtOrder', COURT_ORDER),
    ('registrarsNotation', REGISTRARS_NOTATION),
    ('registrarsOrder', REGISTRARS_ORDER)
]


def _build_complete_filing(name, snippet):
    """Util function to build complete filing from filing template and snippet."""
    complete_dict = copy.deepcopy(FILING_TEMPLATE)
    complete_dict['filing']['header']['name'] = name
    complete_dict['filing'][name] = snippet
    return complete_dict


ALL_FILINGS = [_build_complete_filing(f[0], f[1]) for f in FILINGS_WITH_TYPES]
ALL_FILINGS.insert(0, ANNUAL_REPORT)
ALL_FILINGS.insert(0, CORRECTION_COA)
ALL_FILINGS.insert(0, CORRECTION_INCORPORATION)
