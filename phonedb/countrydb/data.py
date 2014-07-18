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

import sqlite3
from contextlib import closing
from phonedb.config import Config

country_connection = sqlite3.connect(Config.COUNTRIES_DATABASE_FILE)


#@memoize
def get_country_data():
    """

    """
    with closing(country_connection.cursor()) as cursor:
        for row in cursor.execute('SELECT * FROM countries WHERE is_available = 1'):
            yield {
                'county_count': row[0],
                'states_count': row[1],
                'telephone_prefix': row[2],
                'country_name': row[3],
                'country_full_name': row[4],
                'country_code': row[5],
                'country_extended_code': row[6]
            }