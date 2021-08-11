import pandas as pd

# TODO(get RME table: 區間事故、區間平日尖峰、區間平日離峰、區間假日、自強事故、自強平日、自強假日、自強連假)

def station(station:str, trainNumber:int, setupDelayTime:int, isAccident:bool, isWeekDay:bool, isOnPeak:bool)->int:

    trainType = getTrainCategory(trainNumber)

    if station == 'Taichung':
        if isAccident:
            accidentFunction()
        else:
            if isWeekDay:
                if isOnPeak:
                    onPeakFunction()
                else:
                    offPeakFunction()
            else:
                weekEndFunction()

def getTrainCategory(trainNumber:int)->str:

    if trainNumber < 500:
        return '自強'

    if trainNumber < 999:
        return '莒光'
    
    return '區間'

def accidentFunction(trainType:str):
    pass

def onPeakFunction(trainType:str):
    pass

def offPeakFunction(trainType:str):
    pass

def weekEndFunction(trainType:str):
    pass
