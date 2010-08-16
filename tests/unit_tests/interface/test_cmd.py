##############################################################################
#
# Copyright (c) 2010 The MadGraph Development team and Contributors
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
################################################################################
""" Basic test of the command interface """

import unittest
import madgraph
import madgraph.interface.cmd_interface as cmd


class TestValidCmd(unittest.TestCase):
    """ check if the ValidCmd works correctly """
    
    cmd = cmd.MadGraphCmdShell()
    
    def wrong(self,*opt):
        self.assertRaises(madgraph.MadGraph5Error, *opt)
        
    def test_check_generate(self):
        """check if generate format are correctly supported"""
    
        cmd = self.cmd
        
        # valid syntax
        cmd.check_process_format('e+ e- > e+ e-')
        cmd.check_process_format('e+ e- > mu+ mu- QED=0')
        cmd.check_process_format('e+ e- > mu+ ta- / x $y @1')
        cmd.check_process_format('e+ e- > mu+ ta- $ x /y @1')
        cmd.check_process_format('e+ e- > mu+ ta- $ x /y, (e+ > e-, e-> ta) @1')
        
        # unvalid syntax
        self.wrong(cmd.check_process_format, ' e+ e-')
        self.wrong(cmd.check_process_format, ' e+ e- > e+ e-,')
        self.wrong(cmd.check_process_format, ' e+ e- > > e+ e-')
        self.wrong(cmd.check_process_format, ' e+ e- > j / g > e+ e-')        
        self.wrong(cmd.check_process_format, ' e+ e- > j $ g > e+  e-')         
        self.wrong(cmd.check_process_format, ' e+ > j / g > e+ > e-')        
        self.wrong(cmd.check_process_format, ' e+ > j $ g > e+ > e-')
        self.wrong(cmd.check_process_format, ' e+ > e+, (e+ > e- / z, e- > top')   
        self.wrong(cmd.check_process_format, 'e+ > ')
        self.wrong(cmd.check_process_format, 'e+ >')