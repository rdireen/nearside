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
import copy

#--------------------------------------------------------------------3rd Party
import numpy as np
import spherepy as sp

#------------------------------------------------------------------------Custom

#==============================================================================
# Decorators
#==============================================================================



#==============================================================================
# Operations
#==============================================================================

def reciprocity( spherical_coefficients ):
    
    if isinstance( spherical_coefficients, sp.VectorCoefs): 
          
        return _reciprocity_implemented( spherical_coefficients )

    else:
        ValueError("cannot perform reciprocity on this object.")



def _reciprocity_implemented( spherical_coefficients ):

    sc = spherical_coefficients.copy()

    A = sc[:,0]
    A[0][1::2] = -A[0][1::2]
    A[1][0::2] = -A[1][0::2]
    sc.scoef1[:,0] = A[0]
    sc.scoef2[:,0] = A[1]

    for k in range(1, sc.mmax + 1):
        if (k % 2 != 1):
            A = sc[:,k]
            A[0][1::2] = -A[0][1::2]
            A[1][0::2] = -A[1][0::2]
            sc.scoef1[:,k] = A[0]
            sc.scoef2[:,k] = A[1]

            A = sc[:,-k]
            A[0][1::2] = -A[0][1::2]
            A[1][0::2] = -A[1][0::2]
            sc.scoef1[:,-k] = A[0]
            sc.scoef2[:,-k] = A[1]
        else:
            A = sc[:,k]
            A[1][1::2] = -A[1][1::2]
            A[0][0::2] = -A[0][0::2]
            sc.scoef1[:,k] = A[0]
            sc.scoef2[:,k] = A[1]

            A = sc[:,-k]
            A[1][1::2] = -A[1][1::2]
            A[0][0::2] = -A[0][0::2]
            sc.scoef1[:,-k] = A[0]
            sc.scoef2[:,-k] = A[1]

    return sc


def directivity_boresite( spherical_coefficients ):
    if isinstance( spherical_coefficients, sp.VectorCoefs):     
        
        return _directivity_boresite_implementation( spherical_coefficients )

    else:
        ValueError("cannot perform reciprocity on this object.") 

def _directivity_boresite_implementation( spherical_coefficients ):
    pass

def rotate_around_y_by_pi( spherical_coefficients ):
    if isinstance( spherical_coefficients, sp.VectorCoefs):     
        
        return _rotate_around_y_by_pi_implementation( spherical_coefficients )

    else:
        ValueError("cannot perform reciprocity on this object.")

def _rotate_around_y_by_pi_implementation( spherical_coefficients ):

    sc = spherical_coefficients.copy()

    A = sc[:,0]

    L = len(A[0])
    vec = -np.ones(L, dtype=np.complex128)
    ll =  np.array(list(range(0, L)), dtype=np.complex128)
    vec = vec**ll

    sc.scoef1[:,0] = A[0][:]*vec
    sc.scoef2[:,0] = A[1][:]*vec

    for m in range(1, sc.mmax + 1):
        Am = spherical_coefficients[:,-m]
        Ap = spherical_coefficients[:, m]

        L = len(Am[0])
        vec = -np.ones(L, dtype=np.complex128)
        ll =  m + np.array(list(range(m, L + m)), dtype=np.complex128)
        vec = vec**ll

        sc.scoef1[:,-m] = Ap[0][:] * vec
        sc.scoef2[:,-m] = Ap[1][:] * vec

        sc.scoef1[:,m] = Am[0][:] * vec
        sc.scoef2[:,m] = Am[1][:] * vec

    return sc




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