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

"""Unit test library for the various base objects of the core library"""

import copy
import unittest

import madgraph.core.base_objects as base_objects
import madgraph.core.diagram_generation as diagram_generation

#===============================================================================
# DiagramGenerationTest
#===============================================================================
class DiagramGenerationTest(unittest.TestCase):
    """Test class for the diagram generation"""

    mypartlist = base_objects.ParticleList()
    myinterlist = base_objects.InteractionList()

    ref_dict_to0 = {}
    ref_dict_to1 = {}

    def setUp(self):

        self.mypartlist.append(base_objects.Particle({'name':'g',
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

        self.mypartlist.append(base_objects.Particle({'name':'u',
                      'antiname':'u~',
                      'spin':2,
                      'color':3,
                      'mass':'zero',
                      'width':'zero',
                      'texname':'u',
                      'antitexname':'\bar u',
                      'line':'straight',
                      'charge':2. / 3.,
                      'pdg_code':2,
                      'propagating':True,
                      'is_part':True,
                      'self_antipart':False}))
        antiu = copy.copy(self.mypartlist[1])
        antiu.set('is_part', False)

        self.mypartlist.append(base_objects.Particle({'name':'d',
                      'antiname':'d~',
                      'spin':2,
                      'color':3,
                      'mass':'zero',
                      'width':'zero',
                      'texname':'d',
                      'antitexname':'\bar d',
                      'line':'straight',
                      'charge':-1. / 3.,
                      'pdg_code':1,
                      'propagating':True,
                      'is_part':True,
                      'self_antipart':False}))
        antid = copy.copy(self.mypartlist[2])
        antid.set('is_part', False)

        self.mypartlist.append(base_objects.Particle({'name':'a',
                      'antiname':'a',
                      'spin':3,
                      'color':0,
                      'mass':'zero',
                      'width':'zero',
                      'texname':'\gamma',
                      'antitexname':'\gamma',
                      'line':'waivy',
                      'charge':0.,
                      'pdg_code':22,
                      'propagating':True,
                      'is_part':True,
                      'self_antipart':True}))

        self.myinterlist.append(base_objects.Interaction({
                      'particles': base_objects.ParticleList(\
                                            [self.mypartlist[0]] * 3),
                      'color': ['C1'],
                      'lorentz':['L1'],
                      'couplings':{(0, 0):'G'},
                      'orders':{'QCD':1}}))

        self.myinterlist.append(base_objects.Interaction({
                      'particles': base_objects.ParticleList(\
                                            [self.mypartlist[0]] * 4),
                      'color': ['C1'],
                      'lorentz':['L1'],
                      'couplings':{(0, 0):'G^2'},
                      'orders':{'QCD':2}}))

        self.myinterlist.append(base_objects.Interaction({
                      'particles': base_objects.ParticleList(\
                                            [self.mypartlist[1], \
                                             antiu, \
                                             self.mypartlist[0]]),
                      'color': ['C1'],
                      'lorentz':['L1'],
                      'couplings':{(0, 0):'GQQ'},
                      'orders':{'QCD':1}}))

        self.myinterlist.append(base_objects.Interaction({
                      'particles': base_objects.ParticleList(\
                                            [self.mypartlist[1], \
                                             antiu, \
                                             self.mypartlist[3]]),
                      'color': ['C1'],
                      'lorentz':['L1'],
                      'couplings':{(0, 0):'GQED'},
                      'orders':{'QED':1}}))

        self.myinterlist.append(base_objects.Interaction({
                      'particles': base_objects.ParticleList(\
                                            [self.mypartlist[2], \
                                             antid, \
                                             self.mypartlist[0]]),
                      'color': ['C1'],
                      'lorentz':['L1'],
                      'couplings':{(0, 0):'GQQ'},
                      'orders':{'QCD':1}}))

        self.myinterlist.append(base_objects.Interaction({
                      'particles': base_objects.ParticleList(\
                                            [self.mypartlist[2], \
                                             antid, \
                                             self.mypartlist[3]]),
                      'color': ['C1'],
                      'lorentz':['L1'],
                      'couplings':{(0, 0):'GQED'},
                      'orders':{'QED':1}}))

        self.ref_dict_to0 = self.myinterlist.generate_ref_dict()[0]
        self.ref_dict_to1 = self.myinterlist.generate_ref_dict()[1]


    def test_combine_legs(self):

        # Test gluon interactions

        myleglist = base_objects.LegList([base_objects.Leg({'id':21,
                                              'number':num,
                                              'state':'final'}) \
                                              for num in range(1, 5)])

        myleglist[0].set('state', 'initial')
        myleglist[1].set('state', 'initial')

        l1 = myleglist[0]
        l2 = myleglist[1]
        l3 = myleglist[2]
        l4 = myleglist[3]

        my_combined_legs = [\
                [(l1, l2), l3, l4], [(l1, l2), (l3, l4)], \
                [(l1, l3), l2, l4], [(l1, l3), (l2, l4)], \
                [(l1, l4), l2, l3], [(l1, l4), (l2, l3)], \
                [(l2, l3), l1, l4], [(l2, l4), l1, l3], [(l3, l4), l1, l2], \
                [(l1, l2, l3), l4], [(l1, l2, l4), l3], \
                [(l1, l3, l4), l2], [(l2, l3, l4), l1]\
                ]

        combined_legs = diagram_generation.combine_legs([leg for leg in myleglist], \
                                                        self.ref_dict_to1, \
                                                        3)
        self.assertEqual(combined_legs, my_combined_legs)

        # Now test the reduction of legs for this

        reduced_list = diagram_generation.reduce_legs(combined_legs, self.ref_dict_to1)

        l1.set('from_group', False)
        l2.set('from_group', False)
        l3.set('from_group', False)
        l4.set('from_group', False)

        l12 = base_objects.Leg({'id':21,
                                'number':1,
                                'state':'final'})
        l13 = base_objects.Leg({'id':21,
                                'number':1,
                                'state':'initial'})
        l14 = base_objects.Leg({'id':21,
                                'number':1,
                                'state':'initial'})
        l23 = base_objects.Leg({'id':21,
                                'number':2,
                                'state':'initial'})
        l24 = base_objects.Leg({'id':21,
                                'number':2,
                                'state':'initial'})
        l34 = base_objects.Leg({'id':21,
                                'number':3,
                                'state':'final'})
        l123 = base_objects.Leg({'id':21,
                                'number':1,
                                'state':'final'})
        l124 = base_objects.Leg({'id':21,
                                'number':1,
                                'state':'final'})
        l134 = base_objects.Leg({'id':21,
                                'number':1,
                                'state':'initial'})
        l234 = base_objects.Leg({'id':21,
                                'number':2,
                                'state':'initial'})

        my_reduced_list = [\
                (base_objects.LegList([(l12), l3, l4]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l12])})])), \
                (base_objects.LegList([(l12), (l34)]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l12])}), \
                                          base_objects.Vertex({'legs':base_objects.LegList([l3, l4, l34])})])), \
                (base_objects.LegList([(l13), l2, l4]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l3, l13])})])), \
                (base_objects.LegList([(l13), (l24)]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l3, l13])}), \
                                          base_objects.Vertex({'legs':base_objects.LegList([l2, l4, l24])})])), \
                (base_objects.LegList([(l14), l2, l3]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l4, l14])})])), \
                (base_objects.LegList([(l14), (l23)]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l4, l14])}), \
                                          base_objects.Vertex({'legs':base_objects.LegList([l2, l3, l23])})])), \
                (base_objects.LegList([(l23), l1, l4]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l2, l3, l23])})])), \
                (base_objects.LegList([(l24), l1, l3]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l2, l4, l24])})])), \
                (base_objects.LegList([(l34), l1, l2]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l3, l4, l34])})])), \
                (base_objects.LegList([(l123), l4]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l3, l123])})])), \
                (base_objects.LegList([(l124), l3]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l4, l124])})])), \
                (base_objects.LegList([(l134), l2]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l3, l4, l134])})])), \
                (base_objects.LegList([(l234), l1]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l2, l3, l4, l234])})])), \
                ]
        self.assertEqual(reduced_list.__str__(), my_reduced_list.__str__())

        # Test with 2 quarks+2 antiquarks (already flipped sign for IS)

        myleglist = base_objects.LegList()

        myleglist.append(base_objects.Leg({'id':-2,
                                         'number':1,
                                         'state':'initial'}))
        myleglist.append(base_objects.Leg({'id':2,
                                         'number':2,
                                         'state':'initial'}))
        myleglist.append(base_objects.Leg({'id':1,
                                         'number':3,
                                         'state':'final'}))
        myleglist.append(base_objects.Leg({'id':-1,
                                         'number':4,
                                         'state':'final'}))
        l1 = myleglist[0]
        l2 = myleglist[1]
        l3 = myleglist[2]
        l4 = myleglist[3]

        my_combined_legs = [\
                [(l1, l2), l3, l4], [(l1, l2), (l3, l4)], \
                [(l3, l4), l1, l2] \
                ]

        combined_legs = diagram_generation.combine_legs([leg for leg in myleglist], \
                                                        self.ref_dict_to1, \
                                                        3)
        self.assertEqual(combined_legs, my_combined_legs)

        # Now test the reduction of legs for this

        reduced_list = diagram_generation.reduce_legs(combined_legs, self.ref_dict_to1)

        l1.set('from_group', False)
        l2.set('from_group', False)
        l3.set('from_group', False)
        l4.set('from_group', False)

        l12glue = base_objects.Leg({'id':21,
                                'number':1,
                                'state':'final'})
        l12phot = base_objects.Leg({'id':22,
                                'number':1,
                                'state':'final'})
        l34glue = base_objects.Leg({'id':21,
                                'number':3,
                                'state':'final'})
        l34phot = base_objects.Leg({'id':22,
                                'number':3,
                                'state':'final'})
        my_reduced_list = [\
                (base_objects.LegList([l12glue, l3, l4]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l12glue])})])), \
                (base_objects.LegList([l12phot, l3, l4]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l12phot])})])), \
                (base_objects.LegList([l12glue, l34glue]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l12glue])}), base_objects.Vertex({'legs':base_objects.LegList([l3, l4, l34glue])})])), \
                (base_objects.LegList([l12glue, l34phot]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l12glue])}), base_objects.Vertex({'legs':base_objects.LegList([l3, l4, l34phot])})])), \
                (base_objects.LegList([l12phot, l34glue]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l12phot])}), base_objects.Vertex({'legs':base_objects.LegList([l3, l4, l34glue])})])), \
                (base_objects.LegList([l12phot, l34phot]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l1, l2, l12phot])}), base_objects.Vertex({'legs':base_objects.LegList([l3, l4, l34phot])})])), \
                (base_objects.LegList([l34glue, l1, l2]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l3, l4, l34glue])})])), \
                (base_objects.LegList([l34phot, l1, l2]), \
                 base_objects.VertexList([base_objects.Vertex({'legs':base_objects.LegList([l3, l4, l34phot])})])), \
                ]

        self.assertEqual(reduced_list.__str__(), my_reduced_list.__str__())

        # Now test with 3 quarks+3 antiquarks (already flipped sign for IS)
        myleglist = base_objects.LegList()

        myleglist.append(base_objects.Leg({'id':-2,
                                         'number':1,
                                         'state':'initial'}))
        myleglist.append(base_objects.Leg({'id':2,
                                         'number':2,
                                         'state':'initial'}))
        myleglist.append(base_objects.Leg({'id':2,
                                         'number':3,
                                         'state':'final'}))
        myleglist.append(base_objects.Leg({'id':-2,
                                         'number':4,
                                         'state':'final'}))
        myleglist.append(base_objects.Leg({'id':2,
                                         'number':5,
                                         'state':'final'}))
        myleglist.append(base_objects.Leg({'id':-2,
                                         'number':6,
                                         'state':'final'}))
        l1 = myleglist[0]
        l2 = myleglist[1]
        l3 = myleglist[2]
        l4 = myleglist[3]
        l5 = myleglist[4]
        l6 = myleglist[5]

        my_combined_legs = [\
                [(l1, l2), l3, l4, l5, l6], [(l1, l2), (l3, l4), l5, l6], \
                [(l1, l2), (l3, l4), (l5, l6)], [(l1, l2), (l3, l6), l4, l5], \
                [(l1, l2), (l3, l6), (l4, l5)], [(l1, l2), (l4, l5), l3, l6], \
                [(l1, l2), (l5, l6), l3, l4], \
                [(l1, l3), l2, l4, l5, l6], [(l1, l3), (l2, l4), l5, l6], \
                [(l1, l3), (l2, l4), (l5, l6)], [(l1, l3), (l2, l6), l4, l5], \
                [(l1, l3), (l2, l6), (l4, l5)], [(l1, l3), (l4, l5), l2, l6], \
                [(l1, l3), (l5, l6), l2, l4], \
                [(l1, l5), l2, l3, l4, l6], [(l1, l5), (l2, l4), l3, l6], \
                [(l1, l5), (l2, l4), (l3, l6)], [(l1, l5), (l2, l6), l3, l4], \
                [(l1, l5), (l2, l6), (l3, l4)], [(l1, l5), (l3, l4), l2, l6], \
                [(l1, l5), (l3, l6), l2, l4], \
                [(l2, l4), l1, l3, l5, l6], [(l2, l4), l1, (l3, l6), l5], \
                [(l2, l4), l1, (l5, l6), l3], \
                [(l2, l6), l1, l3, l4, l5], [(l2, l6), l1, (l3, l4), l5], \
                [(l2, l6), l1, (l4, l5), l3], \
                [(l3, l4), l1, l2, l5, l6], [(l3, l4), l1, l2, (l5, l6)], \
                [(l3, l6), l1, l2, l4, l5], [(l3, l6), l1, l2, (l4, l5)], \
                [(l4, l5), l1, l2, l3, l6], \
                [(l5, l6), l1, l2, l3, l4]
                ]

        combined_legs = diagram_generation.combine_legs([leg for leg in myleglist], \
                                                        self.ref_dict_to1, \
                                                        3)
        self.assertEqual(combined_legs, my_combined_legs)


    def test_diagram_generation(self):

        for ngluon in range (2, 7):

            myleglist = base_objects.LegList([base_objects.Leg({'id':21,
                                              'number':num,
                                              'state':'final'}) \
                                              for num in range(1, ngluon + 3)])

            myleglist[0].set('state', 'initial')
            myleglist[1].set('state', 'initial')

            myproc = base_objects.Process({'legs':myleglist,
                                           'orders':{'QCD':ngluon}})

            print "Number of diagrams for %d gluons: %d" % (ngluon, \
                len(diagram_generation.generate_diagrams(myproc, \
                                                         self.ref_dict_to0, \
                                                         self.ref_dict_to1)))

    def test_diagram_generation2(self):

        # Test with 2 quarks+2 antiquarks (already flipped sign for IS)

        myleglist = base_objects.LegList()

        myleglist.append(base_objects.Leg({'id':-1,
                                         'number':1,
                                         'state':'initial'}))
        myleglist.append(base_objects.Leg({'id':1,
                                         'number':2,
                                         'state':'initial'}))
        myleglist.append(base_objects.Leg({'id':21,
                                         'number':3,
                                         'state':'final'}))
        myleglist.append(base_objects.Leg({'id':21,
                                         'number':4,
                                         'state':'final'}))
        l1 = myleglist[0]
        l2 = myleglist[1]
        l3 = myleglist[2]
        l4 = myleglist[3]

        myproc = base_objects.Process({'legs':myleglist})

        self.assertEqual(len(diagram_generation.generate_diagrams(myproc,
                                                     self.ref_dict_to0,
                                                     self.ref_dict_to1)), 3)

    def test_expand_list(self):

        mylist = [[1, 2], 3, [4, 5]]

        goal_list = [[1, 3, 4], [1, 3, 5], [2, 3, 4], [2, 3, 5]]

        self.assertEqual(diagram_generation.expand_list(mylist), goal_list)

