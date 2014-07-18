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


def memoize(f):
    """ Memoization decorator for a function taking one or more arguments. """
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__