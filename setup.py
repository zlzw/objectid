import os
import re
from setuptools import setup


def get_version_from_init():
    file = open(os.path.join(os.path.dirname(__file__), 'objectid', '__init__.py'))

    regexp = re.compile(r".*__version__ = '(.*?)'", re.S)
    version = regexp.match(file.read()).group(1)
    file.close()

    return version


setup(
    name='objectid',
    license='MIT',
    author='Maximo Cuadros',
    author_email='maximo@tyba.com',
    version=get_version_from_init(),
    url='https://github.com/tyba/objectid',
    packages=[
        'objectid'
    ]
)
