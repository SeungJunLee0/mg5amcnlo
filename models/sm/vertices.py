# This file was automatically created by FeynRules $Revision: 216 $
# Mathematica version: 7.0 for Mac OS X x86 (64-bit) (November 11, 2008)
# Date: Wed 7 Jul 2010 09:55:56


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.G, P.G, P.G ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV_9 ],
             couplings = {(0,0):C.GC_4})

V_2 = Vertex(name = 'V_2',
             particles = [ P.G, P.G, P.G, P.G ],
             color = [ 'f(2,3,\'a1\')*f(\'a1\',1,4)', 'f(2,4,\'a1\')*f(\'a1\',1,3)', 'f(3,4,\'a1\')*f(\'a1\',1,2)' ],
             lorentz = [ L.VVVV_12, L.VVVV_14, L.VVVV_15 ],
             couplings = {(1,1):C.GC_6,(2,0):C.GC_6,(0,2):C.GC_6})

V_3 = Vertex(name = 'V_3',
             particles = [ P.A, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVV_9 ],
             couplings = {(0,0):C.GC_26})

V_4 = Vertex(name = 'V_4',
             particles = [ P.A, P.A, P.W__minus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV_13 ],
             couplings = {(0,0):C.GC_28})

V_5 = Vertex(name = 'V_5',
             particles = [ P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVV_9 ],
             couplings = {(0,0):C.GC_7})

V_6 = Vertex(name = 'V_6',
             particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
             color = [ '1' ],
             lorentz = [ L.VVVV_13 ],
             couplings = {(0,0):C.GC_8})

V_7 = Vertex(name = 'V_7',
             particles = [ P.A, P.W__minus__, P.W__plus__, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV_16 ],
             couplings = {(0,0):C.GC_27})

V_8 = Vertex(name = 'V_8',
             particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
             color = [ '1' ],
             lorentz = [ L.VVVV_13 ],
             couplings = {(0,0):C.GC_9})

V_9 = Vertex(name = 'V_9',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS_10 ],
             couplings = {(0,0):C.GC_10})

V_10 = Vertex(name = 'V_10',
              particles = [ P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.SSS_1 ],
              couplings = {(0,0):C.GC_31})

V_11 = Vertex(name = 'V_11',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS_11 ],
              couplings = {(0,0):C.GC_11})

V_12 = Vertex(name = 'V_12',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS_8 ],
              couplings = {(0,0):C.GC_32})

V_13 = Vertex(name = 'V_13',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS_11 ],
              couplings = {(0,0):C.GC_30})

V_14 = Vertex(name = 'V_14',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS_8 ],
              couplings = {(0,0):C.GC_33})

V_15 = Vertex(name = 'V_15',
              particles = [ P.d__tilde__, P.d, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_1})

V_16 = Vertex(name = 'V_16',
              particles = [ P.s__tilde__, P.s, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_1})

V_17 = Vertex(name = 'V_17',
              particles = [ P.b__tilde__, P.b, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_1})

V_18 = Vertex(name = 'V_18',
              particles = [ P.e__plus__, P.e__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_3})

V_19 = Vertex(name = 'V_19',
              particles = [ P.m__plus__, P.m__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_3})

V_20 = Vertex(name = 'V_20',
              particles = [ P.tt__plus__, P.tt__minus__, P.A ],
              color = [ '1' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_3})

V_21 = Vertex(name = 'V_21',
              particles = [ P.u__tilde__, P.u, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_2})

V_22 = Vertex(name = 'V_22',
              particles = [ P.c__tilde__, P.c, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_2})

V_23 = Vertex(name = 'V_23',
              particles = [ P.t__tilde__, P.t, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_2})

V_24 = Vertex(name = 'V_24',
              particles = [ P.d__tilde__, P.d, P.G ],
              color = [ 'T(3,1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_5})

V_25 = Vertex(name = 'V_25',
              particles = [ P.s__tilde__, P.s, P.G ],
              color = [ 'T(3,1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_5})

V_26 = Vertex(name = 'V_26',
              particles = [ P.b__tilde__, P.b, P.G ],
              color = [ 'T(3,1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_5})


V_29 = Vertex(name = 'V_29',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS_2 ],
              couplings = {(0,0):C.GC_34})

V_30 = Vertex(name = 'V_30',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4, L.FFV_5 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_24})

V_31 = Vertex(name = 'V_31',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4, L.FFV_5 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_24})

V_32 = Vertex(name = 'V_32',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4, L.FFV_5 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_24})

V_33 = Vertex(name = 'V_33',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_13})

V_34 = Vertex(name = 'V_34',
              particles = [ P.d__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_16})

V_35 = Vertex(name = 'V_35',
              particles = [ P.d__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_19})

V_36 = Vertex(name = 'V_36',
              particles = [ P.s__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_14})

V_37 = Vertex(name = 'V_37',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_17})

V_38 = Vertex(name = 'V_38',
              particles = [ P.s__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_20})

V_39 = Vertex(name = 'V_39',
              particles = [ P.b__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_15})

V_40 = Vertex(name = 'V_40',
              particles = [ P.b__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_18})

V_41 = Vertex(name = 'V_41',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_21})

V_42 = Vertex(name = 'V_42',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_43})

V_43 = Vertex(name = 'V_43',
              particles = [ P.c__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_46})

V_44 = Vertex(name = 'V_44',
              particles = [ P.t__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_49})

V_45 = Vertex(name = 'V_45',
              particles = [ P.u__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_44})

V_46 = Vertex(name = 'V_46',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_47})

V_47 = Vertex(name = 'V_47',
              particles = [ P.t__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_50})

V_48 = Vertex(name = 'V_48',
              particles = [ P.u__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_45})

V_49 = Vertex(name = 'V_49',
              particles = [ P.c__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_48})

V_50 = Vertex(name = 'V_50',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_51})

V_51 = Vertex(name = 'V_51',
              particles = [ P.u__tilde__, P.u, P.G ],
              color = [ 'T(3,1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_5})

V_52 = Vertex(name = 'V_52',
              particles = [ P.c__tilde__, P.c, P.G ],
              color = [ 'T(3,1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_5})

V_53 = Vertex(name = 'V_53',
              particles = [ P.t__tilde__, P.t, P.G ],
              color = [ 'T(3,1,2)' ],
              lorentz = [ L.FFV_3 ],
              couplings = {(0,0):C.GC_5})

V_56 = Vertex(name = 'V_56',
              particles = [ P.tt__plus__, P.tt__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS_2 ],
              couplings = {(0,0):C.GC_41})

V_59 = Vertex(name = 'V_59',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS_2 ],
              couplings = {(0,0):C.GC_40})

V_60 = Vertex(name = 'V_60',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV_4, L.FFV_6 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_25})

V_61 = Vertex(name = 'V_61',
              particles = [ P.m__plus__, P.m__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV_4, L.FFV_6 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_25})

V_62 = Vertex(name = 'V_62',
              particles = [ P.tt__plus__, P.tt__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV_4, L.FFV_6 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_25})

V_63 = Vertex(name = 'V_63',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_12})

V_64 = Vertex(name = 'V_64',
              particles = [ P.m__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_12})

V_65 = Vertex(name = 'V_65',
              particles = [ P.tt__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_12})

V_66 = Vertex(name = 'V_66',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_12})

V_67 = Vertex(name = 'V_67',
              particles = [ P.vm__tilde__, P.m__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_12})

V_68 = Vertex(name = 'V_68',
              particles = [ P.vt__tilde__, P.tt__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_12})

V_69 = Vertex(name = 'V_69',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4, L.FFV_7 ],
              couplings = {(0,0):C.GC_23,(0,1):C.GC_24})

V_70 = Vertex(name = 'V_70',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4, L.FFV_7 ],
              couplings = {(0,0):C.GC_23,(0,1):C.GC_24})

V_71 = Vertex(name = 'V_71',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV_4, L.FFV_7 ],
              couplings = {(0,0):C.GC_23,(0,1):C.GC_24})

V_72 = Vertex(name = 'V_72',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_29})

V_73 = Vertex(name = 'V_73',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_29})

V_74 = Vertex(name = 'V_74',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV_4 ],
              couplings = {(0,0):C.GC_29})

