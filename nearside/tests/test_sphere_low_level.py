


from __future__ import division
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from unittest import TestCase

from six.moves import range  #use range instead of xrange

import nearside as ns


class TestSphereLowLevelProbeCorrect(TestCase):

    def test_wigner3j_mzero_squared(self):
        """:: Test computation of the Wigner 3j symboles
        
        The test compares the output to the same routine written in Matlab
        """

        sll = ns.sphere_low_level

        # These were computed in MATLAB and copied here:
        ml = [[1],
             [0.333333333333333],
             [0.200000000000000],
             [0.142857142857143],
             [0.333333333333333],
             [0.333333333333333, 0.133333333333333],
             [0.133333333333333, 0.085714285714286],
             [0.085714285714286, 0.063492063492063],
             [0.200000000000000],
             [0.133333333333333, 0.085714285714286],
             [0.200000000000000, 0.057142857142857, 0.057142857142857],
             [0.085714285714286, 0.038095238095238, 0.043290043290043],
             [0.142857142857143],
             [0.085714285714286, 0.063492063492063],
             [0.085714285714286, 0.038095238095238, 0.043290043290043],
             [0.142857142857143],
             [0.085714285714286, 0.063492063492063],
             [0.085714285714286, 0.038095238095238, 0.043290043290043],
             [0.142857142857143, 0.038095238095238, 0.025974025974026, 0.033300033300033],
             ]

        idx = 0
        for j2 in range(0,4):
            for j3 in range(0,4):
                value_python = sll.wigner3j_mzero_squared(j2, j3)
                value_matlab = ml[idx]
                for n, _ in enumerate(ml[idx]): 
                    self.assertAlmostEqual(value_python[n],
                                           value_matlab[n],
                                           places=15)

                idx += 1

    def test_bc(self):
        """:: Test computation of the bc coefficients used for translation


        """
        sll = ns.sphere_low_level   
        
        ml = [[0.282094791773878, 0.244301255951460, 0.063078313050504],
              [0, 0.189234939151512, 0.244301255951460, 0.082588898361159],
              [0, 0, 0.165177796722317, 0.244301255951460, 0.092337195461186],
              [0, 0.189234939151512, 0.244301255951460, 0.082588898361159],
              [0.282094791773878, 0.081433751983820, 0.045055937893217,
               0.213243618622923, 0.107464682580525],
              [0, 0.220237062296423, 0.106621809311462, 0.021026104350168, 
               0.198678011253707, 0.119807348622282],
              [0, 0, 0.165177796722317, 0.244301255951460, 0.092337195461186],
              [0, 0.220237062296423, 0.106621809311462, 0.021026104350168,
               0.198678011253707, 0.119807348622282],
              [0.282094791773878, 0.040716875991910, 0.094617469575756, 
               0.124392110863372, 0.004274163511725, 0.177197458262763, 
               0.133361962799220]
              ]

        idx = 0
        for nu in range(1,4):
            for n in range(1,4):
                value_python = sll.bc(nu, n)
                value_matlab = ml[idx]
                for k, _ in enumerate(ml[idx]): 
                    self.assertAlmostEqual(value_python[k],
                                           value_matlab[k],
                                           places=15)

                idx += 1 
           











                       




        


