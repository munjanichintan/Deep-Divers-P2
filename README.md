# Deep-Divers-P2

## Project Description

Creating Spark jobs in Python (using PySpark) to perform various analysis on a Hotel Booking dataset stored in HDFS in csv format.

## Technologies Used

* Hortonworks Data Platform - version 2.6.5
* Apache Spark - version 2.3.2

## Features

List of features ready and TODOs for future development
* Which meal type most choose by people country-wise?
* find percentage of each type of customer_type?
* In which month and year, the highest car parking space was required?
* Which country's people requested most spaecial service? etc...

To-do list:
* You can use Spark Streaming service for live data analysis and processing.
* Spark has a lot of features so you can use features according to your need.

## Getting Started
   
1. Clone the project
```
$ git clone https://github.com/munjanichintan123/Deep-Divers-P2.git
```

## Usage

A Hadoop ecosystem
  * Hortonworks Data Platform has to install.
  * Make sure all the services are started in the Ambari dashboard.

## Contributors

1. After logging into VM, clone the project onto local machine.
2. Copy csv file from local machine to HDFS.
```
$ hdfs dfs -put ./filename <hdfs-path>
```
4. Then, start executing queries which are present in python file.
Below command is used for executing python file.
```
spark-submit <file-name>
```
