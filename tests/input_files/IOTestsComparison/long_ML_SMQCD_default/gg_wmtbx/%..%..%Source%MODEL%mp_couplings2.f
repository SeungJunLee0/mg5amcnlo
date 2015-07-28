ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE MP_COUP2()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'
      REAL*16 MP__PI, MP__ZERO
      PARAMETER (MP__PI=3.1415926535897932384626433832795E0_16)
      PARAMETER (MP__ZERO=0E0_16)
      INCLUDE 'mp_input.inc'
      INCLUDE 'mp_coupl.inc'

      MP__UV_3GB = -MP__MDL_G_UVB_FIN_*MP__G
      MP__UV_3GT = -MP__MDL_G_UVT_FIN_*MP__G
      MP__UV_GQQB = MP__MDL_COMPLEXI*MP__MDL_G_UVB_FIN_*MP__G
      MP__UV_GQQT = MP__MDL_COMPLEXI*MP__MDL_G_UVT_FIN_*MP__G
      MP__UV_BMASS = MP__MDL_BMASS_UV_FIN_
      MP__UV_TMASS = MP__MDL_TMASS_UV_FIN_
      MP__UVWFCT_B_0 = MP_COND(CMPLX(MP__MDL_MB,KIND=16),CMPLX(0.000000
     $ E+00_16,KIND=16),CMPLX(-((MP__MDL_G__EXP__2)/(2.000000E
     $ +00_16*1.600000E+01_16*MP__PI**2))*MP__MDL_CF*(4.000000E
     $ +00_16-3.000000E+00_16*MP_REGLOG(CMPLX((MP__MDL_MB__EXP__2
     $ /MP__MDL_MU_R__EXP__2),KIND=16))),KIND=16))
      MP__UVWFCT_T_0 = MP_COND(CMPLX(MP__MDL_MT,KIND=16),CMPLX(0.000000
     $ E+00_16,KIND=16),CMPLX(-((MP__MDL_G__EXP__2)/(2.000000E
     $ +00_16*1.600000E+01_16*MP__PI**2))*MP__MDL_CF*(4.000000E
     $ +00_16-3.000000E+00_16*MP_REGLOG(CMPLX((MP__MDL_MT__EXP__2
     $ /MP__MDL_MU_R__EXP__2),KIND=16))),KIND=16))
      MP__UVWFCT_G_2 = MP_COND(CMPLX(MP__MDL_MT,KIND=16),CMPLX(0.000000
     $ E+00_16,KIND=16),CMPLX(((MP__MDL_G__EXP__2)/(2.000000E
     $ +00_16*4.800000E+01_16*MP__PI**2))*4.000000E+00_16*MP__MDL_TF
     $ *MP_REGLOG(CMPLX((MP__MDL_MT__EXP__2/MP__MDL_MU_R__EXP__2)
     $ ,KIND=16)),KIND=16))
      MP__UVWFCT_G_1 = MP_COND(CMPLX(MP__MDL_MB,KIND=16),CMPLX(0.000000
     $ E+00_16,KIND=16),CMPLX(((MP__MDL_G__EXP__2)/(2.000000E
     $ +00_16*4.800000E+01_16*MP__PI**2))*4.000000E+00_16*MP__MDL_TF
     $ *MP_REGLOG(CMPLX((MP__MDL_MB__EXP__2/MP__MDL_MU_R__EXP__2)
     $ ,KIND=16)),KIND=16))
      MP__R2_SXCW = ((MP__MDL_CKM22*MP__MDL_EE*MP__MDL_COMPLEXI)
     $ /(MP__MDL_SW*MP__MDL_SQRT__2))*MP__MDL_R2MIXEDFACTOR_FIN_
      MP__GC_4 = -MP__G
      MP__GC_5 = MP__MDL_COMPLEXI*MP__G
      MP__GC_6 = MP__MDL_COMPLEXI*MP__MDL_G__EXP__2
      MP__R2_3GQ = 2.000000E+00_16*MP__MDL_G__EXP__3/(4.800000E
     $ +01_16*MP__PI**2)
      MP__R2_3GG = MP__MDL_NCOL*MP__MDL_G__EXP__3/(4.800000E+01_16
     $ *MP__PI**2)*(7.000000E+00_16/4.000000E+00_16+MP__MDL_LHV)
      MP__R2_GQQ = -MP__MDL_COMPLEXI*MP__MDL_G__EXP__3/(1.600000E
     $ +01_16*MP__PI**2)*((MP__MDL_NCOL__EXP__2_M_1)/(2.000000E
     $ +00_16*MP__MDL_NCOL))*(1.000000E+00_16+MP__MDL_LHV)
      MP__R2_GGQ = (2.000000E+00_16)*MP__MDL_COMPLEXI*MP__MDL_G__EXP__2
     $ /(4.800000E+01_16*MP__PI**2)
      MP__R2_GGB = (2.000000E+00_16)*MP__MDL_COMPLEXI*MP__MDL_G__EXP__2
     $ *(-6.000000E+00_16*MP__MDL_MB__EXP__2)/(4.800000E+01_16*MP__PI*
     $ *2)
      MP__R2_GGT = (2.000000E+00_16)*MP__MDL_COMPLEXI*MP__MDL_G__EXP__2
     $ *(-6.000000E+00_16*MP__MDL_MT__EXP__2)/(4.800000E+01_16*MP__PI*
     $ *2)
      MP__R2_GGG_1 = (2.000000E+00_16)*MP__MDL_COMPLEXI*MP__MDL_G__EXP_
     $ _2*MP__MDL_NCOL/(4.800000E+01_16*MP__PI**2)*(1.000000E
     $ +00_16/2.000000E+00_16+MP__MDL_LHV)
      MP__R2_GGG_2 = -(2.000000E+00_16)*MP__MDL_COMPLEXI*MP__MDL_G__EXP
     $ __2*MP__MDL_NCOL/(4.800000E+01_16*MP__PI**2)*MP__MDL_LHV
      MP__R2_QQQ = MP__MDL_LHV*MP__MDL_COMPLEXI*MP__MDL_G__EXP__2
     $ *(MP__MDL_NCOL__EXP__2_M_1)/(3.200000E+01_16*MP__PI**2
     $ *MP__MDL_NCOL)
      MP__R2_QQB = MP__MDL_LHV*MP__MDL_COMPLEXI*MP__MDL_G__EXP__2
     $ *(MP__MDL_NCOL__EXP__2_M_1)*(2.000000E+00_16*MP__MDL_MB)
     $ /(3.200000E+01_16*MP__PI**2*MP__MDL_NCOL)
      MP__R2_QQT = MP__MDL_LHV*MP__MDL_COMPLEXI*MP__MDL_G__EXP__2
     $ *(MP__MDL_NCOL__EXP__2_M_1)*(2.000000E+00_16*MP__MDL_MT)
     $ /(3.200000E+01_16*MP__PI**2*MP__MDL_NCOL)
      END
