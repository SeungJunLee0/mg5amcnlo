      SUBROUTINE SMATRIXHEL(P,HEL,ANS)
      IMPLICIT NONE
C     
C     CONSTANT
C     
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=6)
      INTEGER                 NCOMB
      PARAMETER (             NCOMB=64)
CF2PY INTENT(OUT) :: ANS
CF2PY INTENT(IN) :: HEL
CF2PY INTENT(IN) :: P(0:3,NEXTERNAL)

C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL),ANS
      INTEGER HEL
C     
C     GLOBAL VARIABLES
C     
      INTEGER USERHEL
      COMMON/HELUSERCHOICE/USERHEL
C     ----------
C     BEGIN CODE
C     ----------
      USERHEL=HEL
      CALL SMATRIX(P,ANS)
      USERHEL=-1

      END

      SUBROUTINE SMATRIX(P,ANS)
C     
C     Generated by MadGraph5_aMC@NLO v. %(version)s, %(date)s
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     MadGraph5_aMC@NLO StandAlone Version
C     
C     Returns amplitude squared summed/avg over colors
C     and helicities
C     for the point in phase space P(0:3,NEXTERNAL)
C     
C     Process: u u~ > u u~ u u~
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=6)
      INTEGER    NINITIAL
      PARAMETER (NINITIAL=2)
      INTEGER NPOLENTRIES
      PARAMETER (NPOLENTRIES=(NEXTERNAL+1)*6)
      INTEGER                 NCOMB
      PARAMETER (             NCOMB=64)
      INTEGER HELAVGFACTOR
      PARAMETER (HELAVGFACTOR=4)
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL),ANS
CF2PY INTENT(OUT) :: ANS
CF2PY INTENT(IN) :: P(0:3,NEXTERNAL)
C     
C     LOCAL VARIABLES 
C     
      INTEGER NHEL(NEXTERNAL,NCOMB),NTRY
      REAL*8 T
      REAL*8 MATRIX
      INTEGER IHEL,IDEN, I, J
C     For a 1>N process, them BEAMTWO_HELAVGFACTOR would be set to 1.
      INTEGER BEAMS_HELAVGFACTOR(2)
      DATA (BEAMS_HELAVGFACTOR(I),I=1,2)/2,2/
      INTEGER JC(NEXTERNAL)
      LOGICAL GOODHEL(NCOMB)
      DATA NTRY/0/
      DATA GOODHEL/NCOMB*.FALSE./

C     
C     GLOBAL VARIABLES
C     
      INTEGER USERHEL
      COMMON/HELUSERCHOICE/USERHEL
      DATA USERHEL/-1/

      DATA (NHEL(I,   1),I=1,6) / 1,-1,-1, 1,-1, 1/
      DATA (NHEL(I,   2),I=1,6) / 1,-1,-1, 1,-1,-1/
      DATA (NHEL(I,   3),I=1,6) / 1,-1,-1, 1, 1, 1/
      DATA (NHEL(I,   4),I=1,6) / 1,-1,-1, 1, 1,-1/
      DATA (NHEL(I,   5),I=1,6) / 1,-1,-1,-1,-1, 1/
      DATA (NHEL(I,   6),I=1,6) / 1,-1,-1,-1,-1,-1/
      DATA (NHEL(I,   7),I=1,6) / 1,-1,-1,-1, 1, 1/
      DATA (NHEL(I,   8),I=1,6) / 1,-1,-1,-1, 1,-1/
      DATA (NHEL(I,   9),I=1,6) / 1,-1, 1, 1,-1, 1/
      DATA (NHEL(I,  10),I=1,6) / 1,-1, 1, 1,-1,-1/
      DATA (NHEL(I,  11),I=1,6) / 1,-1, 1, 1, 1, 1/
      DATA (NHEL(I,  12),I=1,6) / 1,-1, 1, 1, 1,-1/
      DATA (NHEL(I,  13),I=1,6) / 1,-1, 1,-1,-1, 1/
      DATA (NHEL(I,  14),I=1,6) / 1,-1, 1,-1,-1,-1/
      DATA (NHEL(I,  15),I=1,6) / 1,-1, 1,-1, 1, 1/
      DATA (NHEL(I,  16),I=1,6) / 1,-1, 1,-1, 1,-1/
      DATA (NHEL(I,  17),I=1,6) / 1, 1,-1, 1,-1, 1/
      DATA (NHEL(I,  18),I=1,6) / 1, 1,-1, 1,-1,-1/
      DATA (NHEL(I,  19),I=1,6) / 1, 1,-1, 1, 1, 1/
      DATA (NHEL(I,  20),I=1,6) / 1, 1,-1, 1, 1,-1/
      DATA (NHEL(I,  21),I=1,6) / 1, 1,-1,-1,-1, 1/
      DATA (NHEL(I,  22),I=1,6) / 1, 1,-1,-1,-1,-1/
      DATA (NHEL(I,  23),I=1,6) / 1, 1,-1,-1, 1, 1/
      DATA (NHEL(I,  24),I=1,6) / 1, 1,-1,-1, 1,-1/
      DATA (NHEL(I,  25),I=1,6) / 1, 1, 1, 1,-1, 1/
      DATA (NHEL(I,  26),I=1,6) / 1, 1, 1, 1,-1,-1/
      DATA (NHEL(I,  27),I=1,6) / 1, 1, 1, 1, 1, 1/
      DATA (NHEL(I,  28),I=1,6) / 1, 1, 1, 1, 1,-1/
      DATA (NHEL(I,  29),I=1,6) / 1, 1, 1,-1,-1, 1/
      DATA (NHEL(I,  30),I=1,6) / 1, 1, 1,-1,-1,-1/
      DATA (NHEL(I,  31),I=1,6) / 1, 1, 1,-1, 1, 1/
      DATA (NHEL(I,  32),I=1,6) / 1, 1, 1,-1, 1,-1/
      DATA (NHEL(I,  33),I=1,6) /-1,-1,-1, 1,-1, 1/
      DATA (NHEL(I,  34),I=1,6) /-1,-1,-1, 1,-1,-1/
      DATA (NHEL(I,  35),I=1,6) /-1,-1,-1, 1, 1, 1/
      DATA (NHEL(I,  36),I=1,6) /-1,-1,-1, 1, 1,-1/
      DATA (NHEL(I,  37),I=1,6) /-1,-1,-1,-1,-1, 1/
      DATA (NHEL(I,  38),I=1,6) /-1,-1,-1,-1,-1,-1/
      DATA (NHEL(I,  39),I=1,6) /-1,-1,-1,-1, 1, 1/
      DATA (NHEL(I,  40),I=1,6) /-1,-1,-1,-1, 1,-1/
      DATA (NHEL(I,  41),I=1,6) /-1,-1, 1, 1,-1, 1/
      DATA (NHEL(I,  42),I=1,6) /-1,-1, 1, 1,-1,-1/
      DATA (NHEL(I,  43),I=1,6) /-1,-1, 1, 1, 1, 1/
      DATA (NHEL(I,  44),I=1,6) /-1,-1, 1, 1, 1,-1/
      DATA (NHEL(I,  45),I=1,6) /-1,-1, 1,-1,-1, 1/
      DATA (NHEL(I,  46),I=1,6) /-1,-1, 1,-1,-1,-1/
      DATA (NHEL(I,  47),I=1,6) /-1,-1, 1,-1, 1, 1/
      DATA (NHEL(I,  48),I=1,6) /-1,-1, 1,-1, 1,-1/
      DATA (NHEL(I,  49),I=1,6) /-1, 1,-1, 1,-1, 1/
      DATA (NHEL(I,  50),I=1,6) /-1, 1,-1, 1,-1,-1/
      DATA (NHEL(I,  51),I=1,6) /-1, 1,-1, 1, 1, 1/
      DATA (NHEL(I,  52),I=1,6) /-1, 1,-1, 1, 1,-1/
      DATA (NHEL(I,  53),I=1,6) /-1, 1,-1,-1,-1, 1/
      DATA (NHEL(I,  54),I=1,6) /-1, 1,-1,-1,-1,-1/
      DATA (NHEL(I,  55),I=1,6) /-1, 1,-1,-1, 1, 1/
      DATA (NHEL(I,  56),I=1,6) /-1, 1,-1,-1, 1,-1/
      DATA (NHEL(I,  57),I=1,6) /-1, 1, 1, 1,-1, 1/
      DATA (NHEL(I,  58),I=1,6) /-1, 1, 1, 1,-1,-1/
      DATA (NHEL(I,  59),I=1,6) /-1, 1, 1, 1, 1, 1/
      DATA (NHEL(I,  60),I=1,6) /-1, 1, 1, 1, 1,-1/
      DATA (NHEL(I,  61),I=1,6) /-1, 1, 1,-1,-1, 1/
      DATA (NHEL(I,  62),I=1,6) /-1, 1, 1,-1,-1,-1/
      DATA (NHEL(I,  63),I=1,6) /-1, 1, 1,-1, 1, 1/
      DATA (NHEL(I,  64),I=1,6) /-1, 1, 1,-1, 1,-1/
      DATA IDEN/144/

      INTEGER POLARIZATIONS(0:NEXTERNAL,0:5)
      DATA ((POLARIZATIONS(I,J),I=0,NEXTERNAL),J=0,5)/NPOLENTRIES*-1/
      COMMON/BORN_BEAM_POL/POLARIZATIONS
C     
C     FUNCTIONS
C     
      LOGICAL IS_BORN_HEL_SELECTED

C     ----------
C     BEGIN CODE
C     ----------
      IF(USERHEL.EQ.-1) NTRY=NTRY+1
      DO IHEL=1,NEXTERNAL
        JC(IHEL) = +1
      ENDDO
C     When spin-2 particles are involved, the Helicity filtering is
C      dangerous for the 2->1 topology.
C     This is because depending on the MC setup the initial PS points
C      have back-to-back initial states
C     for which some of the spin-2 helicity configurations are zero.
C      But they are no longer zero
C     if the point is boosted on the z-axis. Remember that HELAS
C      helicity amplitudes are no longer
C     lorentz invariant with expternal spin-2 particles (only the
C      helicity sum is).
C     For this reason, we simply remove the filterin when there is
C      only three external particles.
      IF (NEXTERNAL.LE.3) THEN
        DO IHEL=1,NCOMB
          GOODHEL(IHEL)=.TRUE.
        ENDDO
      ENDIF
      ANS = 0D0
      DO IHEL=1,NCOMB
        IF (USERHEL.EQ.-1.OR.USERHEL.EQ.IHEL) THEN
          IF (GOODHEL(IHEL) .OR. NTRY .LT. 20.OR.USERHEL.NE.-1) THEN
            IF(NTRY.GE.2.AND.POLARIZATIONS(0,0).NE.
     $       -1.AND.(.NOT.IS_BORN_HEL_SELECTED(IHEL))) THEN
              CYCLE
            ENDIF
            T=MATRIX(P ,NHEL(1,IHEL),JC(1))
            IF(POLARIZATIONS(0,0).EQ.-1.OR.IS_BORN_HEL_SELECTED(IHEL))
     $        THEN
              ANS=ANS+T
            ENDIF
            IF (T .NE. 0D0 .AND. .NOT.    GOODHEL(IHEL)) THEN
              GOODHEL(IHEL)=.TRUE.
            ENDIF
          ENDIF
        ENDIF
      ENDDO
      ANS=ANS/DBLE(IDEN)
      IF(USERHEL.NE.-1) THEN
        ANS=ANS*HELAVGFACTOR
      ELSE
        DO J=1,NINITIAL
          IF (POLARIZATIONS(J,0).NE.-1) THEN
            ANS=ANS*BEAMS_HELAVGFACTOR(J)
            ANS=ANS/POLARIZATIONS(J,0)
          ENDIF
        ENDDO
      ENDIF
      END


      REAL*8 FUNCTION MATRIX(P,NHEL,IC)
C     
C     Generated by MadGraph5_aMC@NLO v. %(version)s, %(date)s
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     Returns amplitude squared summed/avg over colors
C     for the point with external lines W(0:6,NEXTERNAL)
C     
C     Process: u u~ > u u~ u u~
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NGRAPHS
      PARAMETER (NGRAPHS=42)
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=6)
      INTEGER    NWAVEFUNCS, NCOLOR
      PARAMETER (NWAVEFUNCS=16, NCOLOR=6)
      REAL*8     ZERO
      PARAMETER (ZERO=0D0)
      COMPLEX*16 IMAG1
      PARAMETER (IMAG1=(0D0,1D0))
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL)
      INTEGER NHEL(NEXTERNAL), IC(NEXTERNAL)
C     
C     LOCAL VARIABLES 
C     
      INTEGER I,J
      COMPLEX*16 ZTEMP
      REAL*8 DENOM(NCOLOR), CF(NCOLOR,NCOLOR)
      COMPLEX*16 AMP(NGRAPHS), JAMP(NCOLOR)
      COMPLEX*16 W(20,NWAVEFUNCS)
      COMPLEX*16 DUM0,DUM1
      DATA DUM0, DUM1/(0D0, 0D0), (1D0, 0D0)/
C     
C     GLOBAL VARIABLES
C     
      INCLUDE 'coupl.inc'

C     
C     COLOR DATA
C     
      DATA DENOM(1)/1/
      DATA (CF(I,  1),I=  1,  6) /   27,    9,    9,    3,    3,    9/
C     1 T(2,1) T(3,4) T(5,6)
      DATA DENOM(2)/1/
      DATA (CF(I,  2),I=  1,  6) /    9,   27,    3,    9,    9,    3/
C     1 T(2,1) T(3,6) T(5,4)
      DATA DENOM(3)/1/
      DATA (CF(I,  3),I=  1,  6) /    9,    3,   27,    9,    9,    3/
C     1 T(2,4) T(3,1) T(5,6)
      DATA DENOM(4)/1/
      DATA (CF(I,  4),I=  1,  6) /    3,    9,    9,   27,    3,    9/
C     1 T(2,4) T(3,6) T(5,1)
      DATA DENOM(5)/1/
      DATA (CF(I,  5),I=  1,  6) /    3,    9,    9,    3,   27,    9/
C     1 T(2,6) T(3,1) T(5,4)
      DATA DENOM(6)/1/
      DATA (CF(I,  6),I=  1,  6) /    9,    3,    3,    9,    9,   27/
C     1 T(2,6) T(3,4) T(5,1)
C     ----------
C     BEGIN CODE
C     ----------
      CALL IXXXXX(P(0,1),ZERO,NHEL(1),+1*IC(1),W(1,1))
      CALL OXXXXX(P(0,2),ZERO,NHEL(2),-1*IC(2),W(1,2))
      CALL OXXXXX(P(0,3),ZERO,NHEL(3),+1*IC(3),W(1,3))
      CALL IXXXXX(P(0,4),ZERO,NHEL(4),-1*IC(4),W(1,4))
      CALL OXXXXX(P(0,5),ZERO,NHEL(5),+1*IC(5),W(1,5))
      CALL IXXXXX(P(0,6),ZERO,NHEL(6),-1*IC(6),W(1,6))
      CALL JIOXXX(W(1,1),W(1,2),GG,ZERO,ZERO,W(1,7))
      CALL JIOXXX(W(1,4),W(1,3),GG,ZERO,ZERO,W(1,8))
      CALL FVOXXX(W(1,5),W(1,7),GG,ZERO,ZERO,W(1,9))
C     Amplitude(s) for diagram number 1
      CALL IOVXXX(W(1,6),W(1,9),W(1,8),GG,AMP(1))
      CALL FVIXXX(W(1,6),W(1,7),GG,ZERO,ZERO,W(1,10))
C     Amplitude(s) for diagram number 2
      CALL IOVXXX(W(1,10),W(1,5),W(1,8),GG,AMP(2))
      CALL JIOXXX(W(1,6),W(1,5),GG,ZERO,ZERO,W(1,11))
C     Amplitude(s) for diagram number 3
      CALL VVVXXX(W(1,7),W(1,8),W(1,11),GG,AMP(3))
      CALL JIOXXX(W(1,6),W(1,3),GG,ZERO,ZERO,W(1,12))
      CALL FVIXXX(W(1,4),W(1,7),GG,ZERO,ZERO,W(1,13))
C     Amplitude(s) for diagram number 4
      CALL IOVXXX(W(1,13),W(1,5),W(1,12),GG,AMP(4))
C     Amplitude(s) for diagram number 5
      CALL IOVXXX(W(1,4),W(1,9),W(1,12),GG,AMP(5))
      CALL JIOXXX(W(1,4),W(1,5),GG,ZERO,ZERO,W(1,9))
C     Amplitude(s) for diagram number 6
      CALL VVVXXX(W(1,7),W(1,12),W(1,9),GG,AMP(6))
      CALL FVOXXX(W(1,3),W(1,7),GG,ZERO,ZERO,W(1,14))
C     Amplitude(s) for diagram number 7
      CALL IOVXXX(W(1,6),W(1,14),W(1,9),GG,AMP(7))
C     Amplitude(s) for diagram number 8
      CALL IOVXXX(W(1,10),W(1,3),W(1,9),GG,AMP(8))
C     Amplitude(s) for diagram number 9
      CALL IOVXXX(W(1,4),W(1,14),W(1,11),GG,AMP(9))
C     Amplitude(s) for diagram number 10
      CALL IOVXXX(W(1,13),W(1,3),W(1,11),GG,AMP(10))
      CALL JIOXXX(W(1,1),W(1,3),GG,ZERO,ZERO,W(1,13))
      CALL JIOXXX(W(1,4),W(1,2),GG,ZERO,ZERO,W(1,14))
      CALL FVOXXX(W(1,5),W(1,13),GG,ZERO,ZERO,W(1,10))
C     Amplitude(s) for diagram number 11
      CALL IOVXXX(W(1,6),W(1,10),W(1,14),GG,AMP(11))
      CALL FVIXXX(W(1,6),W(1,13),GG,ZERO,ZERO,W(1,7))
C     Amplitude(s) for diagram number 12
      CALL IOVXXX(W(1,7),W(1,5),W(1,14),GG,AMP(12))
C     Amplitude(s) for diagram number 13
      CALL VVVXXX(W(1,13),W(1,14),W(1,11),GG,AMP(13))
      CALL JIOXXX(W(1,6),W(1,2),GG,ZERO,ZERO,W(1,15))
      CALL FVIXXX(W(1,4),W(1,13),GG,ZERO,ZERO,W(1,16))
C     Amplitude(s) for diagram number 14
      CALL IOVXXX(W(1,16),W(1,5),W(1,15),GG,AMP(14))
C     Amplitude(s) for diagram number 15
      CALL IOVXXX(W(1,4),W(1,10),W(1,15),GG,AMP(15))
C     Amplitude(s) for diagram number 16
      CALL VVVXXX(W(1,13),W(1,15),W(1,9),GG,AMP(16))
      CALL FVOXXX(W(1,2),W(1,13),GG,ZERO,ZERO,W(1,10))
C     Amplitude(s) for diagram number 17
      CALL IOVXXX(W(1,6),W(1,10),W(1,9),GG,AMP(17))
C     Amplitude(s) for diagram number 18
      CALL IOVXXX(W(1,7),W(1,2),W(1,9),GG,AMP(18))
C     Amplitude(s) for diagram number 19
      CALL IOVXXX(W(1,4),W(1,10),W(1,11),GG,AMP(19))
C     Amplitude(s) for diagram number 20
      CALL IOVXXX(W(1,16),W(1,2),W(1,11),GG,AMP(20))
      CALL JIOXXX(W(1,1),W(1,5),GG,ZERO,ZERO,W(1,16))
      CALL FVOXXX(W(1,3),W(1,16),GG,ZERO,ZERO,W(1,10))
C     Amplitude(s) for diagram number 21
      CALL IOVXXX(W(1,6),W(1,10),W(1,14),GG,AMP(21))
      CALL FVIXXX(W(1,6),W(1,16),GG,ZERO,ZERO,W(1,7))
C     Amplitude(s) for diagram number 22
      CALL IOVXXX(W(1,7),W(1,3),W(1,14),GG,AMP(22))
C     Amplitude(s) for diagram number 23
      CALL VVVXXX(W(1,16),W(1,14),W(1,12),GG,AMP(23))
C     Amplitude(s) for diagram number 24
      CALL IOVXXX(W(1,4),W(1,10),W(1,15),GG,AMP(24))
      CALL FVIXXX(W(1,4),W(1,16),GG,ZERO,ZERO,W(1,10))
C     Amplitude(s) for diagram number 25
      CALL IOVXXX(W(1,10),W(1,3),W(1,15),GG,AMP(25))
C     Amplitude(s) for diagram number 26
      CALL VVVXXX(W(1,16),W(1,15),W(1,8),GG,AMP(26))
      CALL FVOXXX(W(1,2),W(1,16),GG,ZERO,ZERO,W(1,13))
C     Amplitude(s) for diagram number 27
      CALL IOVXXX(W(1,6),W(1,13),W(1,8),GG,AMP(27))
C     Amplitude(s) for diagram number 28
      CALL IOVXXX(W(1,7),W(1,2),W(1,8),GG,AMP(28))
C     Amplitude(s) for diagram number 29
      CALL IOVXXX(W(1,4),W(1,13),W(1,12),GG,AMP(29))
C     Amplitude(s) for diagram number 30
      CALL IOVXXX(W(1,10),W(1,2),W(1,12),GG,AMP(30))
      CALL FVIXXX(W(1,1),W(1,14),GG,ZERO,ZERO,W(1,10))
C     Amplitude(s) for diagram number 31
      CALL IOVXXX(W(1,10),W(1,5),W(1,12),GG,AMP(31))
      CALL FVIXXX(W(1,1),W(1,12),GG,ZERO,ZERO,W(1,13))
C     Amplitude(s) for diagram number 32
      CALL IOVXXX(W(1,13),W(1,5),W(1,14),GG,AMP(32))
C     Amplitude(s) for diagram number 33
      CALL IOVXXX(W(1,10),W(1,3),W(1,11),GG,AMP(33))
      CALL FVIXXX(W(1,1),W(1,11),GG,ZERO,ZERO,W(1,10))
C     Amplitude(s) for diagram number 34
      CALL IOVXXX(W(1,10),W(1,3),W(1,14),GG,AMP(34))
      CALL FVIXXX(W(1,1),W(1,15),GG,ZERO,ZERO,W(1,14))
C     Amplitude(s) for diagram number 35
      CALL IOVXXX(W(1,14),W(1,5),W(1,8),GG,AMP(35))
      CALL FVIXXX(W(1,1),W(1,8),GG,ZERO,ZERO,W(1,4))
C     Amplitude(s) for diagram number 36
      CALL IOVXXX(W(1,4),W(1,5),W(1,15),GG,AMP(36))
C     Amplitude(s) for diagram number 37
      CALL IOVXXX(W(1,14),W(1,3),W(1,9),GG,AMP(37))
      CALL FVIXXX(W(1,1),W(1,9),GG,ZERO,ZERO,W(1,14))
C     Amplitude(s) for diagram number 38
      CALL IOVXXX(W(1,14),W(1,3),W(1,15),GG,AMP(38))
C     Amplitude(s) for diagram number 39
      CALL IOVXXX(W(1,4),W(1,2),W(1,11),GG,AMP(39))
C     Amplitude(s) for diagram number 40
      CALL IOVXXX(W(1,10),W(1,2),W(1,8),GG,AMP(40))
C     Amplitude(s) for diagram number 41
      CALL IOVXXX(W(1,13),W(1,2),W(1,9),GG,AMP(41))
C     Amplitude(s) for diagram number 42
      CALL IOVXXX(W(1,14),W(1,2),W(1,12),GG,AMP(42))
      JAMP(1)=+1D0/4D0*(+1D0/9D0*AMP(1)+1D0/9D0*AMP(2)+1D0/3D0*AMP(4)
     $ +1D0/3D0*AMP(5)+1D0/3D0*AMP(7)+1D0/3D0*AMP(8)+1D0/9D0*AMP(9)
     $ +1D0/9D0*AMP(10)+AMP(14)-AMP(16)+AMP(17)+1D0/3D0*AMP(19)+1D0
     $ /3D0*AMP(20)+AMP(22)-AMP(23)+1D0/3D0*AMP(27)+1D0/3D0*AMP(28)
     $ +AMP(29)+AMP(31)+1D0/3D0*AMP(33)+1D0/3D0*AMP(34)+1D0/3D0*AMP(35)
     $ +1D0/3D0*AMP(36)+AMP(37)+1D0/9D0*AMP(39)+1D0/9D0*AMP(40))
      JAMP(2)=+1D0/4D0*(-1D0/3D0*AMP(1)-1D0/3D0*AMP(2)-1D0/9D0*AMP(4)
     $ -1D0/9D0*AMP(5)-1D0/9D0*AMP(7)-1D0/9D0*AMP(8)-1D0/3D0*AMP(9)
     $ -1D0/3D0*AMP(10)-AMP(12)+AMP(13)-1D0/3D0*AMP(17)-1D0/3D0*AMP(18)
     $ -AMP(19)-AMP(25)+AMP(26)-AMP(27)-1D0/3D0*AMP(29)-1D0/3D0*AMP(30)
     $ -1D0/3D0*AMP(31)-1D0/3D0*AMP(32)-AMP(33)-AMP(35)-1D0/3D0*AMP(37)
     $ -1D0/3D0*AMP(38)-1D0/9D0*AMP(41)-1D0/9D0*AMP(42))
      JAMP(3)=+1D0/4D0*(-AMP(4)+AMP(6)-AMP(7)-1D0/3D0*AMP(9)-1D0/3D0
     $ *AMP(10)-1D0/9D0*AMP(11)-1D0/9D0*AMP(12)-1D0/3D0*AMP(14)-1D0
     $ /3D0*AMP(15)-1D0/3D0*AMP(17)-1D0/3D0*AMP(18)-1D0/9D0*AMP(19)
     $ -1D0/9D0*AMP(20)-1D0/3D0*AMP(21)-1D0/3D0*AMP(22)-AMP(24)-AMP(26)
     $ -AMP(28)-1D0/3D0*AMP(31)-1D0/3D0*AMP(32)-1D0/9D0*AMP(33)-1D0
     $ /9D0*AMP(34)-AMP(36)-1D0/3D0*AMP(39)-1D0/3D0*AMP(40)-AMP(41))
      JAMP(4)=+1D0/4D0*(+AMP(1)+AMP(3)+1D0/3D0*AMP(4)+1D0/3D0*AMP(5)
     $ +AMP(10)+1D0/3D0*AMP(11)+1D0/3D0*AMP(12)+AMP(15)+AMP(16)+AMP(18)
     $ +1D0/9D0*AMP(21)+1D0/9D0*AMP(22)+1D0/3D0*AMP(24)+1D0/3D0*AMP(25)
     $ +1D0/3D0*AMP(27)+1D0/3D0*AMP(28)+1D0/9D0*AMP(29)+1D0/9D0*AMP(30)
     $ +1D0/9D0*AMP(31)+1D0/9D0*AMP(32)+1D0/3D0*AMP(33)+1D0/3D0*AMP(34)
     $ +AMP(38)+AMP(40)+1D0/3D0*AMP(41)+1D0/3D0*AMP(42))
      JAMP(5)=+1D0/4D0*(+AMP(2)-AMP(3)+1D0/3D0*AMP(7)+1D0/3D0*AMP(8)
     $ +AMP(9)+1D0/3D0*AMP(11)+1D0/3D0*AMP(12)+1D0/9D0*AMP(14)+1D0/9D0
     $ *AMP(15)+1D0/9D0*AMP(17)+1D0/9D0*AMP(18)+1D0/3D0*AMP(19)+1D0
     $ /3D0*AMP(20)+AMP(21)+AMP(23)+1D0/3D0*AMP(24)+1D0/3D0*AMP(25)
     $ +AMP(30)+AMP(32)+1D0/3D0*AMP(35)+1D0/3D0*AMP(36)+1D0/9D0*AMP(37)
     $ +1D0/9D0*AMP(38)+AMP(39)+1D0/3D0*AMP(41)+1D0/3D0*AMP(42))
      JAMP(6)=+1D0/4D0*(-1D0/3D0*AMP(1)-1D0/3D0*AMP(2)-AMP(5)-AMP(6)
     $ -AMP(8)-AMP(11)-AMP(13)-1D0/3D0*AMP(14)-1D0/3D0*AMP(15)-AMP(20)
     $ -1D0/3D0*AMP(21)-1D0/3D0*AMP(22)-1D0/9D0*AMP(24)-1D0/9D0*AMP(25)
     $ -1D0/9D0*AMP(27)-1D0/9D0*AMP(28)-1D0/3D0*AMP(29)-1D0/3D0*AMP(30)
     $ -AMP(34)-1D0/9D0*AMP(35)-1D0/9D0*AMP(36)-1D0/3D0*AMP(37)-1D0
     $ /3D0*AMP(38)-1D0/3D0*AMP(39)-1D0/3D0*AMP(40)-AMP(42))

      MATRIX = 0.D0
      DO I = 1, NCOLOR
        ZTEMP = (0.D0,0.D0)
        DO J = 1, NCOLOR
          ZTEMP = ZTEMP + CF(J,I)*JAMP(J)
        ENDDO
        MATRIX = MATRIX+ZTEMP*DCONJG(JAMP(I))/DENOM(I)
      ENDDO

      END

      SUBROUTINE GET_ME(P, ALPHAS, NHEL ,ANS)
      IMPLICIT NONE
C     
C     CONSTANT
C     
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=6)
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL),ANS
      INTEGER NHEL
      DOUBLE PRECISION ALPHAS
      REAL*8 PI
CF2PY INTENT(OUT) :: ANS
CF2PY INTENT(IN) :: NHEL
CF2PY INTENT(IN) :: P(0:3,NEXTERNAL)
CF2PY INTENT(IN) :: ALPHAS
C     ROUTINE FOR F2PY to read the benchmark point.    
C     the include file with the values of the parameters and masses 
      INCLUDE 'coupl.inc'

      PI = 3.141592653589793D0
      G = 2* DSQRT(ALPHAS*PI)
      CALL UPDATE_AS_PARAM()
      IF (NHEL.NE.0) THEN
        CALL SMATRIXHEL(P, NHEL, ANS)
      ELSE
        CALL SMATRIX(P, ANS)
      ENDIF
      RETURN
      END

      SUBROUTINE INITIALISE(PATH)
C     ROUTINE FOR F2PY to read the benchmark point.    
      IMPLICIT NONE
      CHARACTER*180 PATH
CF2PY INTENT(IN) :: PATH
      CALL SETPARA(PATH)  !first call to setup the paramaters    
      RETURN
      END

      LOGICAL FUNCTION IS_BORN_HEL_SELECTED(HELID)
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NEXTERNAL
      PARAMETER (NEXTERNAL=6)
      INTEGER    NCOMB
      PARAMETER (NCOMB=64)
C     
C     ARGUMENTS
C     
      INTEGER HELID
C     
C     LOCALS
C     
      INTEGER I,J
      LOGICAL FOUNDIT
C     
C     GLOBALS
C     
      INTEGER HELC(NEXTERNAL,NCOMB)
      COMMON/BORN_HEL_CONFIGS/HELC

      INTEGER POLARIZATIONS(0:NEXTERNAL,0:5)
      COMMON/BORN_BEAM_POL/POLARIZATIONS
C     ----------
C     BEGIN CODE
C     ----------

      IS_BORN_HEL_SELECTED = .TRUE.
      IF (POLARIZATIONS(0,0).EQ.-1) THEN
        RETURN
      ENDIF

      DO I=1,NEXTERNAL
        IF (POLARIZATIONS(I,0).EQ.-1) THEN
          CYCLE
        ENDIF
        FOUNDIT = .FALSE.
        DO J=1,POLARIZATIONS(I,0)
          IF (HELC(I,HELID).EQ.POLARIZATIONS(I,J)) THEN
            FOUNDIT = .TRUE.
            EXIT
          ENDIF
        ENDDO
        IF(.NOT.FOUNDIT) THEN
          IS_BORN_HEL_SELECTED = .FALSE.
          RETURN
        ENDIF
      ENDDO

      RETURN
      END

