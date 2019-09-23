# patatrack-tests
These instructions allow to download, install, configure and run Patatrack for benchmarking purposes.
## Installation and setup
* Use the script scripts/install.sh to install CMSSW and Patatrack on a local directory.
  * Edit the value of VO_CMS_SW_DIR to point to a directory with at least 40 GB of free space.
  * Run the script.
* Use the script scripts/work.sh to prepare the work area for Patatrack and source the CMSSW environment.
  * Edit the value of VO_CMS_SW_DIR to point to the same directory as before.
  * (for CERN) make sure you have a Kerberos token and run kinit.
  * Run `source work.sh`
* Use the script input_data.sh to download the required open data to be used as input.
  * Edit $OUTPUT_DIR to set the desired destination for the dataset (which consists of 20000 events, 32 files and 553.5 GB of data, see http://opendata.cern.ch/record/12301#).
  * Run the script
* Use cmsRun with the configuration config/prepare_data.py to extract the relevant FED from the input data.
  * Edit the value of dataset_prefix to match the value of OUTPUT_DIR.
  * Edit the value of fed_prefix to set the desired destination for the FED (the size of the output will be approximately 5 GB).
  * Run `cmsRun prepare_data.py` (it should take around 10 hours for the whole dataset)
## Running Patatrack
* Get the Patatrack benchmarking suite
  * Run `git clone https://github.com/cms-patatrack/patatrack-scripts`
  * Patch `worflow.sh` with the patch file in scripts/ by doing
    * `patch -b workflow.sh workflow.patch`
    * Generate the workflow by running `./workflow.sh`
  * Patch `profile.py` with the patch file in config/ by doing
    * `patch -b profile.py profile.patch`
  * Copy the configuration `config/sourceFromPixelRaw_cff.py` locally
  * Edit the options in `benchmark` to suit your needs
  * Run the benchmark by doing `./benchmark profile.sh`
