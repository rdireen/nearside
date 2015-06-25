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

           Holds all the structures for planar measurements

Randy Direen
3/06/2015

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
import nearside.probe as pb

#==============================================================================
# Global Declarations
#==============================================================================

err_msg = {}


#=============================================================================
# Objects
#=============================================================================

#-=-=-=-=-=-=-=-=-=-=-= COEFFICIENT REPRESENTATIONS =-=-=-=-=-=-=-=-=-=-=-=-=-
# The coefficients represent the device or environment that has been measured.
# These coefficients can be transformed back to field values.

class PlanarScalarCoeffs(object):
    pass

class PlanarVectorCoeffs(object):
    pass

#-=-=-=-=-=-=-=-=-=-=-= MEASURED ON UNIFORM GRID =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# These objects use the algorithms that require data to be equally spaced in
# the theta direction and the phi direction.

class PlanarMeasurementScalarUniform(object):
    pass

class PlanarMeasurementTransverseUniform(object):
    pass

#-=-=-=-=-=-=-=-=-=-=-= MEASURED ON NON UNIFORM GRID =-=-=-=-=-=-=-=-=-=-=-=-=
# These objects use the algorithms that DO NOT require data to be equally
# spaced in the theta direction and the phi direction.

class PlanarMeasurementScalarNonUniform(object):
    pass

class PlanarMeasurementTransverseNonUniform(object):
    pass
