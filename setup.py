# Copyright (C) 2015  Randy Direen <nearside@direentech.com>
#
# This file is part of NearSide.
#
# NearSide is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# NearSide is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NearSide.  If not, see <http://www.gnu.org/licenses/>

"""

Note about NumPy:

    NumPy is a necessary part of NearSide, but there are many ways to install
    it. On Ubuntu you can install the the python-numpy package with apt-get or
    use pip, and on Windows you can use full systems like Anaconda, download
    wheels from unofficial sites, or if you have the compilers for the right 
    version of the Python distribution you can build it yourself. Since there
    are so many ways to get NumPy, I think I will require people to install
    and update it themselves and not put it in the requirements here.

"""

import os
import sys
import json

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'nearside/pkg_info.json')) as fp:
    _info = json.load(fp)

def readme():
    with open('README.md') as f:
        return f.read()

__version__ = _info['version']
__author__ = _info['author']
__email__ = _info['email']
__download_url__ = _info['download_url']

try:
    from setuptools import setup
except ImportError:
    print("NearSide requires setuptools in order to build. Install " + \
          "setuptools using your package manager (possibly " + \
          "python-setuptools) or using pip (i.e., pip install "
          "setuptools")
    sys.exit(1)

description = 'A package for processing antenna near-field measurements.'
 
""" ***IMPORTANT*** note about distutils

package_data is only for binary builds and not source distributions.
MANIFEST.in is for source and not binary.

So if you want a data file in the binary builds and the source builds
you have to point to them with package_data AND MANIFEST.in.
"""

setup(name='nearside',
      version=__version__,
      author=__author__,
      author_email=__email__,
      description=description,
      long_description=readme(),
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: Microsoft :: Windows :: Windows 7',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Physics'
      ],
      url='https://github.com/rdireen/nearside',  # url to github repo
      download_url=__download_url__,
      license='GPLv3',
      install_requires=['six','spherepy'],
      keywords=['near-field antenna measurments planar spherical cylindrical'],
      packages=['nearside','nearside.spherical','nearside.planar','nearside.cylindrical'],
      package_dir={'nearside':'nearside', 'test':'nearside/test'},
      package_data={'nearside':['pkg_info.json']},
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose']
     )

