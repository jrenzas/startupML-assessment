# startupML-assessment
Assessment for the startupML program. 

Main file: airDelay.py
Usage: python airDelay.py --file filename.csv --lookup airports.dat
Output: Variance scores for Linear Regression and Logistic Regression

Utility file: StripExtraCommas.py 
Usage: python StripExtraCommas.py --file filename.csv
Output: filename.csv has any excess commas at end of each (or some) lines removed. These commas disrupt function used in airDelay.py, hence it is convenient to remove them. Could be combined into airDelay.py if desired. 


Data sources: 
Air travel data: http://transtats.bts.gov/Fields.asp?Table_ID=236
Fields to select: Month, DayofMonth, DayOfWeek, Origin, Dest, TaxiOut, TaxiIn, CRSArrTime, ArrDelay, ArrDelayMinutes, ArrDel15, Cancelled, Diverted, CRSElapsedTime, AirTime, Distance, DistanceGroup

Airport Location Data: http://openflights.org/data.html
Download airports.dat

Currently, the program is setup to use a subset of the air travel data as the training dataset. Program could be easily modified to allow a separate file to be the training set (or to use command line arguments to make it optional). 

Other trivial modifications not currently implemented:
1) Plots of various things.  
2) Writing output to a file.
3) Making model objects reuseable - e.g. serializing them into separate files so they don't need to be recalculated each time. 
