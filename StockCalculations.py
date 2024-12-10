# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:11:26 2024

@author: abram nothnagle
"""

import datetime

class StockCalculator():
    def __init__(self, data, ticker):
        self.data = data
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