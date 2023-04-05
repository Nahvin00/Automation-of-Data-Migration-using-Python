# Automation of Data Migration using Python
## Problem statement
IFMY IT FSC MFW team was tasked to migrate site data from existing format to new standard of practice. The process of data migration involves extracting large data files and comparing thousands of lines in each file to finally import the files with the largest values. Around three (3) sites were involved in this data migration. Colleagues have previously completed data migration from one (1) site by comparing the values manually. This took them roughly three (3) months to complete which is very time consuming and labor intensive.

## Task specification
A solution to automate the data migration was assigned to develop that:
* Loop through each file
* Extract the file and compare the largest values, and
* Export files with largest values to database

## Implementation and solution method
The process begins with a series of meetings to understand the scope. Primarily, discussions were held with Mr. Tat Sern to brainstorm concepts or ideas to solve the data migration issue. After brainstorming, the POC for the solution was started to be developed. The POC was developed using python programming language due to its flexible nature with PyCharm as the IDE for this project. 

A test data which is a small sample from original data is used to test the POC. POC worked as intended and was demonstrated to colleagues. POC was approved and Further development of the program was requested and a solution consisting of two (2) programs, namely 'analysis.py' and 'import.py', was then developed. Figure below shows the overall process flow of these 2 programs.
<p align="center" width="100%">
    <img width="50%" src="https://user-images.githubusercontent.com/55419300/230011760-9c9a5f50-1d4f-44eb-b0ca-e395d5a07060.png">
</p>
The program will begin with ‘analysis.py’ which will loop through each file and extract it. Then, it compares and stores the maximum value (row number) for each line (file). Once the process is completed, the results are exported to a csv file. Then, ‘import.py’ will be executed which will import the results from csv files and extract the files with the largest value. Finally, those files will be imported to the oracle database. ‘Import.py’ was intentionally separated from the ‘analysis.py’ to prevent catastrophic data redundancy in the database if errors were to occur during analysis. It also allows colleagues to inspect the results from ‘analysis.py’ before importing to the database. 

These programs were tested on real data and it works exceptionally well. A stress test with a large amount of data was conducted with colleagues to evaluate how well the program can perform under pressure and the program aced with no error.

## Results of task/project
At the end, two python programs were created to automate the data migration tasks. Since it was a one-time job, there was no emphasis on GUI of the program. The program was integrated with a .bat script to be executed in one click. 
Both of the programs managed to migrate all data for the RGB site flawlessly in a total of 2 days which would usually take 3 months with manual approach. From the benchmark, it is clear that the solution with a total of just 162 lines of python code is approximately 4500% faster which saves around 2112 hours of manual labor.

## Advantage, disadvantage and suggestion for task improvement
In terms of advantage, the solution is 45x times faster than the manual approach. It can save countless hours of human labor and which can be used for some other important tasks. Without a doubt, it will also increase the productivity in the company. Apart from that, due to the simple nature of the solution anyone can run and use it without advanced programming language. It was designed to be simple and minimal for wider approach. The solution can also be run in parallel for data migration of different sites (which sometimes can slow the process time).

In terms of disadvantage, to make the solution simple, few of the parameters such as file directory and database addresses have been hard-coded in the program. If anyone wants to perform data migration for other sites, they have to tweak the parameters in code first. Other than that, since database connections have been hard-coded, any intruders who get hold of the code can hack and damage the entire database ecosystem.

In terms of suggestions, both ‘analysis.py’ and ‘import.py’ can be integrated together for seamless processing which will eliminate human intervention altogether. Other than that, hard-coded parameters can be modified as user input variables to be more user-friendly and less rigid. Together with that, database connections should also be encrypted to prevent unauthorized people from accessing or in worse case damaging the ecosystem. Apart from that, file extraction is the longest process in the solution which can be made faster by implementing distributed computing to utilize more computational resources hence, process files faster
