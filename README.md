# Automation of Data Migration using Python
This project was initiated by me during my internship at Infineon Technologies with the aim to automate the data migration process for three sites. The project involved extracting large data files and comparing thousands of lines in each file to finally import the files with the largest values. The existing approach of manually comparing values took around three months to complete, which was very time-consuming and labor-intensive.

## Task Specification
The project was assigned to automate the data migration process, which involves looping through each file, extracting the file, and comparing the largest values. The program exports files with the largest values to the database.

## Implementation and Solution Method
The project began with a series of meetings to understand the scope. A POC was developed using Python programming language due to its flexible nature, and PyCharm was used as the IDE. A small sample of test data was used to test the POC, and it worked as intended. Colleagues were demonstrated the POC, which was approved, and further development of the program was requested.

The final solution consists of two programs, namely 'analysis.py' and 'import.py.' 'Analysis.py' loops through each file, extracts it, compares and stores the maximum value (row number) for each line (file). Once the process is completed, the results are exported to a csv file. 'Import.py' imports the results from csv files, extracts the files with the largest value, and finally imports those files to the Oracle database.
<p align="center" width="100%">
    <img width="50%" src="https://user-images.githubusercontent.com/55419300/230011760-9c9a5f50-1d4f-44eb-b0ca-e395d5a07060.png">
</p>

The programs were tested on real data and worked exceptionally well. A stress test with a large amount of data was conducted with colleagues, and the program performed flawlessly with no error.

## Results of Task/Project
At the end, two Python programs were created to automate the data migration tasks. The program was integrated with a .bat script to be executed in one click. Both of the programs managed to migrate all data for the RGB site flawlessly in a total of 2 days, which would usually take 3 months with manual approach. From the benchmark, it is clear that the solution with a total of just 162 lines of Python code is approximately 4500% faster, saving around 2112 hours of manual labor.

## Advantages, Disadvantages, and Suggestions for Task Improvement
The solution is 45x times faster than the manual approach, saving countless hours of human labor, which can be used for some other important tasks. Without a doubt, it will also increase productivity in the company. Due to the simple nature of the solution, anyone can run and use it without advanced programming language. The solution can also be run in parallel for data migration of different sites.

In terms of disadvantage, to make the solution simple, few of the parameters such as file directory and database addresses have been hard-coded in the program. If anyone wants to perform data migration for other sites, they have to tweak the parameters in code first. Other than that, since database connections have been hard-coded, any intruders who get hold of the code can hack and damage the entire database ecosystem.

In terms of suggestions, both ‘analysis.py’ and ‘import.py’ can be integrated together for seamless processing which will eliminate human intervention altogether. Hard-coded parameters can be modified as user input variables to be more user-friendly and less rigid. Together with that, database connections should also be encrypted to prevent unauthorized people from accessing or in the worst case damaging the ecosystem. Apart from that, file extraction is the longest process in the solution which can be made faster by implementing distributed computing to utilize more computational resources hence, process files faster.
