      SUBROUTINE SBORN_HEL(P,ANS_SUMMED)
C     
C     Return the sum of the split orders which are required in
C      orders.inc (BORN_ORDERS)
C     Also the values needed for the counterterms are stored in the
C      C_BORN_CNT common block
C     
C     
C     CONSTANTS
C     
      IMPLICIT NONE
      INCLUDE 'nexternal.inc'
      INTEGER NSQAMPSO
      PARAMETER (NSQAMPSO=1)
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL-1), ANS_SUMMED
C     
C     VARIABLES
C     
      INTEGER I, J
      INCLUDE 'orders.inc'
      REAL*8 ANS(0:NSQAMPSO)
      INCLUDE 'born_nhel.inc'
      DOUBLE PRECISION WGT_HEL(NSQAMPSO, MAX_BHEL)
      COMMON/C_BORN_HEL_SPLIT/WGT_HEL
      DOUBLE PRECISION WGT_HEL_SUMMED(MAX_BHEL)
      COMMON/C_BORN_HEL/WGT_HEL_SUMMED
C     
C     FUNCTIONS
C     
      INTEGER GETORDPOWFROMINDEX_B
C     
C     BEGIN CODE
C     
C     Store all the orders that come from the diagrams, regardless
C     of the fact that they satisfy or not the squared-orders
C      constraints


C     look for orders which match the born order constraint 
      CALL SBORN_HEL_SPLITORDERS(P,ANS)
      ANS_SUMMED = 0D0
      DO J = 1, MAX_BHEL
        WGT_HEL_SUMMED(J) = 0D0
      ENDDO
      DO I = 1, NSQAMPSO
        ANS_SUMMED = ANS_SUMMED + ANS(I)
        DO J = 1, MAX_BHEL
          WGT_HEL_SUMMED(J) = WGT_HEL_SUMMED(J) + WGT_HEL(I,J)
        ENDDO
      ENDDO

      RETURN
      END


      SUBROUTINE SBORN_HEL_SPLITORDERS(P1,ANS)
C     
C     Generated by MadGraph5_aMC@NLO v. %(version)s, %(date)s
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     RETURNS AMPLITUDE SQUARED SUMMED/AVG OVER COLORS
C     AND HELICITIES
C     FOR THE POINT IN PHASE SPACE P1(0:3,NEXTERNAL-1)
C     
C     Process: d~ u > ve e+ [ all = QCD QED ] QCD^2=0 QED^2=6
C     Process: s~ c > ve e+ [ all = QCD QED ] QCD^2=0 QED^2=6
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INCLUDE 'nexternal.inc'
      INCLUDE 'born_nhel.inc'
      INTEGER     NCOMB
      PARAMETER ( NCOMB=  16 )
      INTEGER NSQAMPSO
      PARAMETER (NSQAMPSO=1)
      INTEGER    THEL
      PARAMETER (THEL=NCOMB*5)
      INTEGER NGRAPHS
      PARAMETER (NGRAPHS=   1)
C     
C     ARGUMENTS 
C     
      REAL*8 P1(0:3,NEXTERNAL-1),ANS(0:NSQAMPSO)
C     
C     LOCAL VARIABLES 
C     
      INTEGER IHEL,IDEN,I,J
      DOUBLE PRECISION T(NSQAMPSO)
      INTEGER IDEN_VALUES(5)
      DATA IDEN_VALUES /36, 36, 36, 36, 36/
C     
C     GLOBAL VARIABLES
C     
      LOGICAL GOODHEL(NCOMB,5)
      COMMON /C_GOODHEL/ GOODHEL
      DOUBLE PRECISION SAVEMOM(NEXTERNAL-1,2)
      COMMON/TO_SAVEMOM/SAVEMOM
      LOGICAL CALCULATEDBORN
      COMMON/CCALCULATEDBORN/CALCULATEDBORN
      INTEGER NFKSPROCESS
      COMMON/C_NFKSPROCESS/NFKSPROCESS
      DOUBLE PRECISION WGT_HEL(NSQAMPSO, MAX_BHEL)
      COMMON/C_BORN_HEL_SPLIT/WGT_HEL
C     ----------
C     BEGIN CODE
C     ----------
      IDEN=IDEN_VALUES(NFKSPROCESS)
      IF (CALCULATEDBORN) THEN
        DO J=1,NEXTERNAL-1
          IF (SAVEMOM(J,1).NE.P1(0,J) .OR. SAVEMOM(J,2).NE.P1(3,J))
     $      THEN
            CALCULATEDBORN=.FALSE.
            WRITE(*,*) 'Error in sborn_hel_splitorders: momenta not'
     $       //' the same in the born'
            STOP
          ENDIF
        ENDDO
      ELSE
        WRITE(*,*) 'Error in sborn_hel_splitorders: this should be'
     $   //' called only with calculatedborn = true'
        STOP
      ENDIF
      DO I=0,NSQAMPSO
        ANS(I) = 0D0
      ENDDO
      DO IHEL=1,NCOMB
        IF (GOODHEL(IHEL,NFKSPROCESS)) THEN
          CALL BORN_HEL_SPLITORDERS(P1,IHEL,T)
          DO I=1,NSQAMPSO
            WGT_HEL(I, IHEL) = T(I) / DBLE(IDEN)
            ANS(I)=ANS(I)+T(I)
          ENDDO
        ENDIF
      ENDDO
      DO I=1,NSQAMPSO
        ANS(I)=ANS(I)/DBLE(IDEN)
        ANS(0)=ANS(0)+ANS(I)
      ENDDO
      END


      SUBROUTINE BORN_HEL_SPLITORDERS(P,HELL,ANS)
C     
C     Generated by MadGraph5_aMC@NLO v. %(version)s, %(date)s
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     RETURNS AMPLITUDE SQUARED SUMMED/AVG OVER COLORS
C     FOR THE POINT WITH EXTERNAL LINES W(0:6,NEXTERNAL-1)

C     Process: d~ u > ve e+ [ all = QCD QED ] QCD^2=0 QED^2=6
C     Process: s~ c > ve e+ [ all = QCD QED ] QCD^2=0 QED^2=6
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER NAMPSO, NSQAMPSO
      PARAMETER (NAMPSO=1, NSQAMPSO=1)
      INTEGER     NGRAPHS
      PARAMETER ( NGRAPHS = 1 )
      INTEGER NCOLOR
      PARAMETER (NCOLOR=1)
      REAL*8     ZERO
      PARAMETER (ZERO=0D0)
      COMPLEX*16 IMAG1
      PARAMETER (IMAG1 = (0D0,1D0))
      INCLUDE 'nexternal.inc'
      INCLUDE 'born_nhel.inc'
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL-1)
      INTEGER HELL
      REAL*8 ANS(NSQAMPSO)
C     
C     LOCAL VARIABLES 
C     
      INTEGER I,J,M,N
      REAL*8 DENOM(NCOLOR), CF(NCOLOR,NCOLOR)
      COMPLEX*16 ZTEMP, AMP(NGRAPHS), JAMP(NCOLOR,NAMPSO)
C     
C     GLOBAL VARIABLES
C     
      DOUBLE COMPLEX SAVEAMP(NGRAPHS,MAX_BHEL)
      COMMON/TO_SAVEAMP/SAVEAMP
      LOGICAL CALCULATEDBORN
      COMMON/CCALCULATEDBORN/CALCULATEDBORN
C     
C     FUNCTION
C     
      INTEGER SQSOINDEXB
C     
C     COLOR DATA
C     
      DATA DENOM(1)/1/
      DATA (CF(I,  1),I=  1,  1) /    3/
C     1 T(1,2)
C     ----------
C     BEGIN CODE
C     ----------
      IF (.NOT. CALCULATEDBORN) THEN
        WRITE(*,*) 'Error in b_sf: color_linked borns should be called'
     $   //' only with calculatedborn = true'
        STOP
      ELSEIF (CALCULATEDBORN) THEN
        DO I=1,NGRAPHS
          AMP(I)=SAVEAMP(I,HELL)
        ENDDO
      ENDIF
C     JAMPs contributing to orders QCD=0 QED=2
      JAMP(1,1)=+AMP(1)
      DO I = 1, NSQAMPSO
        ANS(I) = 0D0
      ENDDO
      DO M = 1, NAMPSO
        DO I = 1, NCOLOR
          ZTEMP = (0.D0,0.D0)
          DO J = 1, NCOLOR
            ZTEMP = ZTEMP + CF(J,I)*JAMP(J,M)
          ENDDO
          ANS(SQSOINDEXB(M,M))=ANS(SQSOINDEXB(M,M))+ZTEMP
     $     *DCONJG(JAMP(I,M))/DENOM(I)
        ENDDO
      ENDDO
      END




      SUBROUTINE PICKHELICITYMC(P,GOODHEL,HEL,IHEL_OUT,VOL)
      IMPLICIT NONE
      INCLUDE 'nexternal.inc'
      INCLUDE 'born_nhel.inc'
      DOUBLE PRECISION P(0:3, NEXTERNAL-1)
      INTEGER GOODHEL(MAX_BHEL),HEL(0:MAX_BHEL)
      INTEGER IHEL_OUT
      DOUBLE PRECISION VOL

      INTEGER NSQAMPSO
      PARAMETER (NSQAMPSO=1)
      DOUBLE PRECISION WGT_HEL(NSQAMPSO, MAX_BHEL)
      COMMON/C_BORN_HEL_SPLIT/WGT_HEL
      DOUBLE PRECISION SUM_HEL(NSQAMPSO)
      INTEGER I, IHEL

      INTEGER N_NONZERO_ORD
      DOUBLE PRECISION SUM_ALL
      DOUBLE PRECISION ACCUM, TARGET
      DOUBLE PRECISION BORN_WGT_RECOMP_DIRECT

      DOUBLE PRECISION RAN2

      CALL SBORN_HEL(P,BORN_WGT_RECOMP_DIRECT)

C     Loop over the various orders of squared Feynman diagrams and
C      compute for each order the sum
      N_NONZERO_ORD = 0
      SUM_ALL = 0D0
      DO I = 1, NSQAMPSO
        SUM_HEL(I) = 0D0
        DO IHEL = 1, HEL(0)
          IF (WGT_HEL(I, HEL(IHEL)).LT.0D0) THEN
            WRITE(*,*) 'Helicities from squared diagrams must be > 0  !'
            STOP 1
          ENDIF
          SUM_HEL(I)=SUM_HEL(I) + WGT_HEL(I, HEL(IHEL))
     $     *DBLE(GOODHEL(IHEL))
        ENDDO
        IF (SUM_HEL(I).GT.0D0) THEN
          N_NONZERO_ORD = N_NONZERO_ORD + 1
          SUM_ALL = SUM_ALL + SUM_HEL(I)
        ENDIF
      ENDDO


      TARGET=RAN2()
      IHEL=1
      ACCUM=0D0

      DO I = 1, NSQAMPSO
        IF (SUM_HEL(I).EQ.0D0) CYCLE
        ACCUM=ACCUM+WGT_HEL(I,HEL(IHEL))/SUM_HEL(I)*DBLE(GOODHEL(IHEL))
     $   /N_NONZERO_ORD
      ENDDO

      DO WHILE (ACCUM.LT.TARGET)
        IHEL=IHEL+1
        DO I = 1, NSQAMPSO
          IF (SUM_HEL(I).EQ.0D0) CYCLE
          ACCUM=ACCUM+WGT_HEL(I,HEL(IHEL))/SUM_HEL(I)
     $     *DBLE(GOODHEL(IHEL))/N_NONZERO_ORD
        ENDDO
      ENDDO

      VOL=0D0
      DO I = 1, NSQAMPSO
        IF (SUM_HEL(I).EQ.0D0) CYCLE
        VOL=VOL+WGT_HEL(I,HEL(IHEL))/SUM_HEL(I)*DBLE(GOODHEL(IHEL))
     $   /N_NONZERO_ORD
      ENDDO


      IHEL_OUT=IHEL

      RETURN
      END



