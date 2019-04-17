# This file was automatically created by FeynRules $Revision: 535 $
# Mathematica version: 7.0 for Mac OS X x86 (64-bit) (November 11, 2008)
# Date: Fri 18 Mar 2011 18:40:51


from __future__ import absolute_import
from .object_library import all_vertices, all_CTvertices, Vertex, CTVertex
from . import particles as P
from . import CT_couplings as C
from . import lorentz as L

################
# R2 vertices  #
################

# ========= #
# Pure QCD  #
# ========= #

# ggg R2
V_R23G = CTVertex(name = 'V_R23G',
              particles = [ P.G, P.G, P.G ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              loop_particles = [ [[P.u], [P.d], [P.c], [P.s], [P.b], [P.t]],
                               [[P.G]] ],
              couplings = {(0,0,0):C.R2_3Gq, (0,0,1):C.R2_3Gg},
              type = 'R2' )

#=============================================================================================
#  4-gluon R2 vertex
#=============================================================================================

# Keep in mind that Delta8(a,b) is 1/2 Tr(a,b)

V_R24G = CTVertex(name = 'V_R24G',
              particles = [ P.G, P.G, P.G,  P.G ],
              color = [ 'Tr(1,2)*Tr(3,4)' , 'Tr(1,3)*Tr(2,4)' , 'Tr(1,4)*Tr(2,3)', \
                        'd(-1,1,2)*d(-1,3,4)' , 'd(-1,1,3)*d(-1,2,4)' , 'd(-1,1,4)*d(-1,2,3)'],
              lorentz = [  L.R2_4G_1234, L.R2_4G_1324, L.R2_4G_1423 ],
              loop_particles = [ [[P.G]], [[P.u],[P.d],[P.c],[P.s],[P.b],[P.t]] ],
              couplings = {(0,0,0):C.GC_4GR2_Gluon_delta5,(0,1,0):C.GC_4GR2_Gluon_delta7,(0,2,0):C.GC_4GR2_Gluon_delta7, \
                           (1,0,0):C.GC_4GR2_Gluon_delta7,(1,1,0):C.GC_4GR2_Gluon_delta5,(1,2,0):C.GC_4GR2_Gluon_delta7, \
                           (2,0,0):C.GC_4GR2_Gluon_delta7,(2,1,0):C.GC_4GR2_Gluon_delta7,(2,2,0):C.GC_4GR2_Gluon_delta5, \
                           (3,0,0):C.GC_4GR2_4Struct,(3,1,0):C.GC_4GR2_2Struct,(3,2,0):C.GC_4GR2_2Struct, \
                           (4,0,0):C.GC_4GR2_2Struct,(4,1,0):C.GC_4GR2_4Struct,(4,2,0):C.GC_4GR2_2Struct, \
                           (5,0,0):C.GC_4GR2_2Struct,(5,1,0):C.GC_4GR2_2Struct,(5,2,0):C.GC_4GR2_4Struct , \
                           (0,0,1):C.GC_4GR2_Fermion_delta11,(0,1,1):C.GC_4GR2_Fermion_delta5,(0,2,1):C.GC_4GR2_Fermion_delta5, \
                           (1,0,1):C.GC_4GR2_Fermion_delta5,(1,1,1):C.GC_4GR2_Fermion_delta11,(1,2,1):C.GC_4GR2_Fermion_delta5, \
                           (2,0,1):C.GC_4GR2_Fermion_delta5,(2,1,1):C.GC_4GR2_Fermion_delta5,(2,2,1):C.GC_4GR2_Fermion_delta11, \
                           (3,0,1):C.GC_4GR2_11Struct,(3,1,1):C.GC_4GR2_5Struct,(3,2,1):C.GC_4GR2_5Struct, \
                           (4,0,1):C.GC_4GR2_5Struct,(4,1,1):C.GC_4GR2_11Struct,(4,2,1):C.GC_4GR2_5Struct, \
                           (5,0,1):C.GC_4GR2_5Struct,(5,1,1):C.GC_4GR2_5Struct,(5,2,1):C.GC_4GR2_11Struct },
              type = 'R2')

#=============================================================================================

# gdd~
V_R2GDD = CTVertex(name = 'V_R2GDD',
              particles = [ P.d__tilde__, P.d, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              loop_particles =[[[P.d,P.G]]],                 
              couplings = {(0,0,0):C.R2_GQQ},
              type = 'R2')

# guu~              
V_R2GUU = CTVertex(name = 'V_R2GUU',
               particles = [ P.u__tilde__, P.u, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles =[[[P.u,P.G]]],
               couplings = {(0,0,0):C.R2_GQQ},
               type = 'R2')  

# gss~
V_R2GSS = CTVertex(name = 'V_R2GSS',
              particles = [ P.s__tilde__, P.s, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              loop_particles =[[[P.s,P.G]]],
              couplings = {(0,0,0):C.R2_GQQ},
              type = 'R2')

# gcc~              
V_R2GCC = CTVertex(name = 'V_R2GCC',
               particles = [ P.c__tilde__, P.c, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles =[[[P.c,P.G]]],               
               couplings = {(0,0,0):C.R2_GQQ},
               type = 'R2')  

# gbb~
V_R2GBB = CTVertex(name = 'V_R2GBB',
              particles = [ P.b__tilde__, P.b, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              loop_particles =[[[P.b,P.G]]],
              couplings = {(0,0,0):C.R2_GQQ},
              type = 'R2')

# gtt~              
V_R2GTT = CTVertex(name = 'V_R2GTT',
               particles = [ P.t__tilde__, P.t, P.G ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               loop_particles =[[[P.t,P.G]]],               
               couplings = {(0,0,0):C.R2_GQQ},
               type = 'R2')

# gg             
V_R2GG = CTVertex(name = 'V_R2GG',
               particles = [ P.G, P.G ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.R2_GG_1, L.R2_GG_2, L.R2_GG_3],
               loop_particles = [ [[P.u],[P.d],[P.c],[P.s]],
                                  [[P.b]],
                                  [[P.t]],
                                  [[P.G]] ],
               couplings = {(0,0,0):C.R2_GGq,
                            (0,0,1):C.R2_GGq,(0,2,1):C.R2_GGb,
                            (0,0,2):C.R2_GGq,(0,2,2):C.R2_GGt,
                            (0,0,3):C.R2_GGg_1, (0,1,3):C.R2_GGg_2},
               type = 'R2')

# d~d            
V_R2DD = CTVertex(name = 'V_R2DD',
               particles = [ P.d__tilde__, P.d ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.R2_QQ_1 ],
               loop_particles = [[[P.d,P.G]]],
               couplings = {(0,0,0):C.R2_QQq},
               type = 'R2') 

# u~u            
V_R2UU = CTVertex(name = 'V_R2UU',
               particles = [ P.u__tilde__, P.u ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.R2_QQ_1 ],
               loop_particles = [[[P.u,P.G]]],            
               couplings = {(0,0,0):C.R2_QQq},
               type = 'R2')

# s~s            
V_R2SS = CTVertex(name = 'V_R2SS',
               particles = [ P.s__tilde__, P.s ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.R2_QQ_1 ],
               loop_particles = [[[P.s,P.G]]],                
               couplings = {(0,0,0):C.R2_QQq},
               type = 'R2')

# c~c            
V_R2CC = CTVertex(name = 'V_R2CC',
               particles = [ P.c__tilde__, P.c ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.R2_QQ_1 ],
               loop_particles = [[[P.c,P.G]]],
               couplings = {(0,0,0):C.R2_QQq},                
               type = 'R2') 

# b~b            
V_R2BB = CTVertex(name = 'V_R2BB',
               particles = [ P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.R2_QQ_1, L.R2_QQ_2 ],
               loop_particles = [[[P.b,P.G]]],
               couplings = {(0,0,0):C.R2_QQq,(0,1,0):C.R2_QQb},                
               type = 'R2')

# t~t            
V_R2TT = CTVertex(name = 'V_R2TT',
               particles = [ P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.R2_QQ_1, L.R2_QQ_2 ],
               loop_particles = [[[P.t,P.G]]],
               couplings = {(0,0,0):C.R2_QQq,(0,1,0):C.R2_QQt},
               type = 'R2')

# ============== #
# Mixed QCD-QED  #
# ============== #

# R2 for the A and Z couplings to the quarks

V_R2ddA = CTVertex(name = 'V_R2ddA',
              particles = [ P.d__tilde__, P.d, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.d,P.G]]],
              couplings = {(0,0,0):C.R2_DDA},
              type = 'R2')

V_R2ssA = CTVertex(name = 'V_R2ssA',
              particles = [ P.s__tilde__, P.s, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.s,P.G]]],
              couplings = {(0,0,0):C.R2_DDA},
              type = 'R2')

V_R2bbA = CTVertex(name = 'V_R2bbA',
              particles = [ P.b__tilde__, P.b, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.b,P.G]]],
              couplings = {(0,0,0):C.R2_DDA},
              type = 'R2')

V_R2uuA = CTVertex(name = 'V_R2uuA',
              particles = [ P.u__tilde__, P.u, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.u,P.G]]],
              couplings = {(0,0,0):C.R2_UUA},
              type = 'R2')

V_R2ccA = CTVertex(name = 'V_R2ccA',
              particles = [ P.c__tilde__, P.c, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.c,P.G]]],
              couplings = {(0,0,0):C.R2_UUA},
              type = 'R2')

V_R2ttA = CTVertex(name = 'V_R2ttA',
              particles = [ P.t__tilde__, P.t, P.A ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.t,P.G]]],
              couplings = {(0,0,0):C.R2_UUA},
              type = 'R2')

V_R2ddZ = CTVertex(name = 'V_R2ddZ',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              loop_particles = [[[P.d,P.G]]],
              couplings = {(0,0,0):C.R2_DDZ_V2,(0,1,0):C.R2_DDZ_V3},
              type = 'R2')

V_R2ssZ = CTVertex(name = 'V_R2ssZ',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              loop_particles = [[[P.s,P.G]]],
              couplings = {(0,0,0):C.R2_DDZ_V2,(0,1,0):C.R2_DDZ_V3},
              type = 'R2')

V_R2bbZ = CTVertex(name = 'V_R2bbZ',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              loop_particles = [[[P.b,P.G]]],
              couplings = {(0,0,0):C.R2_DDZ_V2,(0,1,0):C.R2_DDZ_V3},
              type = 'R2')

V_R2uuZ = CTVertex(name = 'V_R2uuZ',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              loop_particles = [[[P.u,P.G]]],
              couplings = {(0,0,0):C.R2_UUZ_V2,(0,1,0):C.R2_UUZ_V5},
              type = 'R2')

V_R2ccZ = CTVertex(name = 'V_R2ccZ',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              loop_particles = [[[P.c,P.G]]],
              couplings = {(0,0,0):C.R2_UUZ_V2,(0,1,0):C.R2_UUZ_V5},
              type = 'R2')

V_R2ttZ = CTVertex(name = 'V_R2ttZ',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              loop_particles = [[[P.t,P.G]]],
              couplings = {(0,0,0):C.R2_UUZ_V2,(0,1,0):C.R2_UUZ_V5},
              type = 'R2')

# R2 for the W couplings to the quarks with most general CKM

V_R2dxuW = CTVertex(name = 'V_R2dxuW',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.d,P.u,P.G]]],                   
              couplings = {(0,0,0):C.R2_dxuW},
              type = 'R2')

V_R2dxcW = CTVertex(name = 'V_R2dxcW',
              particles = [ P.d__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.d,P.c,P.G]]],                   
              couplings = {(0,0,0):C.R2_dxcW},
              type = 'R2')

V_R2dxtW = CTVertex(name = 'V_R2dxtW',
              particles = [ P.d__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.d,P.t,P.G]]],                   
              couplings = {(0,0,0):C.R2_dxtW},
              type = 'R2')

V_R2sxuW = CTVertex(name = 'V_R2sxuW',
              particles = [ P.s__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.s,P.u,P.G]]],                   
              couplings = {(0,0,0):C.R2_sxuW},
              type = 'R2')

V_R2sxcW = CTVertex(name = 'V_R2sxcW',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.s,P.c,P.G]]],                   
              couplings = {(0,0,0):C.R2_sxcW},
              type = 'R2')

V_R2sxtW = CTVertex(name = 'V_R2sxtW',
              particles = [ P.s__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.s,P.t,P.G]]],                   
              couplings = {(0,0,0):C.R2_sxtW},
              type = 'R2')

V_R2bxuW = CTVertex(name = 'V_R2bxuW',
              particles = [ P.b__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.b,P.u,P.G]]],                   
              couplings = {(0,0,0):C.R2_bxuW},
              type = 'R2')

V_R2bxcW = CTVertex(name = 'V_R2bxcW',
              particles = [ P.b__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.b,P.c,P.G]]],                   
              couplings = {(0,0,0):C.R2_bxcW},
              type = 'R2')

V_R2bxtW = CTVertex(name = 'V_R2bxtW',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.b,P.t,P.G]]],                   
              couplings = {(0,0,0):C.R2_bxtW},
              type = 'R2')

V_R2uxdW = CTVertex(name = 'V_R2uxdW',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.u,P.d,P.G]]],                   
              couplings = {(0,0,0):C.R2_uxdW},
              type = 'R2')

V_R2cxdW = CTVertex(name = 'V_R2cxdW',
              particles = [ P.c__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.c,P.d,P.G]]],                   
              couplings = {(0,0,0):C.R2_cxdW},
              type = 'R2')

V_R2txdW = CTVertex(name = 'V_R2txdW',
              particles = [ P.t__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.t,P.d,P.G]]],                   
              couplings = {(0,0,0):C.R2_txdW},
              type = 'R2')

V_R2uxsW = CTVertex(name = 'V_R2uxsW',
              particles = [ P.u__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.u,P.s,P.G]]],                   
              couplings = {(0,0,0):C.R2_uxsW},
              type = 'R2')

V_R2cxsW = CTVertex(name = 'V_R2cxsW',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.c,P.s,P.G]]],                   
              couplings = {(0,0,0):C.R2_cxsW},
              type = 'R2')

V_R2txsW = CTVertex(name = 'V_R2txsW',
              particles = [ P.t__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.t,P.s,P.G]]],                   
              couplings = {(0,0,0):C.R2_txsW},
              type = 'R2')

V_R2uxbW = CTVertex(name = 'V_R2uxbW',
              particles = [ P.u__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.u,P.b,P.G]]],                   
              couplings = {(0,0,0):C.R2_uxbW},
              type = 'R2')

V_R2cxbW = CTVertex(name = 'V_R2cxbW',
              particles = [ P.c__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.c,P.b,P.G]]],                   
              couplings = {(0,0,0):C.R2_cxbW},
              type = 'R2')

V_R2txbW = CTVertex(name = 'V_R2txbW',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              loop_particles = [[[P.t,P.b,P.G]]],                   
              couplings = {(0,0,0):C.R2_txbW},
              type = 'R2')

# R2 for the Higgs couplings to massive quarks 

V_bbH = CTVertex(name = 'V_bbH',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              loop_particles = [[[P.b,P.G]]],
              couplings = {(0,0,0):C.R2_bbH},
              type = 'R2')

V_ttH = CTVertex(name = 'V_ttH',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              loop_particles = [[[P.t,P.G]]],
              couplings = {(0,0,0):C.R2_ttH},
              type = 'R2')

V_ccH = CTVertex(name = 'V_ccH',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              loop_particles = [[[P.c,P.G]]],
              couplings = {(0,0,0):C.R2_ccH},
              type = 'R2')

# R2 interactions non proportional to the SM

# R2 for the Higgs interactions

V_GGH = CTVertex(name = 'V_GGH',
              particles = [ P.G, P.G, P.H ],
              color = [ 'Tr(1,2)' ],
              lorentz = [ L.VVS1 ],
              loop_particles = [[[P.c]],[[P.b]],[[P.t]]],
              couplings = {(0,0,0):C.R2_GGHc,(0,0,1):C.R2_GGHb,(0,0,2):C.R2_GGHt},
              type = 'R2')

V_GGHH = CTVertex(name = 'V_GGHH',
              particles = [ P.G, P.G, P.H, P.H ],
              color = [ 'Tr(1,2)' ],
              lorentz = [ L.R2_GGHH ],
              loop_particles = [[[P.c]],[[P.b]],[[P.t]]],
              couplings = {(0,0,0):C.R2_GGHHc,(0,0,1):C.R2_GGHHb,(0,0,2):C.R2_GGHHt},
              type = 'R2')

# R2 for the weak vector bosons interaction with gluons

V_GGZ = CTVertex(name = 'V_GGZ',
              particles = [ P.G, P.G, P.Z ],
              color = [ 'Tr(1,2)' ],
              lorentz = [ L.R2_GGZ ],
              loop_particles = [[[P.u],[P.c],[P.t]],[[P.d],[P.s],[P.b]]],
              couplings = {(0,0,0):C.R2_GGZup,(0,0,1):C.R2_GGZdown},
              type = 'R2')

V_GGZZ = CTVertex(name = 'V_GGZZ',
              particles = [ P.G, P.G, P.Z, P.Z ],
              color = [ 'Tr(1,2)' ],
              lorentz = [ L.R2_GGVV ],
              loop_particles = [[[P.u],[P.c],[P.t]],[[P.d],[P.s],[P.b]]],
              couplings = {(0,0,0):C.R2_GGZZup,(0,0,1):C.R2_GGZZdown},
              type = 'R2')

V_GGAA = CTVertex(name = 'V_GGAA',
              particles = [ P.G, P.G, P.A, P.A ],
              color = [ 'Tr(1,2)' ],
              lorentz = [ L.R2_GGVV ],
              loop_particles = [[[P.u],[P.c],[P.t]],[[P.d],[P.s],[P.b]]],
              couplings = {(0,0,0):C.R2_GGAAup,(0,0,1):C.R2_GGAAdown},
              type = 'R2')

V_GGWW = CTVertex(name = 'V_GGWW',
              particles = [ P.G, P.G, P.W__minus__, P.W__plus__ ],
              color = [ 'Tr(1,2)' ],
              lorentz = [ L.R2_GGVV ],
              loop_particles = [[[P.u,P.d]],[[P.u,P.s]],[[P.u,P.b]],
                                [[P.c,P.d]],[[P.c,P.s]],[[P.c,P.b]],
                                [[P.t,P.d]],[[P.t,P.s]],[[P.t,P.b]]],
              couplings = {(0,0,0):C.R2_GGWWud,(0,0,1):C.R2_GGWWus,(0,0,2):C.R2_GGWWub,
                           (0,0,3):C.R2_GGWWcd,(0,0,4):C.R2_GGWWcs,(0,0,5):C.R2_GGWWcb,
                           (0,0,6):C.R2_GGWWtd,(0,0,7):C.R2_GGWWts,(0,0,8):C.R2_GGWWtb},
              type = 'R2')

V_GGGZ = CTVertex(name = 'V_GGGZ',
              particles = [ P.G, P.G, P.G, P.Z ],
              color = [ 'd(1,2,3)' , 'f(1,2,3)'],
              lorentz = [ L.R2_GGVV, L.R2_GGGVa ],
              loop_particles = [[[P.u],[P.c],[P.t]],[[P.d],[P.s],[P.b]]],
              couplings = {(0,0,0):C.R2_GGGZvecUp,(0,0,1):C.R2_GGGZvecDown,
                           (1,1,0):C.R2_GGGZaxialUp,(1,1,1):C.R2_GGGZaxialDown},
              type = 'R2')

V_GGGA = CTVertex(name = 'V_GGGA',
              particles = [ P.G, P.G, P.G, P.A ],
              color = [ 'd(1,2,3)'],
              lorentz = [ L.R2_GGVV ],
              loop_particles = [[[P.u],[P.c],[P.t]],[[P.d],[P.s],[P.b]]],
              couplings = {(0,0,0):C.R2_GGGAvecUp,(0,0,1):C.R2_GGGAvecDown},
              type = 'R2')

################
# UV vertices  #
################

# ========= #
# Pure QCD  #
# ========= #

# There are the alpha_s renormalization vertices

# ggg
V_UV1eps3G = CTVertex(name = 'V_UV1eps3G',
              particles = [ P.G, P.G, P.G ],
              color = [ 'f(1,2,3)' ],
              lorentz = [ L.VVV1 ],
              loop_particles = [[[P.u],[P.d],[P.c],[P.s]],[[P.b]],[[P.t]],[[P.G]]],
              couplings = {(0,0,0):C.UV_3Gq,(0,0,1):C.UV_3Gb,(0,0,2):C.UV_3Gt,(0,0,3):C.UV_3Gg},
              type = 'UVtree')

# gggg
V_UV4G = CTVertex(name = 'V_UV1eps4G',
              particles = [ P.G, P.G, P.G, P.G ],
              color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
              lorentz = [ L.VVVV1, L.VVVV3, L.VVVV4 ],
              loop_particles = [[[P.u],[P.d],[P.c],[P.s]],[[P.b]],[[P.t]],[[P.G]]],
              couplings = {(0,0,0):C.UV_4Gq,(0,0,1):C.UV_4Gb,(0,0,2):C.UV_4Gt,(0,0,3):C.UV_4Gg,
                           (1,1,0):C.UV_4Gq,(1,1,1):C.UV_4Gb,(1,1,2):C.UV_4Gt,(1,1,3):C.UV_4Gg,
                           (2,2,0):C.UV_4Gq,(2,2,1):C.UV_4Gb,(2,2,2):C.UV_4Gt,(2,2,3):C.UV_4Gg},
              type = 'UVtree')

# gdd~
V_UVGDD = CTVertex(name = 'V_UVGDD',
              particles = [ P.d__tilde__, P.d, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.u],[P.d],[P.c],[P.s]],[[P.b]],[[P.t]],[[P.G]]],
              couplings = {(0,0,0):C.UV_GQQq,(0,0,1):C.UV_GQQb,(0,0,2):C.UV_GQQt,(0,0,3):C.UV_GQQg},
              type = 'UVtree')

# guu~
V_UVGUU = CTVertex(name = 'V_UVGUU',
              particles = [ P.u__tilde__, P.u, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.u],[P.d],[P.c],[P.s]],[[P.b]],[[P.t]],[[P.G]]],
              couplings = {(0,0,0):C.UV_GQQq,(0,0,1):C.UV_GQQb,(0,0,2):C.UV_GQQt,(0,0,3):C.UV_GQQg},
              type = 'UVtree')

# gcc~
V_UVGCC = CTVertex(name = 'V_UVGCC',
              particles = [ P.c__tilde__, P.c, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.u],[P.d],[P.c],[P.s]],[[P.b]],[[P.t]],[[P.G]]],
              couplings = {(0,0,0):C.UV_GQQq,(0,0,1):C.UV_GQQb,(0,0,2):C.UV_GQQt,(0,0,3):C.UV_GQQg},
              type = 'UVtree')

# gss~
V_UVGSS = CTVertex(name = 'V_UVGSS',
              particles = [ P.s__tilde__, P.s, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.u],[P.d],[P.c],[P.s]],[[P.b]],[[P.t]],[[P.G]]],
              couplings = {(0,0,0):C.UV_GQQq,(0,0,1):C.UV_GQQb,(0,0,2):C.UV_GQQt,(0,0,3):C.UV_GQQg},
              type = 'UVtree')

# gbb~
V_UVGBB = CTVertex(name = 'V_UVGBB',
              particles = [ P.b__tilde__, P.b, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.u],[P.d],[P.c],[P.s]],[[P.b]],[[P.t]],[[P.G]]],
              couplings = {(0,0,0):C.UV_GQQq,(0,0,1):C.UV_GQQb,(0,0,2):C.UV_GQQt,(0,0,3):C.UV_GQQg},
              type = 'UVtree')

# gtt~
V_UVGTT = CTVertex(name = 'V_UVGTT',
              particles = [ P.t__tilde__, P.t, P.G ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              loop_particles = [[[P.u],[P.d],[P.c],[P.s]],[[P.b]],[[P.t]],[[P.G]]],
              couplings = {(0,0,0):C.UV_GQQq,(0,0,1):C.UV_GQQb,(0,0,2):C.UV_GQQt,(0,0,3):C.UV_GQQg},
              type = 'UVtree')

# These are the mass renormalization vertices.

# b~b         
V_UVbMass = CTVertex(name = 'V_UVbMass',
               particles = [ P.b__tilde__, P.b ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.R2_QQ_2 ],
               loop_particles = [[[P.G,P.b]]],                   
               couplings = {(0,0,0):C.UV_bMass},
               type = 'UVmass') 

# t~t         
V_UVbMass = CTVertex(name = 'V_UVtMass',
               particles = [ P.t__tilde__, P.t ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.R2_QQ_2 ],
               loop_particles = [[[P.G,P.t]]],                   
               couplings = {(0,0,0):C.UV_tMass},
               type = 'UVmass')

# ============== #
# Mixed QCD-QED  #
# ============== #

V_UVHtt = CTVertex(name = 'V_UVHtt',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              loop_particles = [[[P.G,P.t]]],                   
              couplings = {(0,0,0):C.UV_Htt},
              type = 'UVtree')

V_UVHbb = CTVertex(name = 'V_UVHbb',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1 ],
              loop_particles = [[[P.G,P.b]]],
              couplings = {(0,0,0):C.UV_Hbb},
              type = 'UVtree')

