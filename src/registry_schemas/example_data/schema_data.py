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

import copy


FILING_HEADER = {
    'filing': {
        'header': {
            'name': 'annualReport',
            'availableOnPaperOnly': False,
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
                        'addressCountry': 'mailing_address country',
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
                        'addressCountry': 'mailing_address country',
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
                'addressCountry': 'mailing_address country',
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
                'addressCountry': 'mailing_address country',
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
                'addressCountry': 'delivery_address country',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
                'actions': []
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'mailing_address country',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
                'actions': ['addressChanged']
            }
        }
    }
}

COMMENT_BUSINESS = {
    'comment': {
        'businessId': 1,
        'comment': 'This is a comment on a business.',
        'timestamp': '2020-02-10T20:05:49.068272+00:00',
        'submitterId': 1
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
                'addressCountry': 'delivery_address country',
                'postalCode': 'H0H0H0',
                'addressRegion': 'BC',
                'actions': []
            },
            'mailingAddress': {
                'streetAddress': 'mailing_address - address line one',
                'addressCity': 'mailing_address city',
                'addressCountry': 'mailing_address country',
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
                'addressCountry': 'mailing_address country',
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
                        'addressCountry': 'mailing_address country',
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
                        'addressCountry': 'mailing_address country',
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
                        'addressCountry': 'mailing_address country',
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
                        'addressCountry': 'mailing_address country',
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
                        'addressCountry': 'mailing_address country',
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
                        'addressCountry': 'mailing_address country',
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
                        'addressCountry': 'mailing_address country',
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
                        'addressCountry': 'mailing_address country',
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

VOLUNTARY_DISSOLUTION = {
    'dissolutionDate': '2018-04-08',
    'hasLiabilities': True
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
    ],
    'contactPoint': {
        'email': 'no_one@never.get',
        'phone': '123-456-7890'
    },
    'incorporationAgreement': {
        'agreementType': 'sample'
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
        'incorporationApplication': INCORPORATION
    }
}


STUB_FILING = {
}

# build complete list of filings with names, for use in the generic test_valid_filing() test
# - not including AR or correction because they are already complete filings rather than the others that are snippets
# without header and business elements; prepended to list afterwards.
FILINGS_WITH_TYPES = [
    ('changeOfDirectors', CHANGE_OF_DIRECTORS),
    ('changeOfAddress', CHANGE_OF_ADDRESS),
    ('voluntaryDissolution', VOLUNTARY_DISSOLUTION),
    ('specialResolution', SPECIAL_RESOLUTION),
    ('changeOfName', CHANGE_OF_NAME),
    ('incorporationApplication', STUB_FILING),
    ('amalgamationApplication', STUB_FILING),
    ('dissolved', STUB_FILING),
    ('amendedAGM', STUB_FILING),
    ('restorationApplication', STUB_FILING),
    ('amendedAnnualReport', STUB_FILING),
    ('amendedChangeOfDirectors', STUB_FILING),
    ('voluntaryLiquidation', STUB_FILING),
    ('appointReceiver', STUB_FILING),
    ('continuedOut', STUB_FILING),
    ('changeOfDirectors', CHANGE_OF_DIRECTORS_MAILING),  # bcorp-specific version of filing
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
