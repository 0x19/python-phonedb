# -*- coding: UTF-8 -*-

from phonedb import PACKAGE_VERSION
from setuptools import setup

setup(
    name                = "python-phonedb",
    version             = PACKAGE_VERSION,
    description         = "Discover various information about specific phone number",
    author              = "Nevio Vesic",
    author_email        = "nevio.vesic@gmail.com",
    license             = "GPLv3",
    url                 = "https://github.com/0x19/python-phonedb",
    keywords            = [
        "phone number", "number", "telephony", "python", "npa", "nxx", "area codes", "country code", "exchange", "zip code",
        "postal code", "lata", "csba", "carrier name", "carrier", "country data", "ocn", "rate center", "fips"
    ],
    install_requires    = [],
    packages            = ['phonedb'],
    classifiers         = [
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
        "Topic :: Communications :: Internet Phone",
        "Topic :: Internet",
        "Topic :: System :: Networking",
        "Topic :: Internet :: WWW/HTTP"
    ],
    long_description    = """
    Package designed to translate phone number into useful data. More about data once package gets out of prototype.
    """,
)