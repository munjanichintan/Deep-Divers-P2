# Deep-Divers-P2

## Project Description

Creating Spark jobs in Python (using PySpark) to perform various analysis on a Hotel Booking dataset stored in HDFS in csv format.

## Technologies Used

* Hortonworks Data Platform - version 2.6.5
* Apache Spark - version 2.3.2

## Features

List of features ready and TODOs for future development.

Note: You can see all 24 queries in "queries.txt" file which is present in repository.
Some example of queries..
1. Which meal type most choose by people country-wise?
2. find percentage of each type of customer_type?
3. In which month and year, the highest car parking space was required?
4. Which country's people requested most spaecial service?

To-do list:
* You can use Spark Streaming service for live data analysis and processing.
* Spark has a lot of features so you can use features according to your need.

## Getting Started

1. Before cloning this repository, You have to make sure the installation of Hortonworks Data Sandbox in Oracle Virtual Box is proper and All the services which are shown in Ambari dashboard are started successfully.

2. After the above step, you have to open Git Bash and run below command
```
ssh maria_dev@sandbox-hdp.hortonworks.com -p 2222
```
3. When you run above command it will be asking for password so default password is "maria_dev".

4. Now you are succeefully login as a maria_dev user.
 
5. After completing above all the steps, you can clone repository using below command.
Note: cloning is done at home/maria_dev directory
```
$ git clone https://github.com/munjanichintan123/Deep-Divers-P2.git
```
6. Now you can see Deep-Divers-P2 directory when you run "ls" command.
7. Using "cd Deep-Divers-P2" command, you can go into that directory.
8. Now you have to copy "hotel_bookings.csv" file from local machine to HDFS using below command.
```
hdfs dfs -put hotel_bookings.csv <hdfs-path>
```
9. There is one p2.py file which has python code for analysing datasets.
Note: If you want to see result of particular query then remove comment from that query and run python file using below command.
```
spark-submit p2.py
```
## Usage

A Hadoop ecosystem
  * Hortonworks Data Platform has to install.
  * Make sure all the services are started in the Ambari dashboard.

## Contributors

* Aman Sagar(AmanSagar009)
* Chintan Munjani(munjanichintan123)
* Jaydeep Lanke(jaydeep1009)
