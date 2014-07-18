# -*- coding: UTF-8 -*-

from phonedb.about import __author__, __copyright__, __credits__, __license__, __version__, __maintainer__, \
    __email__, __status__


class CountryParameterMissing(Exception):
    """Exception that will be raised whenever country parameter is missing

    """
    pass


class InvalidCountryCode(Exception):
    """Exception that will be raised whenever country_code parameter is not valid

    """
    pass