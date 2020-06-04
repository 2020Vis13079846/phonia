#!/usr/bin/env python3

# MIT License
#
# Copyright (C) 2019-2020, Entynetproject. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from lib.output import *
from lib.format import *


def scan(InputNumber, print_results=True):
    test('Running local scan...')

    FormattedPhoneNumber = "+" + formatNumber(InputNumber)

    try:
        PhoneNumberObject = phonenumbers.parse(FormattedPhoneNumber, None)
    except Exception as e:
        throw(e)
    else:
        if not phonenumbers.is_valid_number(PhoneNumberObject):
            return False

        number = phonenumbers.format_number(
            PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace('+', '')
        numberCountryCode = phonenumbers.format_number(
            PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL).split(' ')[0]
        numberCountry = phonenumbers.region_code_for_country_code(
            int(numberCountryCode))

        localNumber = phonenumbers.format_number(
            PhoneNumberObject, phonenumbers.PhoneNumberFormat.E164).replace(numberCountryCode, '')
        internationalNumber = phonenumbers.format_number(
            PhoneNumberObject, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

        country = geocoder.country_name_for_number(PhoneNumberObject, "en")
        location = geocoder.description_for_number(PhoneNumberObject, "en")
        carrierName = carrier.name_for_number(PhoneNumberObject, 'en')

        if print_results:
            info('International format: {}'.format(internationalNumber))
            info('Local format: {}'.format(localNumber))
            info('Country found: {} ({})'.format(country, numberCountryCode))
            info('City/Area: {}'.format(location))
            info('Carrier: {}'.format(carrierName))
            for timezoneResult in timezone.time_zones_for_number(PhoneNumberObject):
                info('Timezone: {}'.format(timezoneResult))

            if phonenumbers.is_possible_number(PhoneNumberObject):
                plus('The number is valid and possible!')
            else:
                warn('The number is valid but might not be possible.')

    numberObj = {}
    numberObj['input'] = InputNumber
    numberObj['default'] = number
    numberObj['local'] = localNumber
    numberObj['international'] = internationalNumber
    numberObj['country'] = country
    numberObj['countryCode'] = numberCountryCode
    numberObj['countryIsoCode'] = numberCountry
    numberObj['location'] = location
    numberObj['carrier'] = carrierName

    return numberObj
