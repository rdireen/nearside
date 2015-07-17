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

Credits:
The algorithms within this package have been implemented, in part, using the 
documentation within the NIST Interagency/Internal Report (NISTIR) - 3955.
The majority or the code, however, has been developed using 
Ronald C. Wittmann's unpublished notes.

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
from . import low_level 

#------------------------------------------------------------------------Custom

#=============================================================================
# Global Declarations
#=============================================================================

external = 0
internal = 1

#==============================================================================
# Operations
#==============================================================================

def reciprocity( coefficients ):
    """Return reciprocal version of the VectorCoefs object *coefficients*.
    The operation maps the direction vector **r** to -**r**. 

    Example::

        >>> c = spherepy.random_coefs(3,3)
        >>> p = nearside.spherical.reciprocity(c)
        >>> print(p)

    Args:
      coefficients (VectorCoefs): The coefficients to be transformed to 
      pattern space.

    Returns:
      VectorCoefs: This is the reciprocal version of the input coefficients. 

    Raises:
      TypeError: Is raised if coefficients isn't a VectorCoefs object.

    """
    
    if isinstance( coefficients, sp.VectorCoefs): 
          
        return _reciprocity_implemented( coefficients )

    else:
        TypeError("cannot perform reciprocity on this object.")



def _reciprocity_implemented( coefficients ):

    sc = coefficients.copy()

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



def rotate_around_y_by_pi( coefficients ):
    """Rotates the probe by pi radians in coefficient space.

    Example::

        >>> c = spherepy.random_coefs(3,3)
        >>> p = nearside.spherical.rotate_around_y_by_pi(c)
        >>> print(p)

    Args:
      coefficients (VectorCoefs): The coefficients to be rotated. 

    Returns:
      VectorCoefs: This is the rotated version of the input coefficients. 

    Raises:
      TypeError: Is raised if coefficients isn't a VectorCoefs object.

    """
    if isinstance( coefficients, sp.VectorCoefs):     
        
        return _rotate_around_y_by_pi_implementation( coefficients )

    else:
        TypeError("cannot rotate this object.")

def _rotate_around_y_by_pi_implementation( coefficients ):

    sc = coefficients.copy()

    A = sc[:,0]

    L = len(A[0])
    vec = -np.ones(L, dtype=np.complex128)
    ll =  np.array(list(range(0, L)), dtype=np.complex128)
    vec = vec**ll

    sc.scoef1[:,0] = A[0][:]*vec
    sc.scoef2[:,0] = A[1][:]*vec

    for m in range(1, sc.mmax + 1):
        Am = coefficients[:,-m]
        Ap = coefficients[:, m]

        L = len(Am[0])
        vec = -np.ones(L, dtype=np.complex128)
        ll =  m + np.array(list(range(m, L + m)), dtype=np.complex128)
        vec = vec**ll

        sc.scoef1[:,-m] = Ap[0][:] * vec
        sc.scoef2[:,-m] = Ap[1][:] * vec

        sc.scoef1[:,m] = Am[0][:] * vec
        sc.scoef2[:,m] = Am[1][:] * vec

    return sc

def translate_symmetric_probe( NN, coefficients, kr, region = external):

    if isinstance( coefficients, sp.VectorCoefs): 
        neg = coefficients[:,-1]
        pos = coefficients[:, 1]

        muneg1 = np.column_stack(neg)
        mu1 = np.column_stack(pos)
        
        R = low_level.translate_mu_plus_minus_one_probe(NN, muneg1, mu1, kr, 
                                                        region = region )  

        return R

    else:
        TypeError("cannot translate this object.")
     

def probe_correct( coefficients_to_correct, translated_probe_data):
    """Correctes the measured data using the probe data.
    Probe correction is performed in coefficient space.

    

    """
       
    if isinstance( coefficients_to_correct, sp.VectorCoefs):
                                                                                 
        R = translated_probe_data
        tsh = coefficients_to_correct
        psh = tsh.copy()

        # correct each mode individually
        for n in range(1, tsh.nmax + 1):
            for m in range( -n, n + 1 ):
                if ( abs(m) <= tsh.mmax ):
                    M = low_level.make_inverse_R_matrix(R, n)
                    psh[n,m] = list(np.dot( M, tsh[n, m] ))

        corrected_coefficients = psh

        return corrected_coefficients

    else:
        TypeError("cannot probe correct this object.")


def probe_response( coefficients, translated_probe_data):

    if isinstance( coefficients, sp.VectorCoefs):
                                                                                 
        R = translated_probe_data
        tsh = coefficients
        psh = tsh.copy()

        # correct each mode individually
        for n in range(1, tsh.nmax + 1):
            for m in range( -n, n + 1 ):
                if ( abs(m) <= tsh.mmax ):
                    M = low_level.make_forward_R_matrix(R, n)
                    psh[n,m] = list(np.dot( M, tsh[n, m] ))

        responded_coefficients = psh

        return responded_coefficients

    else:
        TypeError("no probe response for this object.")

def transform_to_vcoeffs( transverse_uniform ):
    pass

def transform_to_transverse_uniform( coefficients ):
    pass

def transform_to_far_field( vector_coeffs ):
    pass

def transform_to_local_field( coefficients, radius_meters ):
    pass

def standard_cuts( transverse_pattern_uniform ):
    """ The magnitude of the cuts along phi = 0 [deg] and phi = 90 [deg] 
    
    
    """

    mt = transverse_pattern_uniform.theta_double
    mp = transverse_pattern_uniform.phi_double

    mag = np.sqrt( np.abs(mt) ** 2 + np.abs(mp) ** 2 )

    cut_phi_0 = mag[:,0]
    L = mag.shape[1]
    idx = int( L / 4 )
    cut_phi_90 = mag[:,idx]

    front = cut_phi_0[0 : int( cut_phi_0.shape[0] / 2 ) - 1]
    back = cut_phi_0[int( cut_phi_0.shape[0] / 2 ) - 1 ::]
    cut_phi_0 = np.concatenate((back,front))

    front = cut_phi_90[0 : int( cut_phi_90.shape[0] / 2 ) - 1]
    back = cut_phi_90[int( cut_phi_90.shape[0] / 2 ) - 1 ::]
    cut_phi_90 = np.concatenate((back,front))

    return (cut_phi_0, cut_phi_90)

