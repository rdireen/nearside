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

         sphere_low_level: spherical case low level routines 

Randy Direen
3/28/2015

A description

***************************************************************************"""

#--------------------------Place in each *.py file----------------------------
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from six.moves import range  #use range instead of xrange
#----------------------------------------------------------------------------

#--------------------------------------------------------------------3rd Party
import numpy as np
import spherepy as sp


#=============================================================================
# Global Declarations
#=============================================================================

external = 0
internal = 1

#=============================================================================
# Routines
#=============================================================================



def wigner3j_mzero_squared(j2, j3):

    a = min([j2,j3])

    v = np.zeros(a + 1, dtype = np.complex128)
    v[a] = 1
    alpha = j2 + j3
    s = 2 * alpha + 1;

    xi = lambda alpha, j2, j3: (alpha ** 2 - (j2 - j3) ** 2) * \
                               ((j2 + j3 + 1) ** 2 - alpha ** 2)

    for m in range(a - 1, -1, -1):
        v[m] = xi(alpha, j2, j3) / xi(alpha - 1 , j2, j3) * v[m + 1];
        alpha = alpha-2;
        s += (2 * alpha + 1) * v[m];
    
    return v / s;

def bc(nu, n):

    v = np.zeros(nu + n + 1, dtype = np.complex128)
    a = min([nu, n])
    c1 = 1 / (4 * nu * (nu + 1) * n * (n + 1))
    c2 = nu * (nu + 1) + n * (n + 1);
    c3 = np.sqrt((2 * nu + 1) * (2 * n + 1) / (4 * np.pi))
    c4 = (nu - n) ** 2
    c5 = (nu + n + 1) ** 2
    t =  wigner3j_mzero_squared(nu, n)

    alpha = nu + n

    v[alpha] = np.sqrt(2 * alpha + 1) * c3 * \
               (alpha * (alpha + 1) - c2) ** 2 * c1 * t[a]

    for m in range(a - 1, -1, -1):
        alpha = alpha - 2
        beta = (alpha + 1) ** 2
        v[alpha + 1] = np.sqrt(2 * alpha + 3) * c3 * \
                       (beta - c4) * (c5 - beta) * c1 * t[m];
        v[alpha] = np.sqrt(2 * alpha + 1) * c3 * \
                   (alpha * (alpha + 1) - c2) ** 2 * c1 * t[m];

    return v

def bc_comp(nu, n, x, region=external):

    L = abs(nu - n)
    U = nu + n

    y = bc(nu, n)
    
    if region == external:
        h = sp.sbesselh1(x, len(y))
    elif region == internal:
        h = sp.sbesselj(x, len(y))
    else:
        raise ValueError("region must be either external or internal")

    B = 0
    C = 0

    i2alpha = 1j ** L

    for alpha in range(L, U + 1, 2):
        B += np.sqrt(2 * alpha + 1) * y[alpha] * i2alpha * h[alpha];
        i2alpha = -i2alpha;

    i2alpha = 1j ** (L + 1)

    for alpha in range(L + 1, U, 2):
        C += np.sqrt(2 * alpha + 1) * y[alpha] * i2alpha * h[alpha];
        i2alpha = -i2alpha;

    B *= np.sqrt(np.pi)
    C *= np.sqrt(np.pi)

    return (B, C)

def translate_mu_plus_minus_one_probe(NN, muneg1, mu1, kr, region=external):
    """ Calculates the translated probe coefficients R from the sh pattern 
    coefficients see R_tran from P_coeff_int.f90 or IR3955 7-4. NN is the 
    multipole limit and x = kr_p. The result Rin is an NN+1 by 4 array.
    Columns 0 and 1 contain the m=-1 components of the magnetic and electric
    coefficients. Columns 2 and 3 contain the m = 1 coefficients. The row 
    number corresponds to the multipole index.

      muneg1 is a NN+1 by 2 array containing the mu=-1 coefficients. The first
    column are the magnetic coefficients and the second row contains the
    electric coefficients. 

      mu1 is a NN+1 by 2 array containing the mu=1 coefficients. The first
    column are the magnetic coefficients and the second row contains the
    electric coefficients.  
    """

    R = np.zeros([NN+1,4], dtype = np.complex128)

    for n in range(1, NN + 1):
        for m in range(1, mu1.shape[0] + 1):
            BB, CC =  bc_comp(m, n, kr, region)
            R[n, 0] += +mu1[m - 1, 0] * BB + mu1[m - 1, 1] * CC
            R[n, 1] += -mu1[m - 1, 0] * CC - mu1[m - 1, 1] * BB
            R[n, 2] += +muneg1[m - 1, 0] * BB - muneg1[m - 1, 1] * CC
            R[n, 3] += +muneg1[m - 1, 0] * CC - muneg1[m - 1, 1] * BB

    return R

def make_inverse_R_matrix(R, n):
    M = np.zeros((2, 2), dtype = np.complex128)

    M[0, 0] = -R[n, 1] - R[n, 3]
    M[0, 1] = -R[n, 1] + R[n, 3]
    M[1, 0] = R[n, 0] + R[n, 2]
    M[1, 1] = R[n, 0] - R[n, 2]

    det = R[n, 0] * R[n, 3] - R[n, 1] * R[n, 2]

    f = np.sqrt((2.0 * n + 1.0) / (4.0 * np.pi))

    return M * 1j * f / (2.0 * det)

def make_forward_R_matrix(R, n):
    M = np.zeros((2, 2), dtype = np.complex128)

    M[0, 0] = R[n, 0] - R[n, 2]
    M[0, 1] = R[n, 1] - R[n, 3]
    M[1, 0] = -R[n, 0] - R[n, 2]
    M[1, 1] = -R[n, 1] - R[n, 3]

    g = np.sqrt((4.0 * np.pi) / (2.0 * n + 1.0))

    return M * 1j * g

def probe_correct(R, tsh):
    """ Corrects the probe response psh to the sh pattern tsh. R is the 4
    column matrix of translated probe coefficients."""

    pass

def probe_response(R, psh):
    """ Calulates the probe response psh to the sh pattern tsh. R is the 4
    column matrix of translated probe coefficients. """

    pass

    








         


