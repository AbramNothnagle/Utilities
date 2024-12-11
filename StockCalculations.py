# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:11:26 2024

@author: abram nothnagle
"""

import datetime
import numpy as np

class StockCalculator():
    def __init__(self, data, ticker):
        self.data = np.array(data)
        self.ticker = ticker
    
    '''
    _UStoISODate(date)
    Meant to transform a US date of format MM/DD/YYYY to ISO format of YYYY/MM/DD.
    Will raise an exception if the format is wrong.
    Input: (string) date of format MM/DD/YYYY or MM/D/YYYY 
    Output: (string) date of format YYYY-MM-DD
    '''
    def _UStoISODate(self,USDate):
        dateList = USDate.split('/') #Get list of [MM, D, YYYY]. Day may be one or two characters long
        if len(dateList) != 3:
            err = 'Improper US date format in _UStoISODate(date) for ' + USDate + ': splitting on slash failed.'
            raise Exception(err)
        #1 character month and day
        if len(dateList[1]) == 1 and len(dateList[0]) == 1:
            isoDate = dateList[2] + '-0' + dateList[0] + '-0' + dateList[1]
        #1 character month, 2 character day
        elif len(dateList[1]) == 2 and len(dateList[0]) == 1:
            isoDate = dateList[2] + '-0' + dateList[0] + '-' + dateList[1]
        #1 character day, 2 character month
        elif len(dateList[1]) == 1 and len(dateList[0]) == 2:
            isoDate = dateList[2] + '-' + dateList[0] + '-0' + dateList[1]
        #2 character month and day
        elif len(dateList[1]) == 2 and len(dateList[0]) == 2:
            isoDate = dateList[2] + '-' + dateList[0] + '-' + dateList[1]
        else:
            err = 'Improper US date format in _UStoISODate(date) for ' + USDate
            raise Exception(err)
        
        return isoDate
    
    '''
    _getDayOfWeekISO
    Meant to get the weekday from an ISO format date string as an integer (1-7)
    Will raise an exception if the extraction failed.
    Input: (string) date of format YYYY-MM-DD 
    Output: (int) weekday number from 1-7
    '''
    def _getDayOfWeekISO(self, isoDate):
        day = -1
        d = datetime.date.fromisoformat(isoDate)
        day = d.weekday() #Returns number of the day in the week from 0 - 6
        if day < 0:
            err = "Day of week could not be parsed for " + isoDate + " in " + self.ticker
            raise Exception(err) 
        return day + 1
    
    '''
    _getDayISO
    Meant to get the day of the month as an integer
    Will raise an exception if the extraction failed.
    Input: (string) date of format YYYY-MM-DD 
    Output: (int) day number
    '''
    def _getDayISO(self, isoDate):
        day = -1
        d = datetime.date.fromisoformat(isoDate)
        day = d.day #Returns number of the day in the month
        if day < 0:
            err = "Day of month could not be parsed for " + isoDate + " in " + self.ticker
            raise Exception(err) 
        return day
    
    '''
    _getMonth
    Meant to extract the month from an ISO formatted date string.
    Will raise an exception if the extraction failed.
    Input: (string) date of format YYYY-MM-DD 
    Output: (int) month from 1-12
    '''
    def _getMonth(self, isoDate):
        month = -1
        d = datetime.date.fromisoformat(isoDate)
        month = d.month
        if month < 0:
            err = "Month could not be parsed for " + isoDate + " in " + self.ticker
            raise Exception(err) 
        return month
    
    '''
    getDayMonth()
    This function generates a list of (day, month) pairs from the data loaded in the object.
    Requires the data to be loaded in as (M/D/YYY, close, volume, open, high, low) strings from the .csv
    Input: None, just requires the data loaded in the object
    Output: list of ((int) day, (int) month) pairs
    '''
    def getDayMonth(self):
        dayMonths = []
        for row in self.data:
            isoDate = self._UStoISODate(row[0])
            dayMonths.append((self._getDayOfWeekISO(isoDate), self._getMonth(isoDate)))
        return dayMonths
    
    '''
    getDayMonthIdx(index)
    This function generates a list of (day, month) pairs from the data loaded in the object.
    Requires the data to be loaded in as (M/D/YYY, close, volume, open, high, low) strings from the .csv
    Input: (int) index of the data to extract the day and month for
    Output: tuple of ((int) day, (int) month)
    '''
    def getDayMonthIdx(self, i):
        row = self.data[i]
        isoDate = self._UStoISODate(row[0])
        return (self._getDayOfWeekISO(isoDate), self._getMonth(isoDate))
    
    '''
    getSMA60(index)
    This function calculates the simple 60-day moving average for the data at a given index.
    Requires index > 60, otherwise will return -1.
    Input: (int) index of the data to calculate SMA60 for
    Output: (float) 60-day SMA at index, or -1 if it can't be calculated
    '''
    def getSMA60(self, i):
        if i < 60:
            return -1.0
        #column 1 is the closing price
        sma60 = round(np.sum(self.data[i-60:i,1]).astype(np.float)/60,2)
        '''sum60 = 0
        for idx in range(i-60,i):
            sum60 += float(self.data[idx][1]) #column 1 should be closing price
        sma60 = sum60/60
        #sma60 = round(sum(self.data[i-60:i][1]),2)'''
        return sma60
    
    '''
    getSMAx(x, i)
    This function calculates the simple x-day moving average for the data at a given index.
    Requires index > x, otherwise will return -1.
    Input:  (int) x - the number of days over which to calculate the SMA 
            (int) i - index of the data to calculate SMAx for
    Output: (float) x-day SMA at index, or -1 if it can't be calculated
    '''
    def getSMAx(self, x, i):
        if i < x:
            return -1.0
        #column 1 is the closing price
        smaX = round(np.sum(self.data[i-x:i,1].astype(np.float))/x,2)

        return smaX
    
    '''
    getWMAx(x, i)
    This function calculates the weighted x-day moving average for the data at a given index.
    Requires index > x, otherwise will return -1.
    Input:  (int) x - the number of days over which to calculate the WMA 
            (int) i - index of the data to calculate WMAx for
    Output: (float) x-day WMA at index, or -1 if it can't be calculated
    '''
    def getWMAx(self, x, i):
        if i < x:
            return -1.0
        #column 1 is the closing price
        window = self.data[i-x:i,1].astype(np.float)
        weights = np.array(list(range(1,x+1)))
        weights = weights/np.sum(weights)
        weightedWindow = window*weights
        wmaX = round(np.sum(weightedWindow),2)

        return wmaX
    
    '''
    getSTDx(x, i)
    This function calculates the standard deviation over the previous x days at the index provided.
    Requires index > x, otherwise will return -1.
    Input:  (int) x - the number of days over which to calculate the STD  
            (int) i - index of the data to calculate STDx for
    Output: (float) x-day standard deviation at index, or -1 if it can't be calculated
    '''
    def getSTDx(self, x, i):
        if i < x:
            return -1.0
        stdX = round(np.std(self.data[i-x:i,1].astype(np.float)),2)
        return stdX