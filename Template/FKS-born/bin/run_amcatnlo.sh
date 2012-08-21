#! /bin/bash

echo '****************************************************'
echo 'This script runs an amcatnlo process'
echo '****************************************************'

# find the correct directory
if [[  ! -d ./SubProcesses  ]]; then
    cd ../
    if [[ ! -d ./SubProcesses ]]; then
	echo "Error: run_amcatnlo.sh must be executed from the main, or bin directory"
	exit
    fi
fi

Maindir=`pwd`

run_mode=$1
use_preset=$2
run_cluster=$3
mint_mode=$4

if [[ $run_mode == "" ]] ; then
    echo 'Enter run mode (F, V or B)'
    read run_mode
fi
if [[ -e! madinMMC_$run_mode.2 ]] ; then
    echo 'Cannot read the inputs. File not found: madinMMC_'$run_mode'.2'
    exit
fi

if [[ $use_preset == "" ]] ; then
    echo "Enter presets used for integration grids (none, F, B or V)"
    echo "   [Default is 'none']"
    read use_preset
fi
if [[ $use_preset == "none" ]] ; then
    echo "No preset used"
    use_preset=""
else
    echo "Using preset:" $use_preset
fi

if [[ $run_cluster == "" ]] ; then
    echo "Local run (0), cluster running (1) or ganga (2)?"
#    echo "Cluster running needs a configured condor batching system"
    read run_cluster
fi
if [[ $run_cluster == 0 ]] ; then
    echo "Running locally"
elif [[ $run_cluster == 1 ]] ; then
    echo "submitting jobs to cluster"
elif [[ $run_cluster == 2 ]] ; then
    echo "using ganga to submit jobs"
else
    echo "ERROR" $run_cluster
    exit
fi

if [[ $mint_mode == "" ]] ; then
    echo "Enter the mint MODE"
    read mint_mode
fi

cd $Maindir/SubProcesses/
if [[ $mint_mode == 0 ]] ; then
    echo "setting-up integration grids"
    sed -i ".bak" "8s/.*/0/" madinMMC_$run_mode.2
elif [[ $mint_mode == 1 ]] ; then
    echo "computing upper bounding envelope"
    sed -i ".bak" "8s/.*/1/" madinMMC_$run_mode.2
elif [[ $mint_mode == 2 ]] ; then
    echo "generating events"
    sed -i ".bak" "8s/.*/2/" madinMMC_$run_mode.2
else
    echo "ERROR" $mint_mode
fi
cd $Maindir/

#---------------------------
# Update random number seed
cd $Maindir/SubProcesses/
r=0
if [[ -e randinit ]]; then
    source ./randinit
fi
for i in P*_* ; do
    r=`expr $r + 1`
done
echo "r=$r" >& randinit
cd $Maindir


vegas_mint="2"

cd SubProcesses

for dir in P*_* ; do
    cd $dir
    echo $dir
    if [[ -e madevent_mintMC ]]; then
	chmod +x ajob*
	if [[ $run_cluster == 1 ]] ; then
	    for job in mg*.cmd ; do
		sed -i "7s/.*/Arguments = $vegas_mint $run_mode $mint_mode $use_preset/" $job
		condor_submit $job
	    done
	elif [[ $run_cluster == 0 ]] ; then
	    echo "Doing "$run_mode"-events in this dir"
	    for job in ajob* ; do
		./$job $vegas_mint $run_mode $mint_mode $use_preset
	    done
	fi
    else
	echo 'madevent_mintMC does not exist. Skipping directory'
    fi
    echo ''
    cd ..
done

cd ..

