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

from new import classobj
from phonedb.countrydb.data import get_country_data

#
COUNTRIES_LOADED = False


class CountryResourceMetaClass(type):

    def __new__(meta, *args, **kwargs):
        return type.__new__(meta, *args, **kwargs)


class CountryResource(object):

    __metaclass__ = CountryResourceMetaClass

    def __init__(self, *args, **kwargs):
        pass


class Us(object):
    pass

country_data = get_country_data()