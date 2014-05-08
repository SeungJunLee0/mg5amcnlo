C     THE CORE SUBROUTINE CALLED BY CUTTOOLS WHICH CONTAINS THE HELAS
C      CALLS BUILDING THE LOOP

      SUBROUTINE P1_LOOPNUM(Q,RES)
C     
C     CONSTANTS 
C     
      INTEGER    NLOOPS
      PARAMETER (NLOOPS=28)
      INTEGER LOOPMAXCOEFS
      PARAMETER (LOOPMAXCOEFS=15)
C     
C     ARGUMENTS 
C     
      COMPLEX*16 Q(0:3)
      COMPLEX*16 RES
C     
C     GLOBAL VARIABLES
C     
      INTEGER ID,RANK
      COMMON/P1_LOOP/ID,RANK

      COMPLEX*16 LOOPCOEFS(0:LOOPMAXCOEFS-1,NLOOPS)
      COMMON/P1_LCOEFS/LOOPCOEFS

      RES=(0.0D0,0.0D0)

      CALL P1_EVAL_POLY(LOOPCOEFS(0,ID),RANK,-Q,RES)

      END

      SUBROUTINE P1_MPLOOPNUM(Q,RES)
C     
C     MODULE
C     
      INCLUDE 'cts_mprec.h'
C     
C     CONSTANTS 
C     
      INTEGER    NLOOPS
      PARAMETER (NLOOPS=28)
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=4)
      INTEGER LOOPMAXCOEFS
      PARAMETER (LOOPMAXCOEFS=15)
C     
C     ARGUMENTS 
C     
      INCLUDE 'cts_mpc.h'                                             
     $ , INTENT(IN), DIMENSION(0:3) :: Q
      INCLUDE 'cts_mpc.h'                                             
     $ , INTENT(OUT) :: RES
C     
C     LOCAL VARIABLES 
C     
      COMPLEX*32 QRES
      REAL*8 DUMMY(3)
      REAL*16 QPP(0:3,NEXTERNAL)
      COMPLEX*32 QQ(0:3)
      INTEGER I,J
C     
C     GLOBAL VARIABLES
C     
      LOGICAL MP_DONE
      COMMON/MP_P1_DONE/MP_DONE

      INTEGER ID,RANK
      COMMON/P1_LOOP/ID,RANK

      COMPLEX*32 LOOPCOEFS(0:LOOPMAXCOEFS-1,NLOOPS)
      COMMON/MP_P1_LCOEFS/LOOPCOEFS

C     MP_PS IS THE FIXED (POSSIBLY IMPROVED) MP PS POINT AND MP_P IS
C      THE ONE WHICH CAN BE MODIFIED (I.E. ROTATED ETC.) FOR STABILITY
C      PURPOSE
      REAL*16 MP_PS(0:3,NEXTERNAL),MP_P(0:3,NEXTERNAL)
      COMMON/MP_P1_PSPOINT/MP_PS,MP_P

C     ----------
C     BEGIN CODE
C     ----------
      DO I=0,3
        QQ(I) = Q(I)
      ENDDO
      QRES=(0.0E0_16,0.0E0_16)

      IF (.NOT.MP_DONE) THEN
        CALL MP_P1_COMPUTE_LOOP_COEFS(MP_P,DUMMY)
        MP_DONE=.TRUE.
      ENDIF

      CALL MP_P1_EVAL_POLY(LOOPCOEFS(0,ID),RANK,-QQ,QRES)

      RES=QRES

      END

      SUBROUTINE P1_MPLOOPNUM_DUMMY(Q,RES)
C     
C     MODULE
C     
      INCLUDE 'cts_mprec.h'
C     
C     ARGUMENTS 
C     
      INCLUDE 'cts_mpc.h'                                             
     $ , INTENT(IN), DIMENSION(0:3) :: Q
      INCLUDE 'cts_mpc.h'                                             
     $ , INTENT(OUT) :: RES
C     
C     LOCAL VARIABLES 
C     
      COMPLEX*16 DRES
      COMPLEX*16 DQ(0:3)
      INTEGER I
C     ----------
C     BEGIN CODE
C     ----------
      DO I=0,3
        DQ(I) = Q(I)
      ENDDO

      CALL P1_LOOPNUM(DQ,DRES)
      RES=DRES

      END

