      SUBROUTINE ML5_0_MP_HELAS_CALLS_UVCT_1(P,NHEL,H,IC)
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=5)
      INTEGER    NCOMB
      PARAMETER (NCOMB=48)

      INTEGER NBORNAMPS
      PARAMETER (NBORNAMPS=8)
      INTEGER    NLOOPS, NLOOPGROUPS, NCTAMPS
      PARAMETER (NLOOPS=144, NLOOPGROUPS=77, NCTAMPS=252)
      INTEGER    NLOOPAMPS
      PARAMETER (NLOOPAMPS=396)
      INTEGER    NWAVEFUNCS,NLOOPWAVEFUNCS
      PARAMETER (NWAVEFUNCS=28,NLOOPWAVEFUNCS=267)
      INCLUDE 'loop_max_coefs.inc'
      INCLUDE 'coef_specs.inc'
      REAL*16     ZERO
      PARAMETER (ZERO=0.0E0_16)
      COMPLEX*32     IZERO
      PARAMETER (IZERO=CMPLX(0.0E0_16,0.0E0_16,KIND=16))
C     These are constants related to the split orders
      INTEGER    NSO, NSQUAREDSO, NAMPSO
      PARAMETER (NSO=0, NSQUAREDSO=0, NAMPSO=0)
C     
C     ARGUMENTS
C     
      REAL*16 P(0:3,NEXTERNAL)
      INTEGER NHEL(NEXTERNAL), IC(NEXTERNAL)
      INTEGER H
C     
C     LOCAL VARIABLES
C     
      INTEGER I,J,K
      COMPLEX*32 COEFS(MAXLWFSIZE,0:VERTEXMAXCOEFS-1,MAXLWFSIZE)
C     
C     GLOBAL VARIABLES
C     
      INCLUDE 'mp_coupl_same_name.inc'

      INTEGER GOODHEL(NCOMB)
      LOGICAL GOODAMP(NSQUAREDSO,NLOOPGROUPS)
      COMMON/ML5_0_FILTERS/GOODAMP,GOODHEL

      INTEGER SQSO_TARGET
      COMMON/ML5_0_SOCHOICE/SQSO_TARGET

      LOGICAL UVCT_REQ_SO_DONE,MP_UVCT_REQ_SO_DONE,CT_REQ_SO_DONE
     $ ,MP_CT_REQ_SO_DONE,LOOP_REQ_SO_DONE,MP_LOOP_REQ_SO_DONE
     $ ,CTCALL_REQ_SO_DONE,FILTER_SO
      COMMON/ML5_0_SO_REQS/UVCT_REQ_SO_DONE,MP_UVCT_REQ_SO_DONE
     $ ,CT_REQ_SO_DONE,MP_CT_REQ_SO_DONE,LOOP_REQ_SO_DONE
     $ ,MP_LOOP_REQ_SO_DONE,CTCALL_REQ_SO_DONE,FILTER_SO

      COMPLEX*32 AMP(NBORNAMPS)
      COMMON/ML5_0_MP_AMPS/AMP
      COMPLEX*32 W(20,NWAVEFUNCS)
      COMMON/ML5_0_MP_W/W

      COMPLEX*32 WL(MAXLWFSIZE,0:LOOPMAXCOEFS-1,MAXLWFSIZE
     $ ,0:NLOOPWAVEFUNCS)
      COMPLEX*32 PL(0:3,0:NLOOPWAVEFUNCS)
      COMMON/ML5_0_MP_WL/WL,PL

      COMPLEX*32 AMPL(3,NCTAMPS)
      COMMON/ML5_0_MP_AMPL/AMPL

C     
C     ----------
C     BEGIN CODE
C     ----------

C     The target squared split order contribution is already reached
C      if true.
      IF (FILTER_SO.AND.MP_UVCT_REQ_SO_DONE) THEN
        GOTO 1001
      ENDIF

C     Amplitude(s) for UVCT diagram with ID 135
      CALL MP_FFV1_0(W(1,5),W(1,7),W(1,6),GC_5,AMPL(1,237))
      AMPL(1,237)=AMPL(1,237)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1+1.0D0
     $ *UVWFCT_T_0+1.0D0*UVWFCT_B_0)
C     Amplitude(s) for UVCT diagram with ID 136
      CALL MP_FFV1_0(W(1,5),W(1,7),W(1,6),GC_5,AMPL(2,238))
      AMPL(2,238)=AMPL(2,238)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0
     $ *UVWFCT_G_2_1EPS)
C     Amplitude(s) for UVCT diagram with ID 137
      CALL MP_FFV1_0(W(1,8),W(1,4),W(1,6),GC_5,AMPL(1,239))
      AMPL(1,239)=AMPL(1,239)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1+1.0D0
     $ *UVWFCT_T_0+1.0D0*UVWFCT_B_0)
C     Amplitude(s) for UVCT diagram with ID 138
      CALL MP_FFV1_0(W(1,8),W(1,4),W(1,6),GC_5,AMPL(2,240))
      AMPL(2,240)=AMPL(2,240)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0
     $ *UVWFCT_G_2_1EPS)
C     Amplitude(s) for UVCT diagram with ID 139
      CALL MP_FFV2_0(W(1,10),W(1,9),W(1,3),GC_47,AMPL(1,241))
      AMPL(1,241)=AMPL(1,241)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1+1.0D0
     $ *UVWFCT_T_0+1.0D0*UVWFCT_B_0)
C     Amplitude(s) for UVCT diagram with ID 140
      CALL MP_FFV2_0(W(1,10),W(1,9),W(1,3),GC_47,AMPL(2,242))
      AMPL(2,242)=AMPL(2,242)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0
     $ *UVWFCT_G_2_1EPS)
C     Amplitude(s) for UVCT diagram with ID 141
      CALL MP_FFV1_0(W(1,8),W(1,9),W(1,2),GC_5,AMPL(1,243))
      AMPL(1,243)=AMPL(1,243)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1+1.0D0
     $ *UVWFCT_T_0+1.0D0*UVWFCT_B_0)
C     Amplitude(s) for UVCT diagram with ID 142
      CALL MP_FFV1_0(W(1,8),W(1,9),W(1,2),GC_5,AMPL(2,244))
      AMPL(2,244)=AMPL(2,244)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0
     $ *UVWFCT_G_2_1EPS)
C     Amplitude(s) for UVCT diagram with ID 143
      CALL MP_FFV2_0(W(1,11),W(1,12),W(1,3),GC_47,AMPL(1,245))
      AMPL(1,245)=AMPL(1,245)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1+1.0D0
     $ *UVWFCT_T_0+1.0D0*UVWFCT_B_0)
C     Amplitude(s) for UVCT diagram with ID 144
      CALL MP_FFV2_0(W(1,11),W(1,12),W(1,3),GC_47,AMPL(2,246))
      AMPL(2,246)=AMPL(2,246)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0
     $ *UVWFCT_G_2_1EPS)
C     Amplitude(s) for UVCT diagram with ID 145
      CALL MP_FFV1_0(W(1,11),W(1,7),W(1,2),GC_5,AMPL(1,247))
      AMPL(1,247)=AMPL(1,247)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1+1.0D0
     $ *UVWFCT_T_0+1.0D0*UVWFCT_B_0)
C     Amplitude(s) for UVCT diagram with ID 146
      CALL MP_FFV1_0(W(1,11),W(1,7),W(1,2),GC_5,AMPL(2,248))
      AMPL(2,248)=AMPL(2,248)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0
     $ *UVWFCT_G_2_1EPS)
C     Amplitude(s) for UVCT diagram with ID 147
      CALL MP_FFV1_0(W(1,8),W(1,12),W(1,1),GC_5,AMPL(1,249))
      AMPL(1,249)=AMPL(1,249)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1+1.0D0
     $ *UVWFCT_T_0+1.0D0*UVWFCT_B_0)
C     Amplitude(s) for UVCT diagram with ID 148
      CALL MP_FFV1_0(W(1,8),W(1,12),W(1,1),GC_5,AMPL(2,250))
      AMPL(2,250)=AMPL(2,250)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0
     $ *UVWFCT_G_2_1EPS)
C     Amplitude(s) for UVCT diagram with ID 149
      CALL MP_FFV1_0(W(1,10),W(1,7),W(1,1),GC_5,AMPL(1,251))
      AMPL(1,251)=AMPL(1,251)*(2.0D0*UVWFCT_G_2+2.0D0*UVWFCT_G_1+1.0D0
     $ *UVWFCT_T_0+1.0D0*UVWFCT_B_0)
C     Amplitude(s) for UVCT diagram with ID 150
      CALL MP_FFV1_0(W(1,10),W(1,7),W(1,1),GC_5,AMPL(2,252))
      AMPL(2,252)=AMPL(2,252)*(2.0D0*UVWFCT_B_0_1EPS+4.0D0
     $ *UVWFCT_G_2_1EPS)

      GOTO 1001
 3000 CONTINUE
      MP_UVCT_REQ_SO_DONE=.TRUE.
 1001 CONTINUE
      END

