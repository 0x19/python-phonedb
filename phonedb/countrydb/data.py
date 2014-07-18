# -*- coding: UTF-8 -*-

from phonedb.about import __author__, __copyright__, __credits__, __license__, __version__, __maintainer__, \
    __email__, __status__

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