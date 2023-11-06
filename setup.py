from setuptools import setup, find_packages

NAME = "PyMenuManager"
MAIL = "<welryzis.public@gmail.com>"
LICENSE = "Apache License, Version 2.0"
DESCRIPTION = "Python package for creating and managing console menus."
LONG_DESCRIPTION = ("PyMenuManager - is a simple Python package for create and manage console menus. "
                    "Its provides easy-to-use interface for developers.")
VERSION = "1.0.0"


setup(
    name=NAME,
    version=VERSION,
    author="Welryzis",
    license=LICENSE,
    author_email=MAIL,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'package', 'menu', 'manager', 'menumanager'],
    classifiers=[
        "Development Status :: Released",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.5",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
