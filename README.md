# testauto
a python script to automate the uploading of testing results. 


# Libraries being Used 

Beautiful Soup 
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

CSV Module Python 
https://docs.python.org/3/library/csv.html

Selenium 
https://selenium-python.readthedocs.io/installation.html


# A rough working outline of how the project will work. 
The script starts. 
The script loads the excel data and gets it ready to go. 
Username information is entered
The script logs me in 
the script waits for me to enter authenticator password. 
The script then logs me in to the main page. 
The script then commences uploading the data. 
It checks whether or not the patient is existing. If the patient exists it executes that work flow. 
If the patient doesn't exist then it executes the other work flow. 

things to match are DOB, GENDER

https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas
https://stackoverflow.com/questions/24870953/does-pandas-iterrows-have-performance-issues
https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#essential-basic-functionality
https://stackoverflow.com/questions/37113173/compare-2-excel-files-using-python

https://datascience.stackexchange.com/questions/58546/valueerror-the-truth-value-of-a-dataframe-is-ambiguous-use-a-empty-a-bool



This is the automation script for registering new patients. 

# Things to automate
3000-> new registration
2000-> encounters
3000 -> follow up. 
2000 -> booster 
500 -> check for medicare against rhino data and put those that are not in rhino into respiratory clinic app. put those that are in rhino app into prexisting. 


empty addreses for new pateients
postcodes for new patients
empty medicare numbers new patients
