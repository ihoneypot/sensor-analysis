# Sensor Data Analysis 

1st Assignement - Sesnsor data analyssis tool.
Python program that simulates sensor readings, analyzes the generated measurements, and visualizes the results.

## Create or activate venv

Use Python 3.10 or newer.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python sensor_monitor.py
```



## App usage file
1. select a file then select the rows to analise best case [datetime, values] order dosent matter
2. upload the file
3. the number of readings can be change if a value will be insert inside the *Number of readings*, if empty the whole file will be considered.
4. Press *Run* and the data will be visualized 

## App usage random
1. Chech the box *Random data* 
2. Select a sensor type
3. The values *Number of readings, max, min, Alert Threshold* cannot be empty, a proper error will be given if empty.
4. Press *Run* and the data will be visualized 

In both cases the data can be saved by pressing *Save*, select the foder where to save. 
Will be saved the generated or selected data to the csv file, a separate file with the result of the analysis and the plots.
