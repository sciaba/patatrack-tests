# Source local installation
export VO_CMS_SW_DIR=/data/patatrack
export SCRAM_ARCH=slc7_amd64_gcc820
source $VO_CMS_SW_DIR/cmsset_default.sh

# Set up work area
scram list CMSSW_10_6_3
cmsrel CMSSW_10_6_3_Patatrack
cd CMSSW_10_6_3_Patatrack/src

# load the environment
cmsenv

# set up a local git repository
git cms-init -x cms-patatrack
git branch CMSSW_10_6_X_Patatrack --track cms-patatrack/CMSSW_10_6_X_Patatrack
