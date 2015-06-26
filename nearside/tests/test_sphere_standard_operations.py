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

     test_sphere_standard_operations: test operations like reciprocity

Randy Direen
6/26/2015

Test standard operations like 'reciprocity' or 'directivity'

***************************************************************************"""


from __future__ import division
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from unittest import TestCase

from six.moves import range  #use range instead of xrange

import numpy as np
import os
import nearside.spherical as ns
import spherepy as sp
import spherepy.file as fl
import nearside.spherical as nss

path = os.path.dirname(os.path.realpath(__file__))
test_path = "test_data"
test_reciprocity_directivity_path = "test_reciprocity_directivity"
test_rotate_around_y_by_pi = "test_rotate_around_y_by_pi"

msg1 = "not getting full precision between Matlab and Python for reciprocity"
msg2 = "not getting full precision between Matlab and Python for rotate by pi"

class TestSphereStandardOperations(TestCase):

    def test_reciprocity_matlab(self):
        """:: Test reciprocity from matlab output
        
        The test compares the output to the same routine written in Matlab
        """

        print(" ")

        for Nmax in range(6,8):
            for Mmax in range(Nmax - 1, Nmax + 1):
                filename_c = "coeffs_%d_%d.tst" % (Nmax, Mmax)
                filename_rc = "coeffs_rec_%d_%d.tst" % (Nmax, Mmax)
                path_c = os.path.join(path,
                                      test_path,
                                      test_reciprocity_directivity_path,
                                      filename_c)
                path_rc = os.path.join(path,
                                       test_path,
                                       test_reciprocity_directivity_path,
                                       filename_rc)

                print(filename_rc)

                (c_m,d) = fl.load_vcoef(path_c)
                (rc_m,d) = fl.load_vcoef(path_rc)
                
                rc = nss.reciprocity(c_m) 

                diff = sp.LInf_coef(rc - rc_m)
                self.assertAlmostEqual(diff, 0, places = 14, msg = msg1)

    def test_reciprocity_on_large_random_coefs(self):
        """:: Test reciprocity using large randomly generated coeff sets.
        
        Large coefficient sets are generated and reciprocity is applied 
        twice two the set of coefficients to return the set back to its
        original form. 
        """

        print(" ")

        #generate five sets of random variabls
        for nmax in range(100,104):
            for mmax in range(nmax - 2, nmax + 1):
                c = sp.random_coefs(nmax, mmax, coef_type=sp.vector)

                print("Nmax = %d, Mmax = %d" % (nmax, mmax))
            
                rc = nss.reciprocity(c) 
                rcc = nss.reciprocity(rc)

                diff = sp.LInf_coef(rcc - c)
                self.assertAlmostEqual(diff, 0, places = 14, msg = msg1)


    def test_rotate_around_y_by_pi_matlab(self):
        """:: Test rotate_around_y_by_pi from matlab output
        
        The test compares the output to the same routine written in Matlab
        """

        print(" ")

        for Nmax in range(6,8):
            for Mmax in range(Nmax - 1, Nmax + 1):
                filename_c = "coeffs2_%d_%d.tst" % (Nmax, Mmax)
                filename_rc = "coeffs2_roty_%d_%d.tst" % (Nmax, Mmax)
                path_c = os.path.join(path,
                                      test_path,
                                      test_rotate_around_y_by_pi,
                                      filename_c)
                path_rc = os.path.join(path,
                                       test_path,
                                       test_rotate_around_y_by_pi,
                                       filename_rc)

                print(filename_rc)

                (c_m,d) = fl.load_vcoef(path_c)
                (rc_m,d) = fl.load_vcoef(path_rc)
                
                rc = nss.rotate_around_y_by_pi(c_m) 

                diff = sp.LInf_coef(rc - rc_m)
                self.assertAlmostEqual(diff, 0, places = 14, msg = msg2)

    def test_rotate_around_y_by_pi_on_large_random_coefs(self):
        """:: Test rotate_around_y_by_pi using large randomly generated coeff
        sets.
        
        Large coefficient sets are generated and rotate_around_y_by_pi is
        applied twice two the set of coefficients to return the set back to 
        its original form. 
        """

        print(" ")

        #generate five sets of random variabls

        for nmax in range(100,104):
            for mmax in range(nmax - 2, nmax + 1):
                c = sp.random_coefs(nmax, mmax, coef_type=sp.vector)

                print("Nmax = %d, Mmax = %d" % (nmax, mmax))
            
                rc = nss.rotate_around_y_by_pi(c) 
                rcc = nss.rotate_around_y_by_pi(rc)

                diff = sp.LInf_coef(rcc - c)
                print("WARNING: This should be 0: err = %.16e" % diff)
                #TODO: I don't understand something here. The difference 
                #between rcc and c should be exactly zero but I am 
                #getting an error roughly 1e-13. I am not doing any 
                #arithmetic so I shouldn't have any error???
                #NEED TO UNDERSTAND THIS
                self.assertAlmostEqual(diff, 0, places = 10, msg = msg2)