import FWCore.ParameterSet.Config as cms

import glob
fed_prefix = '/data/store/opendata/cms'
fed_path = 'MonteCarloUpgrade/RunIIAutumn18DR/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/run000001'
fed_basedir = fed_prefix + '/' + fed_path
fed_files = glob.glob(fed_basedir + '/*.raw')

# input
FastMonitoringService = cms.Service( "FastMonitoringService",
    filePerFwkStream = cms.untracked.bool( False ),
    fastMonIntervals = cms.untracked.uint32( 2 ),
    sleepTime = cms.untracked.int32( 1 )
)

EvFDaqDirector = cms.Service( "EvFDaqDirector",
    runNumber = cms.untracked.uint32( 1 ),

    baseDir = cms.untracked.string( "tmp" ),
    buBaseDir = cms.untracked.string( "tmp" ),

    useFileBroker = cms.untracked.bool( False ),
    fileBrokerKeepAlive = cms.untracked.bool( True ),
    fileBrokerPort = cms.untracked.string( "8080" ),
    fileBrokerUseLocalLock = cms.untracked.bool( True ),
    fuLockPollInterval = cms.untracked.uint32( 2000 ),

    requireTransfersPSet = cms.untracked.bool( False ),
    selectedTransferMode = cms.untracked.string( "" ),
    mergingPset = cms.untracked.string( "" ),

    outputAdler32Recheck = cms.untracked.bool( False ),
)

source = cms.Source( "FedRawDataInputSource",
    runNumber = cms.untracked.uint32( 1 ),
    getLSFromFilename = cms.untracked.bool(True),
    testModeNoBuilderUnit = cms.untracked.bool(False),
    verifyAdler32 = cms.untracked.bool( True ),
    verifyChecksum = cms.untracked.bool( True ),
    alwaysStartFromfirstLS = cms.untracked.uint32( 0 ),

    useL1EventID = cms.untracked.bool( True ),          # True for MC, True/False for data
    eventChunkBlock = cms.untracked.uint32( 240 ),      # 32
    eventChunkSize = cms.untracked.uint32( 240),        # 32
    maxBufferedFiles = cms.untracked.uint32( 8 ),       #  2
    numBuffers = cms.untracked.uint32( 8 ),             #  2

    fileListMode = cms.untracked.bool( True ),          # False
                     fileNames = cms.untracked.vstring(*fed_files),
)
