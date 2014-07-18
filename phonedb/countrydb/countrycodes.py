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

from phonedb.decorators import memoize


class CountryCodes(object):
    """

    """

    US = 'US'
    CA = 'CA'
    HR = 'HR'

    # ISO ALPHA-3 codes. We are calling it extended because I don't like digits in var names
    extended_country_code = {
        US: 'USA',
        CA: 'CAN',
        HR: 'HRK'
    }

    @classmethod
    def keys(cls):
        """

        """
        return cls.extended_country_code.keys()

    @classmethod
    def extended_keys(cls):
        """

        """
        return cls.extended_country_code.values()

    @classmethod
    @memoize
    def extended_to_short(cls, provided_extended_iso):
        """

        """
        for short_iso, extended_iso in cls.extended_country_code.items():
            if extended_iso == provided_extended_iso.upper():
                return short_iso

        return None


    @classmethod
    @memoize
    def is_valid(cls, country_code):
        """Check whenever ALPHA-2 or ALPHA-3 country code is valid and available

        :param country_code string

        :returns string|none
        """

        if not country_code or len(country_code) not in (2, 3):
            return None

        if len(country_code) == 2:
            return country_code.upper() in cls.keys()

        if len(country_code) == 3:
            return country_code.upper() in cls.extended_keys()

        return None


    @classmethod
    @memoize
    def get_code(cls, country_code, default_value=None):
        """Check whenever ALPHA-2 or ALPHA-3 country code is valid and available translate/return back ALPHA-2

        :param country_code string

        :returns string|none
        """

        if not cls.is_valid(country_code):
            return default_value

        if len(country_code) == 2:
            return country_code.upper()

        if len(country_code) == 3:
            return cls.extended_to_short(country_code)

        return default_value