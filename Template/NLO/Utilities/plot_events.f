c Plots the contents of a .lhe file according to a fixed-order analysis.
c Discards all weights which are not central (see do_rwgt_scale_loc and
c do_rwgt_pdf_loc).
c Works with td and HwU for the moment
      program plot_events
      implicit none
      integer maxevt,ifile,i,npart,itype
      integer IDBMUP(2),PDFGUP(2),PDFSUP(2),IDWTUP,NPRUP,LPRUP
      double precision EBMUP(2),XSECUP,XERRUP,XMAXUP
      INTEGER MAXNUP
      PARAMETER (MAXNUP=500)
      INTEGER NUP,IDPRUP,IDUP(MAXNUP),ISTUP(MAXNUP),
     # MOTHUP(2,MAXNUP),ICOLUP(2,MAXNUP)
      DOUBLE PRECISION XWGTUP,SCALUP,AQEDUP,AQCDUP,
     # PUP(5,MAXNUP),VTIMUP(MAXNUP),SPINUP(MAXNUP),
     # SCALUP_a(MAXNUP,MAXNUP)
      double precision sum_wgt,www(1000)
      integer isorh_lhe,ifks_lhe,jfks_lhe,fksfather_lhe,ipartner_lhe
      double precision scale1_lhe,scale2_lhe
      integer jwgtinfo,mexternal,iwgtnumpartn
      double precision wgtcentral,wgtmumin,wgtmumax,wgtpdfmin,wgtpdfmax
      double precision zero
      parameter (zero=0.d0)
      integer ione
      parameter (ione=1)
      character*80 event_file
      character*1000 buff
      character*9 ch1
      logical AddInfoLHE,do_rwgt_scale_loc,do_rwgt_pdf_loc
      logical usexinteg,mint
      common/cusexinteg/usexinteg,mint
      integer itmax,ncall
      common/citmax/itmax,ncall
      character*3 event_norm
      common/cevtnorm/event_norm

      include "run.inc"
      include "genps.inc"
      include "nexternal.inc"
      integer j,k
      real*8 ecm,xmass(nexternal),xmom(0:3,nexternal)
      integer ipdg(nexternal)
      character*10 MonteCarlo
      integer numscales,numPDFpairs,isc,ipdf
      common/cwgxsec1/numscales,numPDFpairs

      usexinteg=.false.
      mint=.false.
      itmax=1
      ncall=1
      call setcuts

      write (*,*) 'Enter event file name'
      read (*,*) event_file

      ifile=34
      open (unit=ifile,file=event_file,status='old')
      AddInfoLHE=.false.

      call read_lhef_header_full(ifile,maxevt,isc,ipdf,MonteCarlo)
      numscales=int(sqrt(dble(isc)))
      numPDFpairs=ipdf/2
      call read_lhef_init(ifile,
     &     IDBMUP,EBMUP,PDFGUP,PDFSUP,IDWTUP,NPRUP,
     &     XSECUP,XERRUP,XMAXUP,LPRUP)

      itype=12      
      sum_wgt=0d0
      do_rwgt_scale_loc=do_rwgt_scale
      do_rwgt_pdf_loc=do_rwgt_pdf
      do_rwgt_scale=.false.
      do_rwgt_pdf=.false.
      call set_error_estimation(0)
      call initplot
      do_rwgt_scale=do_rwgt_scale_loc
      do_rwgt_pdf=do_rwgt_pdf_loc
      do i=1,maxevt
         call read_lhef_event(ifile,
     &        NUP,IDPRUP,XWGTUP,SCALUP,AQEDUP,AQCDUP,
     &        IDUP,ISTUP,MOTHUP,ICOLUP,PUP,VTIMUP,SPINUP,
     &        buff,SCALUP_a)
c topout() in madfks_plot.f knows nothing about the overall event
c normalisation. Compensate here according to the setting of
c event_norm (read from the event file)
         if(event_norm.eq.'ave'.or.event_norm.eq.'bia')then
           www(1)=XWGTUP/maxevt
         else
           www(1)=XWGTUP
         endif
         sum_wgt=sum_wgt+www(1)

         if(i.eq.1.and.buff(1:1).eq.'#')AddInfoLHE=.true.
         if(AddInfoLHE)then
           if(buff(1:1).ne.'#')then
             write(*,*)'Inconsistency in event file',i,' ',buff
             stop
           endif
           read(buff,*)ch1,iSorH_lhe,ifks_lhe,jfks_lhe,
     #                       fksfather_lhe,ipartner_lhe,
     #                       scale1_lhe,scale2_lhe,
     #                       jwgtinfo,mexternal,iwgtnumpartn,
     #            wgtcentral,wgtmumin,wgtmumax,wgtpdfmin,wgtpdfmax
         endif

         npart=0
         do k=1,nup
           if(abs(ISTUP(k)).eq.1)then
             npart=npart+1
             ipdg(npart)=IDUP(k)
             xmass(npart)=pup(5,k)
             do j=1,4
               xmom(mod(j,4),npart)=pup(j,k)
             enddo
           endif
         enddo
         if(npart.gt.nexternal)then
           write(*,*)'Fatal error: number of particles is larger'
           write(*,*)'  than expected:',nup,npart,nexternal
           stop
         endif
         call phspncheck_nocms2(i,npart,xmass,xmom)
         do_rwgt_scale=.false.
         do_rwgt_pdf=.false.
         call outfun(xmom,zero,www,ipdg,itype)
c HwU specific -- dummy with td
         call HwU_add_points
         do_rwgt_scale=do_rwgt_scale_loc
         do_rwgt_pdf=do_rwgt_pdf_loc

      enddo

      do_rwgt_scale=.false.
      do_rwgt_pdf=.false.
c td specific -- dummy with HwU
      call mclear
c HwU specific -- dummy with td. At variance with td, the plots
c are normalised by the inverse of the argument of finalize_histograms,
c hence the choice below
      call finalize_histograms(ione)
      call topout
      do_rwgt_scale=do_rwgt_scale_loc
      do_rwgt_pdf=do_rwgt_pdf_loc

      write (*,*) 'The sum of the weights is:',sum_wgt

      end


      subroutine phspncheck_nocms2(nev,npart,xmass,xmom)
c Checks four-momentum conservation. Derived from phspncheck;
c works in any frame
      implicit none
      integer nev,npart,maxmom
      include "genps.inc"
      include "nexternal.inc"
      real*8 xmass(nexternal),xmom(0:3,nexternal)
      real*8 tiny,vtiny,xm,xlen4,den,xsum(0:3),xsuma(0:3),
     # xrat(0:3),ptmp(0:3)
      parameter (tiny=5.d-3)
      parameter (vtiny=1.d-6)
      integer jflag,i,j,jj
      double precision dot
      external dot
c
      jflag=0
      do i=0,3
        xsum(i)=-xmom(i,1)-xmom(i,2)
        xsuma(i)=abs(xmom(i,1))+abs(xmom(i,2))
        do j=3,npart
          xsum(i)=xsum(i)+xmom(i,j)
          xsuma(i)=xsuma(i)+abs(xmom(i,j))
        enddo
        if(xsuma(i).lt.1.d0)then
          xrat(i)=abs(xsum(i))
        else
          xrat(i)=abs(xsum(i))/xsuma(i)
        endif
        if(xrat(i).gt.tiny.and.jflag.eq.0)then
          write(*,*)'Momentum is not conserved [nocms]'
          write(*,*)'i=',i
          do j=1,npart
            write(*,'(4(d14.8,1x))') (xmom(jj,j),jj=0,3)
          enddo
          jflag=1
        endif
      enddo
      if(jflag.eq.1)then
        write(*,'(4(d14.8,1x))') (xsum(jj),jj=0,3)
        write(*,'(4(d14.8,1x))') (xrat(jj),jj=0,3)
        write(*,*)'event #',nev
c$$$        stop
      endif
c
      do j=1,npart
        do i=0,3
          ptmp(i)=xmom(i,j)
        enddo
        xm=xlen4(ptmp)
        if(ptmp(0).ge.1.d0)then
          den=ptmp(0)
        else
          den=1.d0
        endif
        if(abs(xm-xmass(j))/den.gt.tiny .and.
     &       abs(xm-xmass(j)).gt.tiny)then
          write(*,*)'Mass shell violation [nocms]'
          write(*,*)'j=',j
          write(*,*)'mass=',xmass(j)
          write(*,*)'mass computed=',xm
          write(*,'(4(d14.8,1x))') (xmom(jj,j),jj=0,3)
          write(*,*)'event #',nev
c$$$          stop
        endif
      enddo

      return
      end


      double precision function dot(p1,p2)
C****************************************************************************
C     4-Vector Dot product
C****************************************************************************
      implicit none
      double precision p1(0:3),p2(0:3)
      dot=p1(0)*p2(0)-p1(1)*p2(1)-p1(2)*p2(2)-p1(3)*p2(3)

      if(dabs(dot).lt.1d-6)then ! solve numerical problem 
         dot=0d0
      endif

      end


      function xlen4(v)
      implicit none
      real*8 xlen4,tmp,v(0:3)
c
      tmp=v(0)**2-v(1)**2-v(2)**2-v(3)**2
      xlen4=sign(1.d0,tmp)*sqrt(abs(tmp))
      return
      end


      subroutine boostwdir2(chybst,shybst,chybstmo,xd,xin,xout)
c chybstmo = chybst-1; if it can be computed analytically it improves
c the numerical accuracy
      implicit none
      real*8 chybst,shybst,chybstmo,xd(1:3),xin(0:3),xout(0:3)
      real*8 tmp,en,pz
      integer i
c
      if(abs(xd(1)**2+xd(2)**2+xd(3)**2-1).gt.1.d-6)then
        write(*,*)'Error #1 in boostwdir2',xd
        stop
      endif
c
      en=xin(0)
      pz=xin(1)*xd(1)+xin(2)*xd(2)+xin(3)*xd(3)
      xout(0)=en*chybst-pz*shybst
      do i=1,3
        xout(i)=xin(i)+xd(i)*(pz*chybstmo-en*shybst)
      enddo
c
      return
      end


c Dummy subroutine (normally used with vegas when resuming plots)
      subroutine resume()
      end


c Dummy routines of LHAPDF origin. Taken from ./Source/PDF/pdfwrap.f
      subroutine numberPDFm(idummy)
      implicit none
      integer idummy
      write (*,*) 'ERROR: YOU ARE IN THE numberPDFm SUBROUTINE.'
      write (*,*) 'THIS SUBROUTINE SHOULD NEVER BE USED'
      stop
      return
      end

      subroutine initPDFm(idummy1,idummy2)
      implicit none
      integer idummy1,idummy2
      write (*,*) 'ERROR: YOU ARE IN THE initPDFm SUBROUTINE.'
      write (*,*) 'THIS SUBROUTINE SHOULD NEVER BE USED'
      stop
      return
      end

      subroutine initPDFsetbynamem(idummy,cdummy)
      implicit none
      integer idummy
      character*(*) cdummy
      write (*,*) 'ERROR: YOU ARE IN THE initPDFsetbynamem SUBROUTINE.'
      write (*,*) 'THIS SUBROUTINE SHOULD NEVER BE USED'
      stop
      return
      end


c Dummy rnd number generator: called by schan_order in setcuts.f,
c and thus must not be used here.
      function ran2()
      implicit none
      double precision ran2
      write (*,*) 'ERROR: ran2() called'
      stop
      return
      end
