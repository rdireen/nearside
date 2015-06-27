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
test_translate_symmetric_probe = "test_translate_symmetric_probe"
test_p_correct_response = "test_p_correct_response"


msg1 = "not getting full precision between Matlab and Python for reciprocity"
msg2 = "not getting full precision between Matlab and Python for rotate by pi"
msg3 = "not getting full precision between Matlab and Python for translation"

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
                self.assertAlmostEqual(diff, 0, places = 14)


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
                self.assertAlmostEqual(diff, 0, places = 10)


    def test_translate_symmetric_probe_matlab(self):
        """:: Test translate_symmetric_probe from matlab output
        
        The test compares the output to the same routine written in Matlab
        """

        print(" ")

        # EXTERNAL: Do the external case first

        for Nmax in range(6,8):
            for Mmax in range(Nmax - 1, Nmax + 1):
                filename_c = "coeffs3_%d_%d.tst" % (Nmax, Mmax)
                filename_rc = "coeffs3_trans_%d_%d.tst" % (Nmax, Mmax)
                path_c = os.path.join(path,
                                      test_path,
                                      test_translate_symmetric_probe,
                                      filename_c)
                path_rc = os.path.join(path,
                                       test_path,
                                       test_translate_symmetric_probe,
                                       filename_rc)

                print(filename_rc)

                (c_m,d) = fl.load_vcoef(path_c)
                (rc_m,d) = fl.load_vcoef(path_rc)
                
                # Last flag makes this the EXTERNAL case
                R_python = nss.translate_symmetric_probe(60, c_m, 27,
                                                   region = nss.external)

                # Put data from Matlab in the correct format
                neg = rc_m[:,-1]
                pos = rc_m[:, 1]
                muneg1 = np.column_stack(neg)
                mu1 = np.column_stack(pos)
                R_matlab = np.column_stack((muneg1,mu1))


                diff = np.amax(np.abs(R_python - R_matlab) / 
                                   (np.abs(R_matlab) + 1e-15))

                self.assertAlmostEqual(diff, 0, places = 13, msg = msg3)

        # INTERNAL: This is the internal case

        for Nmax in range(6,8):
            for Mmax in range(Nmax - 1, Nmax + 1):
                filename_c = "coeffs4_%d_%d.tst" % (Nmax, Mmax)
                filename_rc = "coeffs4_trans_int_%d_%d.tst" % (Nmax, Mmax)
                path_c = os.path.join(path,
                                      test_path,
                                      test_translate_symmetric_probe,
                                      filename_c)
                path_rc = os.path.join(path,
                                       test_path,
                                       test_translate_symmetric_probe,
                                       filename_rc)

                print(filename_rc)

                (c_m,d) = fl.load_vcoef(path_c)
                (rc_m,d) = fl.load_vcoef(path_rc)
                
                # Last flag makes this the INTERNAL case
                R_python = nss.translate_symmetric_probe(60, c_m, 27,
                                                   region = nss.internal)

                # Put data from Matlab in the correct format
                neg = rc_m[:,-1]
                pos = rc_m[:, 1]
                muneg1 = np.column_stack(neg)
                mu1 = np.column_stack(pos)
                R_matlab = np.column_stack((muneg1,mu1))


                diff = np.amax(np.abs(R_python - R_matlab) / 
                                   (np.abs(R_matlab) + 1e-15))

                self.assertAlmostEqual(diff, 0, places = 13, msg = msg3)


    def test_probe_correct_compare_matlab(self):
        """:: Test probe_correct and probe_response from matlab output
        
        The test compares the output to the same routine written in Matlab
        """ 

        print(" ")

        # PROBE CORRECT

        for Nmax in range(6,8):
            for Mmax in range(Nmax - 1, Nmax + 1):
                filename_c = "coeffs5_a_%d_%d.tst" % (Nmax, Mmax)
                filename_rc = "coeffs5_a_pcorrect_%d_%d.tst" % (Nmax, Mmax)
                filename_p = "coeffs5_p.tst"
                path_c = os.path.join(path,
                                      test_path,
                                      test_p_correct_response,
                                      filename_c)
                path_rc = os.path.join(path,
                                       test_path,
                                       test_p_correct_response,
                                       filename_rc)
                path_p = os.path.join(path,
                                       test_path,
                                       test_p_correct_response,
                                       filename_p)

                print(filename_rc)

                (c_m,d) = fl.load_vcoef(path_c)
                (rc_m,d) = fl.load_vcoef(path_rc)
                (p_m,d) = fl.load_vcoef(path_p)

                # Last flag makes this the EXTERNAL case
                R_python = nss.translate_symmetric_probe(60, p_m, 27,
                                                   region = nss.external)

                dnm = nss.probe_correct( c_m, R_python)

                diff = sp.LInf_coef(dnm - rc_m)

                self.assertLess(diff, 1e-12)

        # PROBE RESPONSE

        for Nmax in range(6,8):
            for Mmax in range(Nmax - 1, Nmax + 1):
                filename_c = "coeffs6_a_%d_%d.tst" % (Nmax, Mmax)
                filename_rc = "coeffs6_a_presponse_%d_%d.tst" % (Nmax, Mmax)
                filename_p = "coeffs6_p.tst"
                path_c = os.path.join(path,
                                      test_path,
                                      test_p_correct_response,
                                      filename_c)
                path_rc = os.path.join(path,
                                       test_path,
                                       test_p_correct_response,
                                       filename_rc)
                path_p = os.path.join(path,
                                       test_path,
                                       test_p_correct_response,
                                       filename_p)

                print(filename_rc)

                (c_m,d) = fl.load_vcoef(path_c)
                (rc_m,d) = fl.load_vcoef(path_rc)
                (p_m,d) = fl.load_vcoef(path_p)

                # Last flag makes this the EXTERNAL case
                R_python = nss.translate_symmetric_probe(60, p_m, 27,
                                                   region = nss.external)

                dnm = nss.probe_response( c_m, R_python)

                diff = sp.LInf_coef(dnm - rc_m)

                self.assertLess(diff, 1e-12)

    def test_probe_correct_and_probe_response(self):
        """:: Test probe_correct and probe_response based on inverses
        
        probe_response is the inverse of probe_correct, this tests that to make
        sure it's true.
        """  

        p_m = sp.random_coefs(5, 1, coef_type=sp.vector)

        for Nmax in range(10,14):
            for Mmax in range(Nmax - 1, Nmax + 1):
                 
                c_m = sp.random_coefs(Nmax, Mmax, coef_type=sp.vector)

                R_python = nss.translate_symmetric_probe(60, p_m, 27,
                                                           region = nss.external)


                # Do probe response and probe correct here
                dnm_response = nss.probe_response( c_m, R_python)
                dnm_corrected = nss.probe_correct( dnm_response, R_python)

                diff = sp.LInf_coef(dnm_corrected - c_m)

                self.assertLess(diff, 1e-12)


        
             
           
                    