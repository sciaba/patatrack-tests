# patatrack-tests
These instructions allow to download, install, configure and run Patatrack for benchmarking purposes.
## Installation and setup
* Use the script scripts/install.sh to install CMSSW and Patatrack on a local directory.
  * Edit the value of VO_CMS_SW_DIR to point to a directory with at least 100 GB of free space.
  * Run the script.
* Use the script scripts/work.sh to prepare the work area for Patatrack.
  * Edit the value of VO_CMS_SW_DIR to point to the same directory as before.
  * (for CERN) make sure you have a Kerberos token and run kinit.
  * Run the script.
* Use the script input_data.sh to download the required open data to be used as input.
  * Edit $OUTPUT_DIR to set the desired destination for the dataset.
  * Run the script.
* Use cmsRun with the configuration config/prepare_data.py to extract the relevant FED from the input data.
  * Edit the value of basedir to match the value of OUTPUT_DIR.
  * Run cmsRun prepare_data.py
