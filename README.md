# patatrack-tests
These instructions allow to download, install, configure and run Patatrack (https://github.com/cms-patatrack) for benchmarking purposes. These are UNOFFICIAL and the author is NOT a Patatrack developer, so they are liable to stop working if changes in Patatrack happen and are not properly taken into account here.

These instructions have been tested with CMSSW_11_1_0_pre8_Patatrack using CentOS7. The official documentation is at https://patatrack.web.cern.ch/patatrack/wiki/. Be aware that they may break due to changes in both Patatrack and the official benchmarking suite. If you encounter problems, write to Andrea.Sciaba@cern.ch.

## Prerequisites
* Operating system: CentOS7
* Hardware: an Nvidia GPU
* CVMFS installed with the CMS area accessible
* (nothing prevents from running inside a Docker container)

## Installation and setup
* Get the necessary input data:
  * `wget https://hep-benchmarks.web.cern.ch/hep-benchmarks/hep-workloads/data/cms/patatrack/opendata.tar`
  * Unpack it in a suitably large local directory (e.g. in `/data`)
* If needed, install the following dependencies:
  * `yum install -y which man file util-linux gcc wget tar freetype perl perl-Data-Dumper patch git; yum clean all`
* Clone the required repositories, this one and the one with the official benchmarking suite:
  * `git clone https://github.com/cms-patatrack/patatrack-scripts`
  * `git clone https://github.com/sciaba/patatrack-tests`
* Set up the environment
  * `export CMSSW_RELEASE=CMSSW_11_1_0_pre8_Patatrack`
  * `export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch`
  * `source $VO_CMS_SW_DIR/cmsset_default.sh`
  * `scram project CMSSW ${CMSSW_RELEASE}`
  * `cd ${CMSSW_RELEASE}`
  * `cmsenv`
  * `cd ..`
* Prepare the scripts to run the benchmark:
  * `cp patatrack-tests/*/*.patch patatrack-tests/config/sourceFromPixelRaw_cff.py patatrack-scripts/`
  * `cd patatrack-scripts/`
  * `patch -b workflow.sh workflow.patch`
  * `./workflow.sh`
  * `patch -b profile.py profile.patch`
  * Ensure that `fed_prefix` in `sourceFromPixelRaw_cff.py` corresponds to the path of the input data (e.g. `/data/store/opendata/cms`)
* Run the benchmark
  * edit the options in `benchmark` to suit your needs. In particular, make sure you specify a directory for the logs.
  * `./benchmark profile.py`
  * You can play with `./scan profile.py` and `./plot_scan scan.csv` to run the benchmark with different numbers of jobs, threads and streams and plot the results.

## Optional instructions
* In case you need to create a new input dataset:
  * Determine which dataset to use (e.g. http://opendata.cern.ch/record/12301# was used until now)
  * Edit the script `scripts/input_data.sh` in such a way that it will get the desired dataset files and edit OUTPUT_DIR to set the desired destination for the dataset
  * Run the script `scripts/input_data.sh`
  * Use cmsRun with the configuration `config/prepare_data.py` to extract the relevant FED from the input data:
  * Edit the value of `dataset_prefix` to match the value of OUTPUT_DIR.
  * Edit the value of `fed_prefix` to set the desired destination for the FED.
  * Run `cmsRun prepare_data.py` (it may take several hours for the whole dataset)
