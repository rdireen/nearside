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


#--------------------------Place in each *.py file----------------------------
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from six.moves import range  #use range instead of xrange
#-----------------------------------------------------------------------------

import json
import os
from os.path import dirname
import sys


with open(dirname(__file__) + '/pkg_info.json') as fp:
    _info = json.load(fp)

__version__ = _info['version']
__author__ = _info['author']




