# cse6242-F1
Semester project, F1 stats
This package pulls F1 race data from Fast F1 python package and can store it in google 
cloud services. It can then pull that data down locally and sort it into its respictive 
parque files. This data includes telemetry and overall race day statistics. 

The rest of the package creates a visualization on the data. The package used to do this
is streamlit. This creates an interactive website for someone to visualize the experiments
we conducted on the data. The first page of the streamlit app breaks the data down by race.
It used the other files in the package to create plots. The main analysis on drivers is done
on overtakes and tires. The streamlite does a deep dive on what drivers are the most efficient
overtakers in either a race or season. It also analyzes different tire compositions versus 
lap times.

## Description of Files
* `load_data.py` Loops through all races in fastf1 and loads to cache
* `process_data.py` Merges data from cache and produces parquet datasets
* `gcp.ipynb` reads in data from google cloud
* `race_st.py` holds code to launch streamlit app
* `overtake_analysis.py` creates overtake bar plots
* `overatake_experiment.py` Summary overtake visualizations for a season
* `plot_overtake.py` creates overtake points graph
* `tire_analysis` creates plots for tires
* `Track_satView` creates world map of tracks
* `utils.py` assists with data manipulation

## GCS Bucket cse6242-f1-data:
See `gcp.ipynb` for reading data

* /datasets: merged all race data into a single parquet dataset for each data type
* /2018 - /2022: fastf1 cache data for all races

## Creating environment
Use a environment.yml to create conda environment to ensure the app works. Here are the
dependencies listed in file in case of using another environment.
  - python=3.9
  - streamlit
  - plotly
  - scikit-learn
  - matplotlib
Here are the commands needed to create then activate the conda environment. Make sure you are in the
directory where the environment.yml file is held.
>> conda env create -f environment.yml
>> conda activate F1ST

## Launching app
Go to terminal or prompt that your environment is in. Enter the directory the python
and data files are held and run the below command.
>> streamlit run race_st.py

If you are using a non conda enviroment you may need to run
>> python3 -m streamlit run race_st.py

## Using app
Once the app is up it is very simple to explore. Everything is based off of the select box
filters. You can select a race and year and the data will change to that respective race.
Drivers can also be selected for the overtake map and tires analysis. On the left hand pane,
you can change to the season's page. It works in the same way but has no race filter, it only
shows season level statistics.

## Video Instructions Link
https://youtu.be/3gcMDeX5Xok