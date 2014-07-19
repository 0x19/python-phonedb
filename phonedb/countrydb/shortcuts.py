# -*- coding: UTF-8 -*-

from phonedb.about import __author__, __copyright__, __credits__, __license__, __version__, __maintainer__, \
    __email__, __status__

from phonedb.logger import logging
logging = logging.getLogger(__name__)

from phonedb.countrydb.exceptions import CountryParameterMissing


def discover_country(**kwargs):
    """Method used to intelligently discover country record based on provided parameters

    Method requires at least one of the following parameters to be passed along:

    :param country_code
    :param country_prefix
    :
    """
    logging.debug('[discover_country] attempt to discover country against (kwargs: %s)', kwargs)

    if not len(kwargs):
        raise CountryParameterMissing(
            "At least one parameter needs to be passed along to in order be able discover country"
        )

    if kwargs.get('country_prefix'):
        country_search_string = kwargs.get('country_prefix')

    if kwargs.get('country_code'):
        country_search_string = kwargs.get('country_code')

    logging.debug('[discover_country] attempting to discover country against (string: %s)', country_search_string)

    package_class_name = country_search_string.capitalize()
    package_path = __import__('phonedb.countrydb.countries', globals(), locals(), [package_class_name])

    try:
        return getattr(package_path, package_class_name)()
    except AttributeError as e:
        logging.error('[discover_country] unable to discover country against (class_reference: %s)' % package_class_name)
        return None