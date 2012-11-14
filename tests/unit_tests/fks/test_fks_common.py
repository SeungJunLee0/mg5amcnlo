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

"""Testing modules for fks_common functions and classes"""

import sys
import os
root_path = os.path.split(os.path.dirname(os.path.realpath( __file__ )))[0]
sys.path.insert(0, os.path.join(root_path,'..','..'))

import tests.unit_tests as unittest
import madgraph.fks.fks_common as fks_common
import madgraph.core.base_objects as MG
import madgraph.core.color_algebra as color
import madgraph.core.color_amp as color_amp
import madgraph.core.diagram_generation as diagram_generation
import madgraph.core.helas_objects as helas_objects
import models.import_ufo as import_ufo
import copy
import array
import fractions

class TestFKSCommon(unittest.TestCase):
    """ a class to test FKS common functions and classes"""

    def setUp(self):
        if not hasattr(self, 'model') or not hasattr(self, 'expected_qcd_inter'):

            mypartlist = MG.ParticleList()
            myinterlist = MG.InteractionList()
            mypartlist.append(MG.Particle({'name':'u',
                          'antiname':'u~',
                          'spin':2,
                          'color':3,
                          'mass':'zero',
                          'width':'zero',
                          'texname':'u',
                          'antitexname':'\\overline{u}',
                          'line':'straight',
                          'charge':2. / 3.,
                          'pdg_code':2,
                          'propagating':True,
                          'self_antipart':False}))
            mypartlist.append(MG.Particle({'name':'d',
                          'antiname':'d~',
                          'spin':2,
                          'color':3,
                          'mass':'zero',
                          'width':'zero',
                          'texname':'d',
                          'antitexname':'\\overline{d}',
                          'line':'straight',
                          'charge':-1. / 3.,
                          'pdg_code':1,
                          'propagating':True,
                          'self_antipart':False}))
            mypartlist.append(MG.Particle({'name':'g',
                              'antiname':'g',
                              'spin':3,
                              'color':8,
                              'mass':'zero',
                              'width':'zero',
                              'texname':'g',
                              'antitexname':'g',
                              'line':'curly',
                              'charge':0.,
                              'pdg_code':21,
                              'propagating':True,
                              'is_part':True,
                              'self_antipart':True}))

            mypartlist.append(MG.Particle({'name':'a',
                              'antiname':'a',
                              'spin':3,
                              'color':1,
                              'mass':'zero',
                              'width':'zero',
                              'texname':'\gamma',
                              'antitexname':'\gamma',
                              'line':'wavy',
                              'charge':0.,
                              'pdg_code':22,
                              'propagating':True,
                              'is_part':True,
                              'self_antipart':True}))
            
            mypartlist.append(MG.Particle({'name':'t',
                          'antiname':'t~',
                          'spin':2,
                          'color':3,
                          'mass':'tmass',
                          'width':'twidth',
                          'texname':'t',
                          'antitexname':'\\overline{t}',
                          'line':'straight',
                          'charge':2. / 3.,
                          'pdg_code':6,
                          'propagating':True,
                          'self_antipart':False}))
                
            antiu = MG.Particle({'name':'u',
                          'antiname':'u~',
                          'spin':2,
                          'color': 3,
                          'mass':'zero',
                          'width':'zero',
                          'texname':'u',
                          'antitexname':'\\overline{u}',
                          'line':'straight',
                          'charge':  2. / 3.,
                          'pdg_code': 2,
                          'propagating':True,
                          'is_part':False,
                          'self_antipart':False})
            
            antid = MG.Particle({'name':'d',
                          'antiname':'d~',
                          'spin':2,
                          'color':3,
                          'mass':'zero',
                          'width':'zero',
                          'texname':'d',
                          'antitexname':'\\overline{d}',
                          'line':'straight',
                          'charge':-1. / 3.,
                          'pdg_code':1,
                          'is_part': False,
                          'propagating':True,
                          'self_antipart':False})
            
            antit = MG.Particle({'name':'t',
                          'antiname':'t~',
                          'spin':2,
                          'color':3,
                          'mass':'tmass',
                          'width':'twidth',
                          'texname':'t',
                          'antitexname':'\\overline{t}',
                          'line':'straight',
                          'charge':2. / 3.,
                          'pdg_code':6,
                          'propagating':True,
                          'is_part': False,
                          'self_antipart':False})
            
            myinterlist.append(MG.Interaction({\
                              'id':1,\
                              'particles': MG.ParticleList(\
                                                    [mypartlist[1], \
                                                     antid, \
                                                     mypartlist[2]]),
                              'color': [color.ColorString([color.T(2, 0, 1)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'GQQ'},
                              'orders':{'QCD':1}}))    
            
            myinterlist.append(MG.Interaction({\
                              'id':2,\
                              'particles': MG.ParticleList(\
                                                    [mypartlist[0], \
                                                     antiu, \
                                                     mypartlist[2]]),
                              'color': [color.ColorString([color.T(2,0,1)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'GQQ'},
                              'orders':{'QCD':1}}))

            myinterlist.append(MG.Interaction({\
                              'id':5,\
                              'particles': MG.ParticleList(\
                                                    [mypartlist[4], \
                                                     antit, \
                                                     mypartlist[2]]),
                              'color': [color.ColorString([color.T(2, 0, 1)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'GQQ'},
                              'orders':{'QCD':1}}))
            
            myinterlist.append(MG.Interaction({\
                              'id':3,\
                              'particles': MG.ParticleList(\
                                                    [mypartlist[2]] *3 \
                                                     ),
                              'color': [color.ColorString([color.f(0, 1, 2)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'GQQ'},
                              'orders':{'QCD':1}}))
            
            myinterlist.append(MG.Interaction({\
                              'id':4,\
                              'particles': MG.ParticleList([mypartlist[1], \
                                                     antid, \
                                                     mypartlist[3]]
                                                     ),
                              'color': [color.ColorString([color.T(0,1)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'ADD'},
                              'orders':{'QED':1}}))

            myinterlist.append(MG.Interaction({\
                              'id':6,\
                              'particles': MG.ParticleList(\
                                                    [mypartlist[0], \
                                                     antiu, \
                                                     mypartlist[3]]),
                              'color': [color.ColorString([color.T(0,1)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'AUU'},
                              'orders':{'QED':1}}))
            
            expected_qcd_inter = MG.InteractionList()
                
            expected_qcd_inter.append(MG.Interaction({\
                              'id':1,\
                              'particles': MG.ParticleList(\
                                                    [mypartlist[1], \
                                                     antid, \
                                                     mypartlist[2]]),
                              'color': [color.ColorString([color.T(2, 0, 1)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'GQQ'},
                              'orders':{'QCD':1}}))
            
            expected_qcd_inter.append(MG.Interaction({\
                              'id':2,\
                              'particles': MG.ParticleList(\
                                                    [mypartlist[0], \
                                                     antiu, \
                                                     mypartlist[2]]),
                              'color': [color.ColorString([color.T(2,0,1)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'GQQ'},
                              'orders':{'QCD':1}}))
            
            expected_qcd_inter.append(MG.Interaction({\
                              'id':3,\
                              'particles': MG.ParticleList(\
                                                    [mypartlist[2]] *3 \
                                                     ),
                              'color': [color.ColorString([color.f(0, 1, 2)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'GQQ'},
                              'orders':{'QCD':1}}))
            expected_qcd_inter.append(MG.Interaction({\
                              'id':5,\
                              'particles': MG.ParticleList(\
                                                    [mypartlist[4], \
                                                     antit, \
                                                     mypartlist[2]]),
                              'color': [color.ColorString([color.T(2, 0, 1)])],
                              'lorentz':['L1'],
                              'couplings':{(0, 0):'GQQ'},
                              'orders':{'QCD':1}}))
            
            expected_qcd_inter.sort()

            model = MG.Model()
            model.set('particles', mypartlist)
            model.set('interactions', myinterlist)

            TestFKSCommon.expected_qcd_inter = expected_qcd_inter
            TestFKSCommon.model = model

    def test_sort_fksleglist(self):
        """tests the correct sorting of a fks_leglist"""
        input_pdgs = [ [1,1,21,1,1], [21,1,-1,1,1], [1,21,-1,1,1], [1,2,21,2,1],
                       [1,-2,-2,21,1], [2,21,21,2,21] ]
        sorted_pdgs = [ [1,1,1,1,21], [21,1,1,1,-1], [1,21,1,1,-1], [1,2,1,2,21],
                       [1,-2,1,-2,21], [2,21,2,21,21]]
        for input,goal in zip(input_pdgs, sorted_pdgs):
            leglist = fks_common.to_fks_legs(
                    MG.LegList([MG.Leg({'id': id, 'state': i not in [0,1]})\
                            for i, id in enumerate(input)]), self.model)
            leglist.sort()
            self.assertEqual([l['id'] for l in leglist], goal)
            self.assertEqual([l['state'] for l in leglist], [False, False, True, True, True])

    
    def test_split_leg(self):
        """tests the correct splitting of a leg into two partons"""
        leg_list = []
        parts_list = []
        res_list = []
        leg_list.append( fks_common.FKSLeg({'id' : 21, 
                                 'state' : True, 
                                 'number' : 5}))
        parts_list.append([MG.Particle({'name':'u',
                  'antiname':'u~',
                  'spin':2,
                  'color':3,
                  'mass':'zero',
                  'width':'zero',
                  'texname':'u',
                  'antitexname':'\\overline{u}',
                  'line':'straight',
                  'charge':2. / 3.,
                  'pdg_code':2,
                  'propagating':True,
                  'is_part': True,
                  'self_antipart':False}),
                  MG.Particle({'name':'d',
                  'antiname':'d~',
                  'spin':2,
                  'color':3,
                  'mass':'zero',
                  'width':'zero',
                  'texname':'u',
                  'antitexname':'\\overline{u}',
                  'line':'straight',
                  'charge':-1. / 3.,
                  'pdg_code':1,
                  'propagating':True,
                  'is_part': False,
                  'self_antipart':False})
                           ])
        res_list.append([[fks_common.FKSLeg({'id' : 2, 
                                 'state' : True,
                                 'color' : 3,
                                 'spin' : 2,
                                 'massless' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : -1, 
                                 'state' : True,
                                 'color' : -3,
                                 'spin' : 2,
                                 'massless' : True,
                                 'fks' : 'i'})]]
                        )
        
        leg_list.append( fks_common.FKSLeg({'id' : 21, 
                                 'state' : False, 
                                 'number' : 5}))
        parts_list.append([MG.Particle({'name':'u',
                  'antiname':'u~',
                  'spin':2,
                  'color':3,
                  'mass':'zero',
                  'width':'zero',
                  'texname':'u',
                  'antitexname':'\\overline{u}',
                  'line':'straight',
                  'charge':2. / 3.,
                  'pdg_code':2,
                  'propagating':True,
                  'is_part': True,
                  'self_antipart':False}),
                  MG.Particle({'name':'d',
                  'antiname':'d~',
                  'spin':2,
                  'color':3,
                  'mass':'zero',
                  'width':'zero',
                  'texname':'u',
                  'antitexname':'\\overline{u}',
                  'line':'straight',
                  'charge':-1. / 3.,
                  'pdg_code':1,
                  'propagating':True,
                  'is_part': False,
                  'self_antipart':False})
                           ])
        res_list.append([
                        [fks_common.FKSLeg({'id' : 2, 
                                 'state' : False,
                                 'color' : 3,
                                 'spin' : 2,
                                 'massless' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 1, 
                                 'state' : True,
                                 'color' : 3,
                                 'spin' : 2,
                                 'massless' : True,
                                 'fks' : 'i'})],
                        [fks_common.FKSLeg({'id' : -1, 
                                 'state' : False,
                                 'color' : -3,
                                 'spin' : 2,
                                 'massless' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : -2, 
                                 'state' : True,
                                 'color' : -3,
                                 'spin' : 2,
                                 'massless' : True,
                                 'fks' : 'i'})]
                        ]
                        )
        
        leg_list.append( fks_common.FKSLeg({'id' : 21, 
                                 'state' : False, 
                                 'number' : 5}))
        parts_list.append([MG.Particle({'name':'g',
                      'antiname':'g',
                      'spin':3,
                      'color':8,
                      'mass':'zero',
                      'width':'zero',
                      'texname':'g',
                      'antitexname':'g',
                      'line':'curly',
                      'charge':0.,
                      'pdg_code':21,
                      'propagating':True,
                      'is_part':True,
                      'self_antipart':True}),
                      MG.Particle({'name':'g',
                      'antiname':'g',
                      'spin':3,
                      'color':8,
                      'mass':'zero',
                      'width':'zero',
                      'texname':'g',
                      'antitexname':'g',
                      'line':'curly',
                      'charge':0.,
                      'pdg_code':21,
                      'propagating':True,
                      'is_part':True,
                      'self_antipart':True})
                      ])
        res_list.append([
                        [fks_common.FKSLeg({'id' : 21, 
                                 'state' : False,
                                 'color' : 8,
                                 'spin' : 3,
                                 'massless' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'color' : 8,
                                 'spin' : 3,
                                 'massless' : True,
                                 'fks' : 'i'})]])
        
        for leg, parts, res in zip(leg_list, parts_list, res_list):
            self.assertEqual(sorted(res), fks_common.split_leg(leg,parts,self.model) ) 
    
    def test_find_splittings(self):
        """tests if the correct splittings are found by the find_splitting function
        also ij_final is automatically tested here"""
        leg_list = []
        res_list = []
        
        #INITIAL STATE SPLITTINGS
        # u to u>g u or g>u~u
        leg_list.append( MG.Leg({'id' : 2, 
                                 'state' : False, 
                                 'number' : 5}))
        res_list.append([fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 2, 
                                 'state' : False,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model),
                        fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 21, 
                                 'state' : False,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : -2, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model)
                                 ])
        # g to g>gg or g>uu~ or g>u~u or g>dd~ or g>d~d
        leg_list.append( MG.Leg({'id' : 21, 
                                 'state' : False, 
                                 'number' : 5}))
        res_list.append([fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 21, 
                                 'state' : False,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model),
                        fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 1, 
                                 'state' : False,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 1, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model),
                        fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : -1, 
                                 'state' : False,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : -1, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model),
                        fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 2, 
                                 'state' : False,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 2, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model),
                        fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : -2, 
                                 'state' : False,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : -2, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model)
                                 ]
                                 )

        #FINAL STATE SPLITTINGS
        #u to ug
        leg_list.append( MG.Leg({'id' : 2, 
                                 'state' : True, 
                                 'number' : 5}))
        res_list.append([fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 2, 
                                 'state' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model) ])
        #d to dg
        leg_list.append( MG.Leg({'id' : 1, 
                                 'state' : True, 
                                 'number' : 5}))
        res_list.append([fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 1, 
                                 'state' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model) ])
        #t to tg
        leg_list.append( MG.Leg({'id' : 6, 
                                 'state' : True, 
                                 'number' : 5}))
        res_list.append([fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 6, 
                                 'state' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model) ])

        #u~ to ug
        leg_list.append( MG.Leg({'id' : -2, 
                                 'state' : True, 
                                 'number' : 5}))
        res_list.append([fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : -2, 
                                 'state' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model) ])
        #d~ to dg
        leg_list.append( MG.Leg({'id' : -1, 
                                 'state' : True, 
                                 'number' : 5}))
        res_list.append([fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : -1, 
                                 'state' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model) ])
        #t~ to tg
        leg_list.append( MG.Leg({'id' : -6, 
                                 'state' : True, 
                                 'number' : 5}))
        res_list.append([fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : -6, 
                                 'state' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model) ])

        #g > uu~ or dd~
        leg_list.append( MG.Leg({'id' : 21, 
                                 'state' : True, 
                                 'number' : 5}))
        res_list.append([fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : 21, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model), 
                        fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 1, 
                                 'state' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : -1, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model),
                        fks_common.to_fks_legs(
                        [fks_common.FKSLeg({'id' : 2, 
                                 'state' : True,
                                 'fks' : 'j'}),
                        fks_common.FKSLeg({'id' : -2, 
                                 'state' : True,
                                 'fks' : 'i'})], self.model)
                        ])

        for leg, res in zip (leg_list, res_list):    
            self.assertEqual(res, 
                             fks_common.find_splittings(leg, self.model, {}) )   
    
    def test_insert_legs(self):
        """test the correct implementation of the fks_common function"""
        legs = []
        splittings = []
        res_leglists = []
        
        leglist_orig = [fks_common.FKSLeg({ 
                                    'id': 2,
                                    'number': 1,
                                    'state': False,
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True
                                }), \
                                fks_common.FKSLeg({ 
                                    'id': 21,
                                    'number': 2,
                                    'state': False,
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True
                                }),\
                                fks_common.FKSLeg({
                                    'id': 2,
                                    'number': 3,
                                    'state': True,
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True
                                }),\
                                fks_common.FKSLeg({
                                    'id': 21,
                                    'number': 4,
                                    'state': True,
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True
                                })
                                ]
        #split initial state u  
        legs.append(fks_common.FKSLeg({ 
                                    'id': 2,
                                    'number': 1,
                                    'state': False,
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True
                                }))
        splittings.append([fks_common.FKSLeg({ 
                                    'id': 2,
                                    'number': 1,
                                    'state': False,
                                    'fks' :'j',
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True
                                }),
                           fks_common.FKSLeg({ 
                                    'id': 21,
                                    'number': 3,
                                    'state': True,
                                    'fks' : 'i',
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True
                                })
                                ])
        
        res_leglists.append([fks_common.FKSLeg({ 
                                    'id': 2,
                                    'number': 1,
                                    'state': False,
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True,
                                    'fks': 'j'
                                }), \
                                fks_common.FKSLeg({ 
                                    'id': 21,
                                    'number': 2,
                                    'state': False,
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True
                                }),\
                                fks_common.FKSLeg({
                                    'id': 2,
                                    'number': 3,
                                    'state': True,
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True
                                }),\
                                fks_common.FKSLeg({
                                    'id': 21,
                                    'number': 4,
                                    'state': True,
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True,
                                    }),\
                                fks_common.FKSLeg({
                                    'id': 21,
                                    'number': 5,
                                    'state': True,
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True,
                                    'fks': 'i'
                                })])
        
        #split final state u
        legs.append(fks_common.FKSLeg({ 
                                    'id': 2,
                                    'number': 3,
                                    'state': True,
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True
                                }))
        splittings.append([fks_common.FKSLeg({ 
                                    'id': 2,
                                    'number': 3,
                                    'state': True,
                                    'fks' :'j',
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True
                                }),
                           fks_common.FKSLeg({ 
                                    'id': 21,
                                    'number': 4,
                                    'state': True,
                                    'fks' : 'i',
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True
                                })
                                ])
        
        res_leglists.append([fks_common.FKSLeg({ 
                                    'id': 2,
                                    'number': 1,
                                    'state': False,
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True,
                                }), \
                                fks_common.FKSLeg({ 
                                    'id': 21,
                                    'number': 2,
                                    'state': False,
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True
                                }),\
                                fks_common.FKSLeg({
                                    'id': 2,
                                    'number': 3,
                                    'state': True,
                                    'color': 3,
                                    'spin': 2,
                                    'massless': True,
                                    'fks': 'j'
                                }),\
                                fks_common.FKSLeg({
                                    'id': 21,
                                    'number': 4,
                                    'state': True,
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True,
                                }),\
                                fks_common.FKSLeg({
                                    'id': 21,
                                    'number': 5,
                                    'state': True,
                                    'color': 8,
                                    'spin': 3,
                                    'massless': True,
                                    'fks': 'i'
                                })])
        
        for leg, split, res in zip(legs, splittings, res_leglists):
            self.assertEqual(res, fks_common.insert_legs(leglist_orig, leg, split))
    
    
    def test_combine_ij(self):
        """tests if legs i/j are correctly combined into leg ij"""
        legs_i = []
        legs_j = []
        legs_ij = []
        #i,j final u~ u pair
        legs_i.append(MG.Leg({'id' : -2, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : 2, 'state' : True, 'number': 4}))
        legs_ij.append([MG.Leg({'id' : 21, 'state' : True , 'number' : 3})
                        ])
        #i,j final u u~ pair ->NO COMBINATION
        legs_i.append(MG.Leg({'id' : 2, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : -2, 'state' : True, 'number': 4}))
        legs_ij.append([])
        #i,j final u d~ pair ->NO COMBINATION
        legs_i.append(MG.Leg({'id' : 2, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : -1, 'state' : True, 'number': 4}))
        legs_ij.append([])
        #i,j initial/final u quark
        legs_i.append(MG.Leg({'id' : 2, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : 2, 'state' : False, 'number': 1}))
        legs_ij.append([MG.Leg({'id' : 21, 'state' : False , 'number' : 1})
                        ])
        #i,j initial/final u~ quark
        legs_i.append(MG.Leg({'id' : -2, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : -2, 'state' : False, 'number': 1}))
        legs_ij.append([MG.Leg({'id' : 21, 'state' : False , 'number' : 1})
                        ])
        #i,j initial/final u quark, i initial ->NO COMBINATION
        legs_i.append(MG.Leg({'id' : 2, 'state' : False, 'number': 3}))
        legs_j.append(MG.Leg({'id' : 2, 'state' : True, 'number': 1}))
        legs_ij.append([])
        #i, j final glu /quark
        legs_i.append(MG.Leg({'id' : 21, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : 2, 'state' : True, 'number': 4}))
        legs_ij.append([MG.Leg({'id' : 2, 'state' : True , 'number' : 3})
                        ])
        #i, j final glu /anti quark
        legs_i.append(MG.Leg({'id' : 21, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : -2, 'state' : True, 'number': 4}))
        legs_ij.append([MG.Leg({'id' : -2, 'state' : True , 'number' : 3})
                        ])
        #i, j final glu /initial quark
        legs_i.append(MG.Leg({'id' : 21, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : 2, 'state' : False, 'number': 1}))
        legs_ij.append([MG.Leg({'id' : 2, 'state' : False , 'number' : 1})
                        ])
        #i, j final glu /initial anti quark
        legs_i.append(MG.Leg({'id' : 21, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : -2, 'state' : False, 'number': 1}))
        legs_ij.append([MG.Leg({'id' : -2, 'state' : False , 'number' : 1})
                        ])
        #i, j final: j glu, i quark -> NO COMBINATION
        legs_i.append(MG.Leg({'id' : 2, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : 21, 'state' : True, 'number': 4}))
        legs_ij.append([])
        # i, j final final gluons 
        legs_i.append(MG.Leg({'id' : 21, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : 21, 'state' : True, 'number': 4}))
        legs_ij.append([MG.Leg({'id' : 21, 'state' : True , 'number' : 3})
                        ])
        # i, j final final/initial gluons 
        legs_i.append(MG.Leg({'id' : 21, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : 21, 'state' : False, 'number': 1}))
        legs_ij.append([MG.Leg({'id' : 21, 'state' : False , 'number' : 1})
                        ])
        # i, j initial gluon/final quark 
        legs_i.append(MG.Leg({'id' : 2, 'state' : True, 'number': 3}))
        legs_j.append(MG.Leg({'id' : 21, 'state' : False, 'number': 1}))
        legs_ij.append([MG.Leg({'id' : -2, 'state' : False , 'number' : 1})
                        ])
        
        dict = {}
 
        for i, j, ij in zip(legs_i, legs_j, legs_ij):
            self.assertEqual(fks_common.combine_ij(
                                    fks_common.to_fks_leg(i, self.model), 
                                    fks_common.to_fks_leg(j, self.model), 
                                    self.model, dict, 'QCD'), 
                                    fks_common.to_fks_legs(ij, self.model))
        


    def test_find_pert_particles_interactions(self):
        """test if interactions, particles and massless particles corresponding
        to the perturbative expansion are correctly extracted from the model"""
        
        dict = fks_common.find_pert_particles_interactions(self.model, 'QCD')
        res_int = self.expected_qcd_inter
        res_part = [-6,-2,-1,1,2,6,21]
        res_soft = [-2,-1,1,2,21]
        self.assertEqual(dict['pert_particles'], res_part)
        self.assertEqual(dict['soft_particles'], res_soft)
        self.assertEqual(dict['interactions'], res_int)


    def test_find_pert_particles_interactionsi_mssm(self):
        """ for the mssm, the soft_particles should be the same as for the sm"""
        dict_mssm = fks_common.find_pert_particles_interactions(\
                import_ufo.import_model('mssm'))
        dict_sm = fks_common.find_pert_particles_interactions(\
                import_ufo.import_model('mssm'))
        self.assertEqual(dict_sm['soft_particles'], dict_mssm['soft_particles'])


    def test_find_particles_interactions_no_ghosts(self):
        """tests that interactions involving ghosts are NOT returned by the
        find_particles_interactions function when using a loop model"""
        
        dict = fks_common.find_pert_particles_interactions( \
                import_ufo.import_model('loop_sm'))

        for inte  in dict['interactions']:
            self.assertTrue(not 'gh' in [p['name'] for p in inte['particles']])


    
    
    def test_to_fks_leg_s(self):
        """tests if color, massless and spin entries of a fks leg/leglist
         are correctly set"""
        leg_list = MG.LegList()
        res_list = fks_common.FKSLegList()
        leg_list.append( MG.Leg({'id' : 21, 
                                     'state' : True, 
                                     'number' : 5}))
        res_list.append( fks_common.FKSLeg({'id' : 21, 
                                     'state' : True, 
                                     'number' : 5,
                                     'massless' : True,
                                     'color' : 8,
                                     'spin' : 3})) 
        leg_list.append( MG.Leg({'id' : 6, 
                                     'state' : True, 
                                     'number' : 5}))
        res_list.append( fks_common.FKSLeg({'id' : 6, 
                                     'state' : True, 
                                     'number' : 5,
                                     'massless' : False,
                                     'color' : 3,
                                     'spin' : 2}))  
        leg_list.append( MG.Leg({'id' : -1, 
                                     'state' : True, 
                                     'number' : 5}))
        res_list.append( fks_common.FKSLeg({'id' : -1, 
                                     'state' : True, 
                                     'number' : 5,
                                     'massless' : True,
                                     'color' : -3,
                                     'spin' : 2}))  
        leg_list.append( MG.Leg({'id' : -1, 
                                     'state' : False, 
                                     'number' : 5}))
        res_list.append( fks_common.FKSLeg({'id' : -1, 
                                     'state' : False, 
                                     'number' : 5,
                                     'massless' : True,
                                     'color' : -3,
                                     'spin' : 2})) 
    
    
        self.assertEqual(fks_common.to_fks_legs(leg_list, self.model), res_list)
            
        for leg, res in zip(leg_list, res_list):
            self.assertEqual(fks_common.to_fks_leg(leg, self.model), res)                                                                                            

    def test_find_color_links(self): 
        """tests if all the correct color links are found for a given born process"""
        myleglist = MG.LegList()
        # PROCESS: u u~ > g t t~ a 
        mylegs = [{ \
        'id': 2,\
        'number': 1,\
        'state': False,\
     #   'from_group': True \
    }, \
    { \
        'id': -2,\
        'number': 2,\
        'state': False,\
        #'from_group': True\
    },\
    {\
        'id': 21,\
        'number': 3,\
        'state': True,\
      #  'from_group': True\
    },\
    {\
        'id': 6,\
        'number': 4,\
        'state': True,\
       # 'from_group': True\
    },\
    {\
        'id': -6,\
        'number': 5,\
        'state': True,\
       # 'from_group': True\
    },\
    {\
        'id': 22,\
        'number': 6,\
        'state': True,\
       # 'from_group': True\
    }
    ]

        for i in mylegs:
            myleglist.append(MG.Leg(i))   

        fkslegs = fks_common.to_fks_legs(myleglist, self.model)
        color_links = fks_common.find_color_links(fkslegs)

        links = []
        links.append([fkslegs[0], fkslegs[1]])
        links.append([fkslegs[0], fkslegs[2]])
        links.append([fkslegs[0], fkslegs[3]])
        links.append([fkslegs[0], fkslegs[4]])
        
        links.append([fkslegs[1], fkslegs[0]])
        links.append([fkslegs[1], fkslegs[2]])
        links.append([fkslegs[1], fkslegs[3]])
        links.append([fkslegs[1], fkslegs[4]])
        
        links.append([fkslegs[2], fkslegs[0]])
        links.append([fkslegs[2], fkslegs[1]])
        links.append([fkslegs[2], fkslegs[3]])
        links.append([fkslegs[2], fkslegs[4]])
        
        links.append([fkslegs[3], fkslegs[0]])
        links.append([fkslegs[3], fkslegs[1]])
        links.append([fkslegs[3], fkslegs[2]])
        links.append([fkslegs[3], fkslegs[3]])
        links.append([fkslegs[3], fkslegs[4]])
        
        links.append([fkslegs[4], fkslegs[0]])
        links.append([fkslegs[4], fkslegs[1]])
        links.append([fkslegs[4], fkslegs[2]])
        links.append([fkslegs[4], fkslegs[3]])
        links.append([fkslegs[4], fkslegs[4]])
        
        self.assertEqual(len(links), len(color_links))
        for l1, l2 in zip (links, color_links):
            self.assertEqual(l1,l2['legs'])
            
    def test_insert_color_links(self):
        """given a list of color links, tests if the insert color link works, ie 
        if a list of dictionaries is returned. Each dict has the following entries:
        --link, list of number of linked legs
        --link_basis the linked color basis
        --link_matrix the color matrix created from the original basis"""
        #test the process u u~ > d d~, link u and d
        leglist = MG.LegList([
                    MG.Leg({'id':2, 'state':False, 'number':1}),
                    MG.Leg({'id':-2, 'state':False, 'number':2}),
                    MG.Leg({'id':1, 'state':True, 'number':3}),
                    MG.Leg({'id':-1, 'state':True, 'number':4}),
                    ])
        myproc = MG.Process({'legs' : leglist,
                       'orders':{'QCD':10, 'QED':0},
                       'model': self.model,
                       'id': 1,
                       'required_s_channels':[],
                       'forbidden_s_channels':[],
                       'forbidden_particles':[],
                       'is_decay_chain': False,
                       'decay_chains': MG.ProcessList(),
                       'overall_orders': {}})
        helas = helas_objects.HelasMatrixElement(
                        diagram_generation.Amplitude(myproc))
        
        basis_orig = copy.deepcopy(helas['color_basis'])
        
        links = fks_common.find_color_links(
                                    fks_common.to_fks_legs(leglist, self.model))
        dicts = fks_common.insert_color_links(
                    helas['color_basis'],
                    helas['color_basis'].create_color_dict_list(helas['base_amplitude']),
                    links)
        #color_string for link 1-3 (dicts[1])
        linkstring = color.ColorString([
                        color.T(-1000,2,-3001), color.T(-1000,-3002,4),
                        color.T(-6000,-3001,1), color.T(-6000,3,-3002)])
        linkstring.coeff = linkstring.coeff * (-1)
        
        linkdicts = [{(0,0) : linkstring}]
        
        link_basis = color_amp.ColorBasis()
        for i, dict in enumerate(linkdicts):
            link_basis.update_color_basis(dict, i)
        
        matrix = color_amp.ColorMatrix(basis_orig, link_basis)
        
        self.assertEqual(len(dicts), 12)
        self.assertEqual(link_basis, dicts[1]['link_basis'])
        self.assertEqual(matrix, dicts[1]['link_matrix'])
        

    def test_legs_to_color_link_string(self):
        """tests if, given two fks legs, the color link between them is correctly 
        computed, i.e. if string and replacements are what they are expected to be"""
        pairs = []
        strings = []
        replacs = []
        ###MASSIVE
        #FINAL t with itself
        pairs.append([MG.Leg({'id' : 6, 'state' : True, 'number' : 5 }),
                      MG.Leg({'id' : 6, 'state' : True, 'number' : 5 })])
        replacs.append([[5, -3001]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000,-6000, 5, -3001)],
                       coeff = fractions.Fraction(1,2)))
        #FINAL anti-t with itself
        pairs.append([MG.Leg({'id' : -6, 'state' : True, 'number' : 5 }),
                      MG.Leg({'id' : -6, 'state' : True, 'number' : 5 })])
        replacs.append([[5, -3001]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000,-6000, -3001, 5)],
                       coeff = fractions.Fraction(1,2)))
        ####INITIAL-INITIAL
        #INITIAL state quark with INITIAL state quark
        pairs.append([MG.Leg({'id' : 1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : 2, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001, 1),color.T(-6000, -3002, 2)],
                       coeff = fractions.Fraction(1,1)))
        #INITIAL state quark with INITIAL state anti-quark
        pairs.append([MG.Leg({'id' : 1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : -2, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001, 1),color.T(-6000, 2,-3002)],
                       coeff = fractions.Fraction(-1,1)))
        #INITIAL state anti-quark with INITIAL state quark
        pairs.append([MG.Leg({'id' : -1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : 2, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1, -3001),color.T(-6000, -3002, 2)],
                       coeff = fractions.Fraction(-1,1)))
        #INITIAL state anti-quark with INITIAL state anti-quark
        pairs.append([MG.Leg({'id' : -1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : -2, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1,-3001),color.T(-6000, 2,-3002)],
                       coeff = fractions.Fraction(1,1)))
        #INITIAL state quark with INITIAL state gluon
        pairs.append([MG.Leg({'id' : 1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001,1),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(1,1),
                       is_imaginary = True))
        #INITIAL state anti-quark with INITIAL state gluon
        pairs.append([MG.Leg({'id' : -1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1, -3001),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(-1,1),
                       is_imaginary = True))
        #INITIAL state gluon with INITIAL state gluon
        pairs.append([MG.Leg({'id' : 21, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.f(-3001,-6000, 1),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(-1,1),
                       is_imaginary = False))
        ####FINAL-FINIAL
        #FINAL state quark with FINIAL state quark
        pairs.append([MG.Leg({'id' : 1, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : 2, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1,-3001),color.T(-6000, 2,-3002)],
                       coeff = fractions.Fraction(1,1)))
        #FINAL state quark with FINAL state anti-quark
        pairs.append([MG.Leg({'id' : 1, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : -2, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1,-3001),color.T(-6000,-3002,2)],
                       coeff = fractions.Fraction(-1,1)))
        #FINAL state anti-quark with FINAL state quark
        pairs.append([MG.Leg({'id' : -1, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : 2, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001,1),color.T(-6000, 2,-3002)],
                       coeff = fractions.Fraction(-1,1)))
        #FINAL state anti-quark with FINAL state anti-quark
        pairs.append([MG.Leg({'id' : -1, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : -2, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001,1),color.T(-6000,-3002,2)],
                       coeff = fractions.Fraction(1,1)))
        #FINAL state quark with FINAL state gluon
        pairs.append([MG.Leg({'id' : 1, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1,-3001),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(-1,1),
                       is_imaginary = True))
        #FINAL state anti-quark with FINAL state gluon
        pairs.append([MG.Leg({'id' : -1, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001,1),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(1,1),
                       is_imaginary = True))
        #FINAL state gluon with FINAL state gluon
        pairs.append([MG.Leg({'id' : 21, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.f(-3001,-6000, 1),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(-1,1),
                       is_imaginary = False))
        ###INITIAL-FINAL
        #INITIAL state quark with FINAL state quark
        pairs.append([MG.Leg({'id' : 1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : 2, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001, 1),color.T(-6000, 2,-3002)],
                       coeff = fractions.Fraction(-1,1)))
        #INITIAL state quark with FINAL state anti-quark
        pairs.append([MG.Leg({'id' : 1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : -2, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001, 1),color.T(-6000, -3002,2)],
                       coeff = fractions.Fraction(1,1)))
        #INITIAL state anti-quark with FINAL state quark
        pairs.append([MG.Leg({'id' : -1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : 2, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1, -3001),color.T(-6000, 2,-3002)],
                       coeff = fractions.Fraction(1,1)))
        #INITIAL state anti-quark with FINAL state anti-quark
        pairs.append([MG.Leg({'id' : -1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : -2, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1,-3001),color.T(-6000, -3002,2)],
                       coeff = fractions.Fraction(-1,1)))
        #INITIAL state quark with FINAL state gluon
        pairs.append([MG.Leg({'id' : 1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001,1),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(1,1),
                       is_imaginary = True))
        #INITIAL state anti-quark with FINAL state gluon
        pairs.append([MG.Leg({'id' : -1, 'state' : False, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : True, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1, -3001),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(-1,1),
                       is_imaginary = True))
        #FINAL state quark with INITIAL state gluon
        pairs.append([MG.Leg({'id' : 1, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, 1,-3001),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(-1,1),
                       is_imaginary = True))
        #FINAL state anti-quark with INITIAL state gluon
        pairs.append([MG.Leg({'id' : -1, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.T(-6000, -3001,1),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(1,1),
                       is_imaginary = True))
        #FINAL state gluon with INITIAL state gluon
        pairs.append([MG.Leg({'id' : 21, 'state' : True, 'number' : 1 }),
                      MG.Leg({'id' : 21, 'state' : False, 'number' : 2 })])
        replacs.append([[1, -3001], [2, -3002]])
        strings.append(color.ColorString(init_list = [
                       color.f(-3001,-6000, 1),color.f(-3002,-6000, 2)],
                       coeff = fractions.Fraction(-1,1),
                       is_imaginary = False))
        
        for pair, string, replac in zip(pairs, strings, replacs):
            dict = fks_common.legs_to_color_link_string(\
                fks_common.to_fks_leg(pair[0],self.model), 
                fks_common.to_fks_leg(pair[1],self.model)
                                                    )
            self.assertEqual(string, dict['string'])
            self.assertEqual(replac, dict['replacements'])
            
        
    def test_find_orders(self):
        """tests if the orders of a given amplitude are correctly returned"""

        myleglist = MG.LegList()
        # PROCESS: u u~ > g t t~ a 
        mylegs = [{ \
        'id': 2,\
        'number': 1,\
        'state': False,\
     #   'from_group': True \
    }, \
    { \
        'id': -2,\
        'number': 2,\
        'state': False,\
        #'from_group': True\
    },\
    {\
        'id': 21,\
        'number': 3,\
        'state': True,\
      #  'from_group': True\
    },\
    {\
        'id': 6,\
        'number': 4,\
        'state': True,\
       # 'from_group': True\
    },\
    {\
        'id': -6,\
        'number': 5,\
        'state': True,\
       # 'from_group': True\
    },\
    {\
        'id': 22,\
        'number': 6,\
        'state': True,\
       # 'from_group': True\
    }
    ]

        for i in mylegs:
            myleglist.append(MG.Leg(i))   

        amp = diagram_generation.Amplitude(\
                        MG.Process({'legs' : myleglist,
                       'orders':{'QCD':10, 'QED':1},
                       'model': self.model,
                       'id': 1,
                       'required_s_channels':[],
                       'forbidden_s_channels':[],
                       'forbidden_particles':[],
                       'is_decay_chain': False,
                       'decay_chains': MG.ProcessList(),
                       'overall_orders': {}}) )
        self.assertEqual(fks_common.find_orders(amp), \
                        {'QED':1, 'QCD':3, 'WEIGHTED':5})


#===============================================================================
# TestLinkRBConfHEFT
#===============================================================================
class TestLinkRBConfHEFT(unittest.TestCase):
    """Class to test the link_rb_conf function for various processes, using SM
    (only processes with 3 point interactions)"""

    def setUp(self):
        if not hasattr(self, 'base_model'):
            TestLinkRBConfHEFT.base_model = import_ufo.import_model('heft')


    def test_link_gghg_ggh(self):
        """tests that the real emission process gg>hg and born process gg>h are
        correctly linked"""

        myleglist_r = fks_common.FKSLegList()
        myleglist_r.append(fks_common.FKSLeg({'id':21, 'state':False}))
        myleglist_r.append(fks_common.FKSLeg({'id':21, 'state':False}))
        myleglist_r.append(fks_common.FKSLeg({'id':25, 'state':True}))
        myleglist_r.append(fks_common.FKSLeg({'id':21, 'state':True}))
        realproc = MG.Process({'legs':myleglist_r,
                                       'model':self.base_model,
                                       'orders':{'QCD':1, 'QED':0, 'HIG':1}})
        realamp= diagram_generation.Amplitude(realproc)


        myleglist_b = fks_common.FKSLegList()
        myleglist_b.append(fks_common.FKSLeg({'id':21, 'state':False}))
        myleglist_b.append(fks_common.FKSLeg({'id':21, 'state':False}))
        myleglist_b.append(fks_common.FKSLeg({'id':25, 'state':True}))
        bornproc = MG.Process({'legs':myleglist_b,
                                       'model':self.base_model,
                                       'orders':{'QCD':0, 'QED':0, 'HIG':1}})
        bornamp= diagram_generation.Amplitude(bornproc)

        ij_conf = [ {'i': 4, 'j':1, 'ij':1}, 
                    {'i': 4, 'j':2, 'ij':2}]

        links =[[{'born_conf':0, 'real_conf':3}],
                [{'born_conf':0, 'real_conf':2}] ]

        for conf, link in zip(ij_conf, links):
            self.assertEqual(link, fks_common.link_rb_conf(bornamp, realamp, conf['i'], conf['j'], conf['ij']))

    def test_link_gghgg_gghg(self):
        """tests that the real emission process gg>hgg and born process gg>hg are
        correctly linked"""

        myleglist_r = fks_common.FKSLegList()
        myleglist_r.append(fks_common.FKSLeg({'id':21, 'state':False}))
        myleglist_r.append(fks_common.FKSLeg({'id':21, 'state':False}))
        myleglist_r.append(fks_common.FKSLeg({'id':25, 'state':True}))
        myleglist_r.append(fks_common.FKSLeg({'id':21, 'state':True}))
        myleglist_r.append(fks_common.FKSLeg({'id':21, 'state':True}))
        realproc = MG.Process({'legs':myleglist_r,
                                       'model':self.base_model,
                                       'orders':{'QCD':2, 'QED':0, 'HIG':1}})
        realamp= diagram_generation.Amplitude(realproc)


        myleglist_b = fks_common.FKSLegList()
        myleglist_b.append(fks_common.FKSLeg({'id':21, 'state':False}))
        myleglist_b.append(fks_common.FKSLeg({'id':21, 'state':False}))
        myleglist_b.append(fks_common.FKSLeg({'id':25, 'state':True}))
        myleglist_b.append(fks_common.FKSLeg({'id':21, 'state':True}))
        bornproc = MG.Process({'legs':myleglist_b,
                                       'model':self.base_model,
                                       'orders':{'QCD':1, 'QED':0, 'HIG':1}})
        bornamp= diagram_generation.Amplitude(bornproc)

#        for i, diag in enumerate(bornamp.get('diagrams')):
#            print "B",i , diag.nice_string()
#        for i, diag in enumerate(realamp.get('diagrams')):
#            print "R",i , diag.nice_string()


        ij_conf = [ {'i': 4, 'j':1, 'ij':1}, 
                    {'i': 4, 'j':2, 'ij':2}, 
                    {'i': 5, 'j':1, 'ij':1}, 
                    {'i': 5, 'j':2, 'ij':2}, 
                    {'i': 5, 'j':4, 'ij':4} ]

        links =[[{'born_conf':1, 'real_conf':11},
                 {'born_conf':2, 'real_conf':10},
                 {'born_conf':3, 'real_conf':9} ],
                [{'born_conf':1, 'real_conf':18},
                 {'born_conf':2, 'real_conf':5},
                 {'born_conf':3, 'real_conf':14}],
                [{'born_conf':1, 'real_conf':15},
                 {'born_conf':2, 'real_conf':14},
                 {'born_conf':3, 'real_conf':13}],
                [{'born_conf':1, 'real_conf':19},
                 {'born_conf':2, 'real_conf':6},
                 {'born_conf':3, 'real_conf':10}],
                [{'born_conf':1, 'real_conf':3},
                 {'born_conf':2, 'real_conf':7},
                 {'born_conf':3, 'real_conf':17}] ]

        for conf, link in zip(ij_conf, links):
            self.assertEqual(link, fks_common.link_rb_conf(bornamp, realamp, conf['i'], conf['j'], conf['ij']))

    def test_sort_proc(self):
        """tests that the legs of a process are correctly sorted"""
        model = import_ufo.import_model('sm')

# sorted leglist for e+ e- > u u~ g
        myleglist_s = MG.LegList()
        myleglist_s.append(MG.Leg({'id':-11, 'state':False}))
        myleglist_s.append(MG.Leg({'id':11, 'state':False}))
        myleglist_s.append(MG.Leg({'id':2, 'state':True}))
        myleglist_s.append(MG.Leg({'id':-2, 'state':True}))
        myleglist_s.append(MG.Leg({'id':21, 'state':True}))

# unsorted leglist: e+ e- > u g u~
        myleglist_u = MG.LegList()
        myleglist_u.append(MG.Leg({'id':-11, 'state':False}))
        myleglist_u.append(MG.Leg({'id':11, 'state':False}))
        myleglist_u.append(MG.Leg({'id':2, 'state':True}))
        myleglist_u.append(MG.Leg({'id':21, 'state':True}))
        myleglist_u.append(MG.Leg({'id':-2, 'state':True}))

# define (un)sorted process:
        proc_s = MG.Process({'model':model, 'legs':myleglist_s,\
                             'orders':{'QED':2, 'QCD':1}})
        proc_u = MG.Process({'model':model, 'legs':myleglist_u,\
                             'orders':{'QED':2, 'QCD':1}})
        
        res = fks_common.sort_proc(proc_u)

        self.assertEqual(res, proc_s)


#===============================================================================
# TestLinkRBConfSM
#===============================================================================
class TestLinkRBConfSM(unittest.TestCase):
    """Class to test the link_rb_conf function for various processes, using SM
    (only processes with 3 point interactions)"""

    def setUp(self):
        if not hasattr(self, 'base_model'):
            TestLinkRBConfSM.base_model = import_ufo.import_model('sm')

    def test_link_uuddg_uudd(self):
        """tests that the real emission process uu~>dd~g and born process uu~>dd~ are
        correctly linked"""


        myleglist_r = MG.LegList()
        myleglist_r.append(MG.Leg({'id':2, 'state':False}))
        myleglist_r.append(MG.Leg({'id':-2, 'state':False}))
        myleglist_r.append(MG.Leg({'id':1, 'state':True}))
        myleglist_r.append(MG.Leg({'id':-1, 'state':True}))
        myleglist_r.append(MG.Leg({'id':21, 'state':True}))
        realproc = MG.Process({'legs':myleglist_r,
                                       'model':self.base_model,
                                       'orders':{'QCD':3, 'QED':0}})
        realamp= diagram_generation.Amplitude(realproc)


        myleglist_b = MG.LegList()
        myleglist_b.append(MG.Leg({'id':2, 'state':False}))
        myleglist_b.append(MG.Leg({'id':-2, 'state':False}))
        myleglist_b.append(MG.Leg({'id':1, 'state':True}))
        myleglist_b.append(MG.Leg({'id':-1, 'state':True}))
        bornproc = MG.Process({'legs':myleglist_b,
                                       'model':self.base_model,
                                       'orders':{'QCD':2, 'QED':0}})
        bornamp= diagram_generation.Amplitude(bornproc)

        ij_conf = [ {'i': 5, 'j':1, 'ij':1}, 
                    {'i': 5, 'j':2, 'ij':2},
                    {'i': 5, 'j':3, 'ij':3},
                    {'i': 5, 'j':4, 'ij':4}]

        links =[[{'born_conf':0, 'real_conf':3}],
                [{'born_conf':0, 'real_conf':4}],
                [{'born_conf':0, 'real_conf':1}],
                [{'born_conf':0, 'real_conf':2}] ]

        for conf, link in zip(ij_conf, links):
            self.assertEqual(link, fks_common.link_rb_conf(bornamp, realamp, conf['i'], conf['j'], conf['ij']))


    def test_link_uuddg_uugg(self):
        """tests that the real emission process uu~>dd~g and born process uu~>gg are
        correctly linked"""


        myleglist_r = fks_common.FKSLegList()
        myleglist_r.append(fks_common.FKSLeg({'id':2, 'state':False}))
        myleglist_r.append(fks_common.FKSLeg({'id':-2, 'state':False}))
        myleglist_r.append(fks_common.FKSLeg({'id':1, 'state':True}))
        myleglist_r.append(fks_common.FKSLeg({'id':-1, 'state':True}))
        myleglist_r.append(fks_common.FKSLeg({'id':21, 'state':True}))
        realproc = MG.Process({'legs':myleglist_r,
                                       'model':self.base_model,
                                       'orders':{'QCD':3, 'QED':0}})
        realamp= diagram_generation.Amplitude(realproc)


        myleglist_b = fks_common.FKSLegList()
        myleglist_b.append(fks_common.FKSLeg({'id':2, 'state':False}))
        myleglist_b.append(fks_common.FKSLeg({'id':-2, 'state':False}))
        myleglist_b.append(fks_common.FKSLeg({'id':21, 'state':True}))
        myleglist_b.append(fks_common.FKSLeg({'id':21, 'state':True}))
        bornproc = MG.Process({'legs':myleglist_b,
                                       'model':self.base_model,
                                       'orders':{'QCD':2, 'QED':0}})
        bornamp= diagram_generation.Amplitude(bornproc)


        ij_conf = [ {'i': 4, 'j':3, 'ij':3}, 
                    {'i': 4, 'j':3, 'ij':4}]

        links =[[{'born_conf':0, 'real_conf':0},
                 {'born_conf':1, 'real_conf':4},
                 {'born_conf':2, 'real_conf':3}],
                [{'born_conf':0, 'real_conf':0},
                 {'born_conf':1, 'real_conf':3},
                 {'born_conf':2, 'real_conf':4}] ]

        for conf, link in zip(ij_conf, links):
            self.assertEqual(link, fks_common.link_rb_conf(bornamp, realamp, conf['i'], conf['j'], conf['ij']))


    def test_link_uuuug_guug(self):
        """tests that the real emission process uu>uug and born process gu>ug are
        correctly linked"""


        myleglist_r = MG.LegList()
        myleglist_r.append(MG.Leg({'id':2, 'state':False}))
        myleglist_r.append(MG.Leg({'id':2, 'state':False}))
        myleglist_r.append(MG.Leg({'id':2, 'state':True}))
        myleglist_r.append(MG.Leg({'id':2, 'state':True}))
        myleglist_r.append(MG.Leg({'id':21, 'state':True}))
        realproc = MG.Process({'legs':myleglist_r,
                                       'model':self.base_model,
                                       'orders':{'QCD':3, 'QED':0}})
        realamp= diagram_generation.Amplitude(realproc)


        myleglist_b = MG.LegList()
        myleglist_b.append(MG.Leg({'id':21, 'state':False}))
        myleglist_b.append(MG.Leg({'id':2, 'state':False}))
        myleglist_b.append(MG.Leg({'id':2, 'state':True}))
        myleglist_b.append(MG.Leg({'id':21, 'state':True}))
        bornproc = MG.Process({'legs':myleglist_b,
                                       'model':self.base_model,
                                       'orders':{'QCD':2, 'QED':0}})
        bornamp= diagram_generation.Amplitude(bornproc)


        ij_conf = [ {'i': 3, 'j':1, 'ij':1}, 
                    {'i': 4, 'j':1, 'ij':1}]

        links =[[{'born_conf':0, 'real_conf':2},
                 {'born_conf':1, 'real_conf':1},
                 {'born_conf':2, 'real_conf':0}],
                [{'born_conf':0, 'real_conf':5},
                 {'born_conf':1, 'real_conf':4},
                 {'born_conf':2, 'real_conf':3}] ]

        for conf, link in zip(ij_conf, links):
            self.assertEqual(link, fks_common.link_rb_conf(bornamp, realamp, conf['i'], conf['j'], conf['ij']))


    def test_link_butdg_butd(self):
        """tests that the real emission process bu>tdg and born process bu>td are
        correctly linked"""


        myleglist_r = MG.LegList()
        myleglist_r.append(MG.Leg({'id':5, 'state':False}))
        myleglist_r.append(MG.Leg({'id':2, 'state':False}))
        myleglist_r.append(MG.Leg({'id':6, 'state':True}))
        myleglist_r.append(MG.Leg({'id':1, 'state':True}))
        myleglist_r.append(MG.Leg({'id':21, 'state':True}))
        realproc = MG.Process({'legs':myleglist_r,
                                       'model':self.base_model,
                                       'orders':{'QCD':1, 'QED':2}})
        realamp= diagram_generation.Amplitude(realproc)


        myleglist_b = MG.LegList()
        myleglist_b.append(MG.Leg({'id':5, 'state':False}))
        myleglist_b.append(MG.Leg({'id':2, 'state':False}))
        myleglist_b.append(MG.Leg({'id':6, 'state':True}))
        myleglist_b.append(MG.Leg({'id':1, 'state':True}))
        bornproc = MG.Process({'legs':myleglist_b,
                                       'model':self.base_model,
                                       'orders':{'QCD':0, 'QED':2}})
        bornamp= diagram_generation.Amplitude(bornproc)


        ij_conf = [ {'i': 5, 'j':1, 'ij':1}, 
                    {'i': 5, 'j':2, 'ij':2}, 
                    {'i': 5, 'j':3, 'ij':3}, 
                    {'i': 5, 'j':4, 'ij':4}]

        links =[[{'born_conf':0, 'real_conf':2}],
                [{'born_conf':0, 'real_conf':0}],
                [{'born_conf':0, 'real_conf':3}],
                [{'born_conf':0, 'real_conf':1}] ]

        for conf, link in zip(ij_conf, links):
            self.assertEqual(link, fks_common.link_rb_conf(bornamp, realamp, conf['i'], conf['j'], conf['ij']))


    def test_link_gutdb_butd(self):
        """tests that the real emission process gu>tdb~ and born process bu>td are
        correctly linked"""


        myleglist_r = MG.LegList()
        myleglist_r.append(MG.Leg({'id':21, 'state':False}))
        myleglist_r.append(MG.Leg({'id':2, 'state':False}))
        myleglist_r.append(MG.Leg({'id':6, 'state':True}))
        myleglist_r.append(MG.Leg({'id':1, 'state':True}))
        myleglist_r.append(MG.Leg({'id':-5, 'state':True}))
        realproc = MG.Process({'legs':myleglist_r,
                                       'model':self.base_model,
                                       'orders':{'QCD':1, 'QED':2}})
        realamp= diagram_generation.Amplitude(realproc)


        myleglist_b = MG.LegList()
        myleglist_b.append(MG.Leg({'id':5, 'state':False}))
        myleglist_b.append(MG.Leg({'id':2, 'state':False}))
        myleglist_b.append(MG.Leg({'id':6, 'state':True}))
        myleglist_b.append(MG.Leg({'id':1, 'state':True}))
        bornproc = MG.Process({'legs':myleglist_b,
                                       'model':self.base_model,
                                       'orders':{'QCD':0, 'QED':2}})
        bornamp= diagram_generation.Amplitude(bornproc)

        ij_conf = [ {'i': 5, 'j':1, 'ij':1}] 

        links =[[{'born_conf':0, 'real_conf':3}]]

        for conf, link in zip(ij_conf, links):
            self.assertEqual(link, fks_common.link_rb_conf(bornamp, realamp, conf['i'], conf['j'], conf['ij']))


#===============================================================================
# TestFKSDiagramTag
#===============================================================================
class TestFKSDiagramTag(unittest.TestCase):
    """Test class for the FKSDiagramTag class"""


    def setUp(self):
        if not hasattr(self, 'base_model'):
            TestFKSDiagramTag.base_model = import_ufo.import_model('sm')
    
    def test_diagram_tag_gg_ggg(self):
        """Test the diagram tag for gg > ggg"""

        myleglist = MG.LegList()

        myleglist.append(MG.Leg({'id':21,
                                           'state':False}))
        myleglist.append(MG.Leg({'id':21,
                                           'state':False}))
        myleglist.append(MG.Leg({'id':21,
                                           'state':True}))
        myleglist.append(MG.Leg({'id':21,
                                           'state':True}))
        myleglist.append(MG.Leg({'id':21,
                                           'state':True}))

        myproc = MG.Process({'legs':myleglist,
                                       'model':self.base_model})

        myamplitude = diagram_generation.Amplitude(myproc)

        tags = []
        permutations = []
        diagram_classes = []
        for idiag, diagram in enumerate(myamplitude.get('diagrams')):
            tag = fks_common.FKSDiagramTag(diagram)
            try:
                ind = tags.index(tag)
            except:
                diagram_classes.append([idiag + 1])
                permutations.append([tag.get_external_numbers()])
                tags.append(tag)
            else:
                diagram_classes[ind].append(idiag + 1)
                permutations[ind].append(tag.get_external_numbers())

        permutations = [[fks_common.FKSDiagramTag.reorder_permutation(p, perms[0])\
                         for p in perms] for perms in permutations]        

        # for the fks tags all diagrams should be different, i.e. no final state
        # permutation should be done
        goal_classes =  [[i+1] for i in range(25)]
        goal_perms = [[[0,1,2,3,4]]] *25

        for i in range(len(diagram_classes)):
            self.assertEqual(diagram_classes[i], goal_classes[i])
            self.assertEqual(permutations[i], goal_perms[i])

    def test_diagram_tag_uu_uug(self):
        """Test diagram tag for uu>uug"""

        myleglist = MG.LegList()

        myleglist.append(MG.Leg({'id':2,
                                           'state':False}))
        myleglist.append(MG.Leg({'id':2,
                                           'state':False}))
        myleglist.append(MG.Leg({'id':2,
                                           'state':True}))
        myleglist.append(MG.Leg({'id':2,
                                           'state':True}))
        myleglist.append(MG.Leg({'id':21,
                                           'state':True}))

        myproc = MG.Process({'legs':myleglist,
                                       'model':self.base_model})

        myamplitude = diagram_generation.Amplitude(myproc)

        tags = []
        permutations = []
        diagram_classes = []
        for idiag, diagram in enumerate(myamplitude.get('diagrams')):
            tag = fks_common.FKSDiagramTag(diagram)
            try:
                ind = tags.index(tag)
            except:
                diagram_classes.append([idiag + 1])
                permutations.append([tag.get_external_numbers()])
                tags.append(tag)
            else:
                diagram_classes[ind].append(idiag + 1)
                permutations[ind].append(tag.get_external_numbers())

        permutations = [[fks_common.FKSDiagramTag.reorder_permutation(p, perms[0])\
                         for p in perms] for perms in permutations]        

        goal_classes =  [[i+1] for i in range(26)]
        goal_perms = [[[0,1,2,3,4]]] *26

        for i in range(len(diagram_classes)):
            self.assertEqual(diagram_classes[i], goal_classes[i])
            self.assertEqual(permutations[i], goal_perms[i])


    def test_reorder_permutation(self):
        """Test the reorder_permutation routine"""

        perm1 = [2,3,4,5,1]
        perm2 = [3,5,2,1,4]
        goal = [3,2,4,1,0]

        self.assertEqual(fks_common.FKSDiagramTag.reorder_permutation(\
            perm1, perm2), goal)



