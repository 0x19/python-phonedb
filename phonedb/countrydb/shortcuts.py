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

from phonedb.logger import logging
logging = logging.getLogger(__name__)

from phonedb.countrydb.exceptions import CountryParameterMissing
from phonedb.countrydb.utils import validate_country_code, validate_country_prefix


def discover_country(**kwargs):
    """Method used to intelligently discover country record based on provided parameters

    Method requires at least one of the following parameters to be passed along:

    :param country_code
    :param country_alpha_3
    :param country_prefix
    :
    """
    logging.debug('[discover_country] attempt to discover country against (kwargs: %s)', kwargs)

    if not len(kwargs):
        raise CountryParameterMissing(
            "At least one parameter needs to be passed along to in order be able discover country"
        )

    if kwargs.get('country_code') or kwargs.get('country_alpha_3'):
        country_code = validate_country_code(kwargs.get('country_code'), None)
        logging.debug('[discover_country] validated (country_code: %s)', country_code)

    if kwargs.get('country_prefix'):
        country_code = validate_country_code(kwargs.get('country_code'), None)
        logging.debug('[discover_country] validated (country_code: %s)', country_code)


    package_class_name = country_code.capitalize()
    package_path = __import__('phonedb.countrydb.countries', globals(), locals(), [package_class_name])

    return getattr(package_path, package_class_name)()

