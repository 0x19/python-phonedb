# -*- coding: UTF-8 -*-

from phonedb.about import __author__, __copyright__, __credits__, __license__, __version__, __maintainer__, \
    __email__, __status__

import os

from phonedb.logger import logging
logging = logging.getLogger(__name__)


class Config(object):
    """

    """

    COUNTRIES_DATABASE_FILE = '/'.join([os.getcwd(), 'phonedb/data/countries.db'])