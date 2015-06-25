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

"""***************************************************************************

                Standard operations on spherical structures

Randy Direen
6/25/2015

A description

***************************************************************************"""

#--------------------------Place in each *.py file----------------------------
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from six.moves import range  #use range instead of xrange
#-----------------------------------------------------------------------------

#---------------------------------------------------------------------Built-ins

import json
from os.path import dirname

#--------------------------------------------------------------------3rd Party
import numpy as np
import spherepy as sp

#------------------------------------------------------------------------Custom
import nearside.spherical.structures as structures

#==============================================================================
# Operations
#==============================================================================

def reciprocity( spherical_coefficients ):
    pass

def directivity( spherical_coefficients ):
    pass 

def probe_correct( spherical_coefficients, probe):
    pass

def transform_to_vcoeffs( transverse_uniform ):
    pass

def transform_to_transverse_uniform( vector_coeffs ):
    pass

def transform_to_far_field( vector_coeffs ):
    pass

def transform_to_local_field( vector_coeffs, radius_meters ):
    pass