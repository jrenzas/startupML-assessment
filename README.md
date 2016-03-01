# startupML-assessment
Assessment for the startupML program. 

Data sources: 
Air travel data: http://transtats.bts.gov/Fields.asp?Table_ID=236
Fields to select: Month, DayofMonth, DayOfWeek, Origin, Dest, TaxiOut, TaxiIn, CRSArrTime, ArrDelay, ArrDelayMinutes, ArrDel15, Cancelled, Diverted, CRSElapsedTime, AirTime, Distance, DistanceGroup

Airport Location Data: http://openflights.org/data.html
Download airports.dat

Currently, the program is setup to use a subset of the air travel data as the training dataset. Program could be easily modified to allow a separate file to be the training set (or to use command line arguments to make it optional). 

Other trivial modifications not currently implemented:
1) Plots of various things.
2) Writing output to a file.
