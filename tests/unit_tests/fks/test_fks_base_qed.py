################################################################################
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
################################################################################

"""Testing modules for FKS_process class"""

import sys
import os
root_path = os.path.split(os.path.dirname(os.path.realpath( __file__ )))[0]
sys.path.insert(0, os.path.join(root_path,'..','..'))

import tests.unit_tests as unittest
import madgraph.fks.fks_base as fks_base
import madgraph.fks.fks_common as fks_common
import madgraph.core.base_objects as MG
import madgraph.core.color_algebra as color
import madgraph.core.diagram_generation as diagram_generation
import models.import_ufo as import_ufo
import madgraph.iolibs.helas_call_writers as helas_call_writers
import copy
import array


class TestFKSQED(unittest.TestCase):
    """a class to test FKS Processes, with QED perturbation"""

    def setUp(self):
        if not hasattr(self, 'mymodel'):
            created_files = ['test']
            TestFKSQED.mymodel = import_ufo.import_model('sm')
            #remove third and fourth generation of quarks, and the muon
            particles_to_rm = [3, 4, 13]
            for p in particles_to_rm:
                part = TestFKSQED.mymodel.get('particle_dict')[p]
                TestFKSQED.mymodel['particles'].remove(part)
                bad_vertices = [vert for vert in TestFKSQED.mymodel['interactions'] \
                        if part in vert['particles']]
                for vert in bad_vertices:
                    TestFKSQED.mymodel['interactions'].remove(vert)


    def test_qqtoqqQed(self):
        """test the dijet QED corrections for a subprocess"""
        leglist = MG.MultiLegList()
        leglist.append(MG.MultiLeg({'ids': [1], 'state': False}))
        leglist.append(MG.MultiLeg({'ids': [-1], 'state': False}))
        leglist.append(MG.MultiLeg({'ids': [2], 'state': True}))
        leglist.append(MG.MultiLeg({'ids': [-2], 'state': True}))

        procdef_dict = {'legs': leglist, 'orders':{'QCD':2, 'QED':2},
                       'model': self.mymodel,
                       'id': 1,
                       'NLO_mode': 'real',
                       'required_s_channels':[],
                       'forbidden_s_channels':[],
                       'forbidden_particles':[],
                       'is_decay_chain': False,
                       'perturbation_couplings':['QED'],
                       'decay_chains': MG.ProcessList(),
                       'overall_orders': {},
                       'born_orders':{'QCD':2, 'QED':2}}

        fksmultiproc = fks_base.FKSMultiProcess(MG.ProcessDefinition(procdef_dict))
        fksproc = fksmultiproc['born_processes'][0]
        # check perturbation
     #   self.assertEqual(fksproc.perturbation, 'QED')
        # check correct number of diagrams at born (4)
        # 3 s channels (a, z, g)
        # 1 t channel (w)
        self.assertEqual(len(fksproc.born_amp_list[0]['diagrams']), 4)
        # check correct colors and charges
        self.assertEqual(fksproc.get_colors(), [[3,-3,3,-3]])
        self.assertEqual(len(fksproc.get_charges()[0]), 4)
        for q1, q2 in zip(fksproc.get_charges()[0],[-1./3., 1./3., 2./3., -2./3.]):
            self.assertAlmostEqual(q1, q2)
        # check real emissions:
        # from the first and second leg, one can have the final and initial
        # state photon splitting,
        # as well as the final and initial state gluon splittng 
        # (for order consistency)
        self.assertEqual(len(fksproc.reals[0]), 4)
        self.assertEqual(len(fksproc.reals[1]), 4)
        # from the two final state legs, one can either radiate a photon or
        # a gluon
        self.assertEqual(len(fksproc.reals[2]), 2)
        self.assertEqual(len(fksproc.reals[3]), 2)
        

    def test_pptojj_2flav(self):
        """test the dijet QED corrections for dijet production"""

        multi_ids = [1, -1, 2, -2, 22, 21]
        p = MG.MultiLeg({'ids': multi_ids, 'state': False})
        j = MG.MultiLeg({'ids': multi_ids, 'state': True})
        leglist = MG.MultiLegList([p, p, j, j])

        procdef_dict = {'legs': leglist, 'orders':{'QCD':2, 'QED':1},
                       'model': self.mymodel,
                       'id': 1,
                       'NLO_mode': 'real',
                       'required_s_channels':[],
                       'forbidden_s_channels':[],
                       'forbidden_particles':[],
                       'is_decay_chain': False,
                       'perturbation_couplings':['QED'],
                       'decay_chains': MG.ProcessList(),
                       'overall_orders': {},
                       'squared_orders': {'QCD':4, 'QED':2},
                       'born_orders':{'QCD':2, 'QED':0}}
         
        fksmultiproc = fks_base.FKSMultiProcess(MG.ProcessDefinition(procdef_dict))
        #check that the correct orders are set for the real amplitudes
        print len(fksmultiproc['born_processes'])
        born_pdg_list = [amp.get_pdg_codes() for amp in fksmultiproc['born_processes']]
        for amp in fksmultiproc['born_processes']:
            print amp.get_pdg_codes()

        #there should be 35 born processes
        self.assertEqual(len(fksmultiproc['born_processes']), 35)

###        for amp in fksmultiproc['real_amplitudes']:
         ###   print [l['id'] for l in amp['process']['legs']], len(amp['diagrams']), amp['process']['orders']
#            self.assertTrue(len(amp['diagrams']) > 0)

        for born in fksmultiproc['born_processes']:
            for real in born.real_amps:
                print real.pdgs
                print 'orders', real.amplitude['process']['orders']
                print 'sq_orders', real.amplitude['process']['squared_orders']
                print 'diagrams', len(real.amplitude['diagrams'])
                print [[l['id'] for l in born['born_amp']['process']['legs']] for born in real.missing_borns]
                self.assertEqual(len(real.missing_borns), 0)

                for missing_born in real.missing_borns:
                    self.assertTrue([l['id'] for l in missing_born['born_amp']['process']['legs']] not in born_pdg_list)

                    


        




