# -*- coding: UTF-8 -*-

from phonedb.about import __author__, __copyright__, __credits__, __license__, __version__, __maintainer__, \
    __email__, __status__

from phonedb.countrydb.exceptions import InvalidCountryCode
from phonedb.countrydb.countrycodes import CountryCodes


def validate_country_code(country_code, default_return_value=None):
    """

    """

    country_code = str(country_code)

    if not country_code or len(country_code) not in (2, 3):
        raise InvalidCountryCode(
            "We could not validate country code due to invalid parameter. (passed_parameter: %s)" % country_code
        )

    if not CountryCodes.is_valid(country_code):
        raise InvalidCountryCode(
            "Invalid or unsupported country code provided (provided_country_code: %s)" % country_code
        )

    return CountryCodes.get_code(country_code, default_return_value)



def validate_country_prefix():
    pass