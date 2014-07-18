# -*- coding: UTF-8 -*-

from phonedb import PACKAGE_VERSION, PACKAGE_STATUS, PACKAGE_AUTHOR, PACKAGE_COPYRIGHT, PACKAGE_CREDITS, PACKAGE_LICENSE
from phonedb import PACKAGE_MAINTAINER, PACKAGE_MAINTAINER_EMAIL

__author__ = PACKAGE_AUTHOR
__copyright__ = PACKAGE_COPYRIGHT
__credits__ = PACKAGE_CREDITS
__license__ = PACKAGE_LICENSE
__version__ = PACKAGE_VERSION
__maintainer__ = PACKAGE_MAINTAINER
__email__ = PACKAGE_MAINTAINER_EMAIL
__status__ = PACKAGE_STATUS

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