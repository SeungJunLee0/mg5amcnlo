#! /usr/bin/env python
################################################################################
#
# Copyright (c) 2009 The MadGraph5_aMC@NLO Development team and Contributors
#
# This file is a part of the MadGraph5_aMC@NLO project, an application which 
# automatically generates Feynman diagrams and matrix elements for arbitrary
# high-energy processes in the Standard Model and beyond.
#
# It is subject to the MadGraph5_aMC@NLO license which should accompany this 
# distribution.
#
# For more information, visit madgraph.phys.ucl.ac.be and amcatnlo.web.cern.ch
#
################################################################################
import os
import sys
import logging
import time
# Get the parent directory (mg root) of the script real path (bin)
# and add it to the current PYTHONPATH
root_path = os.path.split(os.path.dirname(os.path.realpath( __file__ )))[0]
sys.path.append(root_path)

from madgraph import MG5DIR
import madgraph.iolibs.import_v4 as import_v4
import madgraph.interface.master_interface as interface
import models.import_ufo as import_ufo
import aloha.create_aloha as create_aloha
import madgraph.iolibs.files as files
import madgraph.various.misc as misc

# Set logging level to error
logging.basicConfig(level=vars(logging)['INFO'],
                    format="%(message)s")
pjoin = os.path.join

class Compile_MG5:
    
    def __init__(self):
        """ launch all the compilation """

        self.make_UFO_pkl()
        self.make_v4_pkl()
        self.make_stdHep()
        self.make_CutTools()

        #important for UCL cluster
        files.cp(pjoin(MG5DIR,'input','.mg5_configuration_default.txt'),
                 pjoin(MG5DIR,'input','mg5_configuration.txt'))
        self.cmd = interface.MasterCmd()        
        self.install_package()

    @staticmethod
    def make_v4_pkl():
        """create the model.pkl for each directory"""
        file_cond = lambda p :  (os.path.exists(os.path.join(MG5DIR,'models',p,'particles.dat'))) 
        #1. find v4 model:
        v4_model = [os.path.join(MG5DIR,'models',p) 
                        for p in os.listdir(os.path.join(MG5DIR,'models')) 
                            if file_cond(p)]
            
        for model_path in v4_model:
            #remove old pkl
            start = time.time()
            print 'make pkl for %s :' % os.path.basename(model_path),
            try:
                os.remove(os.path.join(model_path,'model.pkl'))
            except:
                pass
            import_v4.import_model(model_path)
            print '%2fs' % (time.time() - start)
    
    @staticmethod
    def make_UFO_pkl():
        """ """
        file_cond = lambda p : os.path.exists(os.path.join(MG5DIR,'models',p,'particles.py'))
        #1. find UFO model:
        ufo_model = [os.path.join(MG5DIR,'models',p) 
                        for p in os.listdir(os.path.join(MG5DIR,'models')) 
                            if file_cond(p)]
        # model.pkl
        for model_path in ufo_model:
            start = time.time()
            print 'make model.pkl for %s :' % os.path.basename(model_path),
            #remove old pkl
            try:
                os.remove(os.path.join(model_path,'model.pkl'))
            except:
                pass
            import_ufo.import_full_model(model_path)
            print '%2fs' % (time.time() - start)
        
        return
        # aloha routine 
        for model_path in ufo_model:
            start = time.time()
            print 'make ALOHA for %s' % os.path.basename(model_path)
            #remove old pkl
            try:
                os.remove(os.path.join(model_path,'aloha.pkl'))
            except:
                pass    
            try:
                os.system('rm -rf %s &> /dev/null' % os.path.join(model_path,'Fortran'))
            except:
                pass            
            
            ufo_path, ufo_name =os.path.split(model_path)
            sys.path.insert(0, ufo_path)
            output_dir = os.path.join(model_path, 'Fortran')
            create_aloha.AbstractALOHAModel(ufo_name, write_dir=output_dir, format='Fortran')
            print 'done in %2fs' % (time.time() - start)
           
    @staticmethod
    def make_stdHep():
        print "Compiling StdHEP in %s."%str(os.path.join(MG5DIR, 'vendor', 'StdHEP'))
        # this is for 64-bit systems
        if sys.maxsize > 2**32:
            path = os.path.join(MG5DIR, 'vendor', 'StdHEP', 'src', 'make_opts')
            text = open(path).read()
            text = text.replace('MBITS=32','MBITS=64')
            open(path, 'w').writelines(text)
        # Set the correct fortran compiler
        if 'FC' not in os.environ or not os.environ['FC']:
            if misc.which('gfortran'):
                compiler = 'FC=gfortran'
            elif misc.which('g77'):
                compiler = 'FC=g77'
            else:
                raise self.InvalidCmd('Require g77 or Gfortran compiler')
        else:
            compiler = '#FC=gfortran'

        base_compiler= ['FC=g77','FC=gfortran','#FC=g77','#FC=gfortran']
        path = None            
        path = os.path.join(MG5DIR, 'vendor', 'StdHEP', 'src', 'make_opts')
        text = open(path).read()
        for base in base_compiler:
            text = text.replace(base,compiler)
        open(path, 'w').writelines(text)

        misc.compile(cwd = os.path.join(MG5DIR, 'vendor', 'StdHEP'))

    @staticmethod
    def make_CutTools():
        print "Compiling CutTools in %s."%str(os.path.join(MG5DIR, 'vendor', 'CutTools'))
        # Set the correct fortran compiler
        if 'FC' not in os.environ or not os.environ['FC']:
            if misc.which('gfortran'):
                compiler = 'FC=gfortran'
            else:
                raise self.InvalidCmd('Require gfortran compiler')
        else:
            compiler = '#FC=gfortran'
        
        base_compiler= ['FC=gfortran','#FC=gfortran']            
        path = None            
        path = os.path.join(MG5DIR, 'vendor', 'CutTools', 'makefile')
        text = open(path).read()
        for base in base_compiler:
            text = text.replace(base,compiler)
        open(path, 'w').writelines(text)

        misc.compile(cwd = os.path.join(MG5DIR, 'vendor', 'CutTools'))

    def install_package(self):
        print "installing external package"
        self.cmd.exec_cmd('install pythia-pgs')
        self.cmd.exec_cmd('install Delphes')
        self.cmd.exec_cmd('install ExRootAnalysis')
        self.cmd.exec_cmd('install MadAnalysis')
        self.cmd.exec_cmd('install SysCalc')

if __name__ == '__main__':
    Compile_MG5()
