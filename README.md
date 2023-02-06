# Purpose of Project
The input file contains web analytics data from 100 different websites. The metrics measured from each site includes: Page Views, Unique Visitors, Total Time Spent, Visits, and
Average Time Spent on Site. The purpose of the project is to extract the data from the flat file and transform to the given format in order to perform further analysis on the data. 

* The final working code is the python 3 script: metric_extraction.py
* The Input file is the excel file data.xlsx
* The generated output file is the comma separated value (CSV) file. Sample output file data_3526.csv
* The Unit Test is the file: test_metric_extraction.py

The requirement packages are listed in the file requirements.txt


# Expected input and output
The expected input is an excel file (data.xlsx) and the output is a comma separated value (CSV) file: data_xxxx.csv file where xxxx is 4 random digits.

# Installation steps/instruction
* Download the project
* Run the command `pip install -r requirements.txt` to install all of the Python modules and packages listed in the requirements.txt file.
* Delete the generated output, data.csv, file in the project.
* Open the file metric_extraction.py and run the file. The script takes the input file in the project root directory, parsed it, and generate the output based on the analytics template.

# Instruction to run test
Open the PyCharm (the IDE used) terminal and run the command: `py.test`

# Known limitations
Sort the Site ID properly. site 1, site 2, ...., site 10 and not site 1, site 10, ...., site 2







