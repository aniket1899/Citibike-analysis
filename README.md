# Citibike-analysis
Citibike data analysis for NYC using Hadoop and Hive. Data visualization with Tableau. 
Size of the entire dataset - 15 GB
---


### Data
The data was downloaded from Citibike's web portal using the 'requests' library in Python and unzips them. The data was collected for the period 2019-2022. 


### Data aggregation - using MapReduce
* Count ride, age, start times (hours) counts for each month for each year.
* Count ride, age, start times (hours) sum of trip durations for each month for each year.

#### Using Hive SQL queries to analyse trip summaries. 
* Calculating trip summaries using start and stop times with aggregated trip durations. 

### Data aggregation - using PySpark
* Extract 'month', 'time of day', 'time of day - Morning/Afternoon/Evening/Night' from date.
* Aggregate data for all monmths for all years-
> 1. Demographics: ['Birth year', 'Gender', 'Time of day'] aggregated on sum('Trip duration')
> 2. Trip details: ['Start station', 'End Station', 'Time of day - bucketed'] aggregated on sum('Trip duration')

### Visualization
* Using these sum aggragations, averages are calculated by maintaining counts for all groups.
* Utilizing a NYC Subway Map to locate all stations in the choropleth. 
