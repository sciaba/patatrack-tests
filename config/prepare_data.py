import os
import FWCore.ParameterSet.Config as cms

process = cms.Process("FED")

dataset_prefix = 'file:/data/store/opendata/cms'
dataset_path = 'MonteCarloUpgrade/RunIIAutumn18DR/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/PUAvg50IdealConditions_IdealConditions_102X_upgrade2018_design_v9_ext1-v2/260000'
prefix = dataset_prefix + '/' + dataset_path + '/'
fed_prefix = '/data/store/opendata/cms'
fed_path = 'MonteCarloUpgrade/RunIIAutumn18DR/TTToHadronic_TuneCP5_13TeV-powheg-pythia8'
fed_basedir = fed_prefix + '/' + fed_path

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(prefix + '206A6E9A-4DB2-1941-A60B-7174FA398D86.root',
   prefix + '23BAC38C-A5CD-4844-8EA5-C7B5AA443861.root',
   prefix + '3C001F42-8E40-7B41-BA3B-780714F6ABBD.root',
   prefix + '4978A440-0E12-8541-86B8-81086CDC98A0.root',
   prefix + '5163175A-C833-534E-9197-A275A38A78E2.root',
   prefix + '60FF74A6-2B35-1243-BDCB-282EC3A1D961.root',
   prefix + '6D6E7EAA-5553-C440-B6BD-E8FF165CADC2.root',
   prefix + '6EEA5B7D-3D49-5F42-856F-AB11593D6EB5.root',
   prefix + '715C11D3-94C5-5945-A295-DD120D8697F4.root',
   prefix + '76E5A405-B666-444B-A086-C9D102519D96.root',
   prefix + '834227F5-C683-AC43-86C8-96A0642376DF.root',
   prefix + '83560C49-46DD-9C49-AB5A-6D72053E8CC3.root',
   prefix + '86C39A48-D56F-3741-929C-6C72DCA015D7.root',
   prefix + '8727F95B-0A35-D24B-A957-81391C5EE7D9.root',
   prefix + '95F7275E-3A4D-CF42-9F6C-84F4EF4ECAFF.root',
   prefix + '9DA43473-81B2-EB42-BF52-FE7C1DE0857B.root',
   prefix + '9E4F2FEA-B27D-0E47-AE5B-74D01EE8CE51.root',
   prefix + '9FBCC652-F2E5-1348-AB39-C74B46F2BB8D.root',
   prefix + 'A9FB61CD-4A96-E645-B56B-AA8037DB9118.root',
   prefix + 'AD86C759-277C-124F-95BA-F4DD7BA838AD.root',
   prefix + 'B2E83B4E-5136-6240-B6C5-C36B1728716C.root',
   prefix + 'BE332030-68F5-2A46-97D5-F851A69AB3BA.root',
   prefix + 'CD903778-801D-CA4A-B73A-ACAA54BA3D74.root',
   prefix + 'CE277B72-55FC-6A42-98DE-AB9CB048A517.root',
   prefix + 'D2FF2B84-7404-614C-961A-AC0BE5E98F65.root',
   prefix + 'D4B3768F-C95E-E249-ADDC-A608EDD26EB8.root',
   prefix + 'E0802B57-98A4-DA4E-96BF-F7D90DF1B786.root',
   prefix + 'E0968F76-5E44-0A4C-AC6F-1222662E57E0.root',
   prefix + 'E7AF7B47-7A09-A441-B255-DCE8D46C954E.root',
   prefix + 'E9740D7E-F61D-4D40-A1E7-6A8A6D647D94.root',
   prefix + 'EDD5D9BB-5E52-454A-AF1A-63391379C76A.root',
   prefix + 'F68115D9-E295-DA4E-8DB0-15520D79107F.root')
)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.load('EventFilter.Utilities.EvFDaqDirector_cfi')
process.EvFDaqDirector.baseDir   = fed_basedir
process.EvFDaqDirector.buBaseDir = fed_basedir
process.EvFDaqDirector.runNumber = 1

# create a fake BU lock file
import os.path
workdir = '%s/run%06d/open' % (process.EvFDaqDirector.baseDir.value(), process.EvFDaqDirector.runNumber.value())
if not os.path.isdir(workdir):
	  os.makedirs(workdir)
	  open(workdir + '/fu.lock', 'w').close()

process.rawStreamFileWriterForBU = cms.OutputModule("RawStreamFileWriterForBU",
		    ProductLabel = cms.untracked.string("rawDataCollector"),
		        numEventsPerFile = cms.untracked.uint32(100),
			    jsonDefLocation = cms.untracked.string(os.path.expandvars('$CMSSW_RELEASE_BASE/src/EventFilter/Utilities/plugins/budef.jsd')),
			        debug = cms.untracked.bool(False),
				)

process.endpath = cms.EndPath(process.rawStreamFileWriterForBU)

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.rawDataSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32(
        # SCAL
          735,
        # TCDS FED
         1024,
        # Pixel FEDs, barrel plus
         1200, 1201, 1202, 1203, 1204, 1205, 1206, 1207, 1208, 1209, # 11200,
         1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, # 11212,
         1224, 1225, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, # 11224,
         1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, # 11236,
        # Pixel FEDs, barrel minus
         1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, # 11248,
         1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, # 11260,
         1272, 1273, 1274, 1275, 1276, 1277, 1278, 1279, 1280, 1281, # 11272,
         1284, 1285, 1286, 1287, 1288, 1289, 1290, 1291, 1292, 1293, # 11284,
        # Pixel FEDs, endcap plus
         1296, 1297, 1298, 1299, 1300, 1301, 1302, # 11296,
         1308, 1309, 1310, 1311, 1312, 1313, 1314, # 11308,
        # Pixel FEDs, endcap minus
         1320, 1321, 1322, 1323, 1324, 1325, 1326, # 11320,
         1332, 1333, 1334, 1335, 1336, 1337, 1338, # 11332,
    )
)
process.path = cms.Path(process.rawDataSelector)

process.rawStreamFileWriterForBU.ProductLabel = "rawDataSelector"
