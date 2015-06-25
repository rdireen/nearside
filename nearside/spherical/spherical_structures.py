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

            Holds all the structures for spherical measurements

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
err_msg['not_tpu'] = "transverse_pattern_uniform must be a " + \
                                    "spherepy.TransversePatternUniform object"
err_msg['not_probe'] = "probe must be a valid probe object or None"

#=============================================================================
# Objects
#=============================================================================

#-=-=-=-=-=-=-=-=-=-=-= COEFFICIENT REPRESENTATIONS =-=-=-=-=-=-=-=-=-=-=-=-=-
# The coefficients represent the device or environment that has been measured.
# These coefficients can be transformed back to field values.

class SphericalScalarCoeffs(object):
    pass

class SphericalVectorCoeffs(object):
    pass

#-=-=-=-=-=-=-=-=-=-=-= MEASURED ON UNIFORM GRID =-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# These objects use the algorithms that require data to be equally spaced in
# the theta direction and the phi direction.

class SphericalMeasurementScalarUniform(object):
    pass

class SphericalMeasurementTransverseUniform(object):
    def __init__(self, transverse_pattern_uniform, 
                       frequency_ghz = None,
                       radius_meters = None, 
                       probe = None):

        if ( isinstance(transverse_pattern_uniform,
                        sp.TransversePatternUniform) ):

            self._tp = transverse_pattern_uniform
        else:
            ValueError(err_msg['not_tpu'])

        if ( isinstance(probe, pb.VectorProbe) 
             or probe == None):

            self._probe = probe
        else:
            ValueError(err_msg['not_probe'])

        self._radius_meters = radius_meters

        self._frequency_ghz = frequency_ghz

    @property
    def probe(self):
        return self._probe

    @probe.setter
    def probe(self, value):
        if ( isinstance(probe, pb.VectorProbe) or probe == None):
            self._probe = value
        else:
            ValueError("probe must be a valid probe object or None")

    @property
    def nrows(self):
        self._tp.nrows

    @property
    def ncols(self):
        self._tp.nrows

    @property
    def shape(self):
        return self._tp.shape

    @property
    def theta(self):
        return self._tp.theta

    @property
    def phi(self):
        return self._tp.phi

#-=-=-=-=-=-=-=-=-=-=-= MEASURED ON NON UNIFORM GRID =-=-=-=-=-=-=-=-=-=-=-=-=
# These objects use the algorithms that DO NOT require data to be equally
# spaced in the theta direction and the phi direction.

class SphericalMeasurementScalarNonUniform(object):
    pass

class SphericalMeasurementTransverseNonUniform(object):
    pass

