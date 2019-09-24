#! /bin/bash

# Bootstrap
export LANG=C
export VO_CMS_SW_DIR=/data/patatrack
export SCRAM_ARCH=slc7_amd64_gcc820
mkdir -p $VO_CMS_SW_DIR
wget http://cmsrep.cern.ch/cmssw/bootstrap.sh -O $VO_CMS_SW_DIR/bootstrap.sh
chmod a+x $VO_CMS_SW_DIR/bootstrap.sh
$VO_CMS_SW_DIR/bootstrap.sh -a $SCRAM_ARCH -r cms -path $VO_CMS_SW_DIR setup
if [[ $? -ne 0 ]] ; then
    echo "[ERROR] Could not bootstrap installation"
    exit 1
fi

# CMSSW installation
$VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH upgrade -y
$VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH install -y cms+cmssw+CMSSW_10_6_3
$VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH install -y cms+cmssw-tool-conf+45.0-nmpfii8

# Patatrack installation
$VO_CMS_SW_DIR/common/cmspkg -a $SCRAM_ARCH -r cms.patatrack install -y cms+cmssw+CMSSW_10_6_3_Patatrack
