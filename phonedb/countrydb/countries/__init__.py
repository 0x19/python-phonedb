# -*- coding: UTF-8 -*-

from phonedb.about import __author__, __copyright__, __credits__, __license__, __version__, __maintainer__, \
    __email__, __status__

from phonedb.logger import logging
logging = logging.getLogger(__name__)

from new import classobj
from contextlib import closing

from phonedb.countrydb.data import get_country_data
from phonedb.countrydb.countries.states import StatesMixin


class CountryResourceMetaClass(type):
    """

    """

    cache = {}

    def __new__(mcs, *args):
        """

        """
        return type.__new__(mcs, *args)

    def __call__(cls, *args):
        """

        """
        country_code = cls.country_code.lower()
        cached = cls.cache.get(country_code)

        if cached:
            return cached

        instance = type.__call__(cls, *args)
        cls.cache.update({country_code: instance})
        return instance


class CountryResource(StatesMixin):
    """

    """

    __metaclass__ = CountryResourceMetaClass

    def __init__(self, *args, **kwargs):
        pass

    def __unicode__(self):
        return unicode(' - '.join([self.__class__.__name__, self.country_name]))

    def __str__(self):
        return str(' - '.join([self.__class__.__name__, self.country_name]))

    def __repr__(self):
        return '%s()' % self.__class__.__name__


with closing(get_country_data()) as data:
    country_data = next(data)
    logging.debug('[builder] building country against (country_data: %s)' % country_data)

    country_class_name = str(country_data.get('country_code').capitalize())

    docstring = """%s country resource

    Country resource is designed to fetch out country and state specific data about the country
    -------------------------
    Attributes: %s

    """ % (
        country_class_name,
        map(str, []),
    )

    country_resource_dict = {
        "__doc__": docstring,
        "_short_name": country_data.get('country_code')
    }
    country_resource_dict.update(country_data)

    globals()[country_class_name] = classobj(country_class_name, (CountryResource,), country_resource_dict)