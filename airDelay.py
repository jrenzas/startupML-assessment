# Airplane Delay Prediction
# Russ Renzas, 2016
# Open Source, do what you will
# Uses Linear Regression to estimate how long a given flight will be delayed.
# Uses Logistic Regression to classify likelihood of a given flight being delayed more than 15 minutes.
# Works fine in Python 3.
# Comments: Originally was going to use geopy to lookup longitude & latitude of airports, but got timeout erros
#           Replaced by optional lookup table using data from: http://openflights.org/data.html
#           Oddly enough, this didn't actually improve the variance. Maybe it would with another regression method?

import argparse
from sklearn import linear_model
import pandas as pd
import sklearn
import matplotlib.pyplot as plt

def munge(filename, lookupFile):
    try:
        df = pd.read_csv(filename)
        dfLook = pd.read_csv(lookupFile)
    except EnvironmentError:
        print('Invalid or Missing File(s)')
        exit(0)
    df = df[df.CANCELLED == 0]
    df = df[df.DIVERTED == 0]
    df = df.drop(['CANCELLED', 'DIVERTED'], axis=1)
    # df = df.drop(['CRS_ARR_TIME'], axis=1)
    dfLookD = dfLook
    dfLook.columns = ['a', 'b', 'c', 'd', 'ORIGIN', 'f', 'ORIGIN_LONG', 'ORIGIN_LAT', 'i', 'j', 'k', 'l']
    dfLook =dfLook.drop(['a','b','c','d','f','i','j','k','l'], axis=1)
    dfLookD.columns = ['a', 'b', 'c', 'd', 'DEST', 'f', 'DEST_LONG', 'DEST_LAT', 'i', 'j', 'k', 'l']
    dfLookD =dfLookD.drop(['a','b','c','d','f','i','j','k','l'], axis=1)
    df = pd.merge(df, dfLook, on=['ORIGIN'])
    df = pd.merge(df, dfLookD, on=['DEST'])
    df = df.drop(['ORIGIN', 'DEST'], axis=1)
    df = df.dropna()
    # print(df.head())

    return df

def regress(df):
    regr = linear_model.LinearRegression()
    df = df.drop(['ARR_DELAY_NEW', 'ARR_DEL15', 'ARR_DELAY_GROUP'], axis=1)
    Y = df.ARR_DELAY
    trainX, testX, trainY, testY = sklearn.cross_validation.train_test_split(df.drop(['ARR_DELAY'], axis=1), Y, test_size=0.33, random_state=5)
    regr.fit(trainX, trainY)
    regr.score(trainX, trainY)
    print('Linear Regression:')
    print('Coefficients:')
    print(list(zip(trainX.head(), regr.coef_)))
    print('Intercept: \n', regr.intercept_)
    print('Variance score: %.2f\n' % regr.score(testX, testY))

    # plt.scatter(trainX.DISTANCE_GROUP, trainY)
    # plt.show()

def logis(df):
    df = df.drop(['ARR_DELAY_NEW', 'ARR_DELAY', 'ARR_DELAY_GROUP'], axis=1)
    regr = linear_model.LogisticRegression()
    Y = df.ARR_DEL15
    trainX, testX, trainY, testY = sklearn.cross_validation.train_test_split(df.drop(['ARR_DEL15'], axis=1), Y, test_size=0.33, random_state=5)
    regr.fit(trainX, trainY)
    regr.score(trainX, trainY)

    print('Logistic Regression:')
    print('Variance score: %.2f' % regr.score(testX, testY))

def main():
    parser = argparse.ArgumentParser(description="This program analyzes flight delay data")
    parser.add_argument('--file', dest='fname', required=True)
    parser.add_argument('--lookup', dest='lname', required=True)
    args = parser.parse_args()
    fname = args.fname
    lname = args.lname
    df = munge(fname, lname)
    regress(df)
    logis(df)

if __name__ == '__main__':
    main()