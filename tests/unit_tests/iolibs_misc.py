##############################################################################
#
# Copyright (c) 2009 The MadGraph Development team and Contributors
#
# This file is a part of the MadGraph 5 project, an application which 
# automatically generates Feynman diagrams and matrix elements for arbitrary
# high-energy processes in the Standard Model and beyond.
#
# It is subject to the MadGraph license which should accompany this 
# distribution.
#
# For more information, please visit: http://madgraph.phys.ucl.ac.be
#
##############################################################################

"""Unit test library for the Misc routine library in the I/O package"""

import unittest
import madgraph.iolibs.misc as misc

class IOLibsMiscTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testParse_Info_Str_Correct(self):
        "_parse_info_str converts info strings to dictionaries"

        mystr = "param1 = value1\n param2=value 2\n \n"
        rightdict = {'param1':'value1', 'param2':'value 2'}

        self.assertEqual(rightdict, misc._parse_info_str(mystr))

    def testParse_Info_Str_Error(self):
        "_parse_info_str raises an error for strings which are not valid"

        mystr = "param1 : value1"

        self.assertRaises(IOError, misc._parse_info_str, mystr)

if __name__ == "__main__":
    unittest.main()
