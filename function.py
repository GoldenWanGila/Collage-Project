import pandas as pd

# get RME table: 區間事故、區間平日尖峰、區間平日離峰、區間假日、自強事故、自強平日、自強假日、自強連假
localTrain_weekday_onPeak_dataFrame = pd.read_csv('區間平日尖峰MSE.csv', index_col=0)
localTrain_weekday_offPeak_dataFrame = pd.read_csv('區間平日離峰MSE.csv', index_col=0)
localTrain_weekend_dataFrame = pd.read_csv('區間假日MSE.csv', index_col=0)
TzeChiang_weekday_dataFrame = pd.read_csv('自強中部平日MSE.csv', index_col=0)
TzeChiang_weekend_dataFrame = pd.read_csv('自強中部假日MSE.csv', index_col=0)
TzeChiang_longWeekend_dataFrame = pd.read_csv('自強中部連假日MSE.csv', index_col=0)

stationList = ['Fengyuan', 'Taiyuan', 'Taichung', 'Xinwuri', 'Chenggong', 'Changhua', 'Yuanlin']

def getOffsetDelay(station:str, time:str, trainNumber:int, setupDelayTime:int, isAccident:bool, dayOfTheWeek:int, isClockwise:bool)->list[int]:
    if isLocalTrain(trainNumber):
        if isAccident:
            return accidentFunction(isLocalTrain(trainNumber), station, setupDelayTime, isClockwise)
        else:
            if isWeekday(dayOfTheWeek) == 'weekday':
                if isOnPeak(time):
                    return onPeakFunction(station, setupDelayTime, isClockwise)
                else:
                    return offPeakFunction(station, setupDelayTime, isClockwise)
            else:
                return weekEndFunction(isLocalTrain(trainNumber), station, setupDelayTime, isClockwise)
    else:
        if isAccident:
            return accidentFunction(isLocalTrain(trainNumber), station, setupDelayTime, isClockwise)
        else:
            if isWeekday(dayOfTheWeek) == 'weekday':
                return weekDayFunction(station, setupDelayTime, isClockwise)
            elif isWeekday(dayOfTheWeek) == 'weekend':
                return weekEndFunction(isLocalTrain(trainNumber), station, setupDelayTime, isClockwise)
            else:
                return longWeekDayFunction(station, setupDelayTime, isClockwise)

def accidentFunction(isLocalTrain:bool, station:str, setupDelayTime:int, isClockwise:bool):
    if isLocalTrain:
        pass
    else:
        pass

def onPeakFunction(station:str, setupDelayTime:int, isClockwise:bool)->list[int]:
    targetRow = localTrain_weekday_onPeak_dataFrame[localTrain_weekday_onPeak_dataFrame.index == station]
    delayList = []
    openFlag = True if isClockwise else False

    for col in targetRow:
        delay = (targetRow[col].values)[0]
        if openFlag:
            if delay == '--':
                delayList.append(0)
                openFlag = False
            elif float(delay) >= 1.5:
                delayList.append(round(float(delay))+setupDelayTime)
            else:
                delayList.append(setupDelayTime)
        else:
            delayList.append(0)
            if delay == '--':
                openFlag = True
    
    return delayList

def offPeakFunction(station:str, setupDelayTime:int, isClockwise:bool):
    targetRow = localTrain_weekday_offPeak_dataFrame[localTrain_weekday_offPeak_dataFrame.index == station]
    delayList = []
    openFlag = True if isClockwise else False

    for col in targetRow:
        delay = (targetRow[col].values)[0]
        if openFlag:
            if delay == '--':
                delayList.append(0)
                openFlag = False
            elif float(delay) >= 1.5:
                delayList.append(round(float(delay))+setupDelayTime)
            else:
                delayList.append(setupDelayTime)
        else:
            delayList.append(0)
            if delay == '--':
                openFlag = True
    
    return delayList

def weekEndFunction(isLocalTrain:bool, station:str, setupDelayTime:int, isClockwise:bool):
    if isLocalTrain:
        targetRow = localTrain_weekend_dataFrame[localTrain_weekend_dataFrame.index == station]
        delayList = []
        openFlag = True if isClockwise else False

        for col in targetRow:
            delay = (targetRow[col].values)[0]
            if openFlag:
                if delay == '--':
                    delayList.append(0)
                    openFlag = False
                elif float(delay) >= 1.5:
                    delayList.append(round(float(delay))+setupDelayTime)
                else:
                    delayList.append(setupDelayTime)
            else:
                delayList.append(0)
                if delay == '--':
                    openFlag = True
        
        return delayList
    else:
        targetRow = TzeChiang_weekend_dataFrame[TzeChiang_weekend_dataFrame.index == station]
        stationToDelay = dict(zip(stationList, [0]*7))
        openFlag = False

        for col in targetRow:
            delay = (targetRow[col].values)[0]
            if openFlag:
                if delay == '--':
                    openFlag = False
                elif float(delay) >= 2:
                    stationToDelay[col] = round(float(delay))+setupDelayTime
                else:
                    stationToDelay[col] = setupDelayTime
            else:
                if delay == '--':
                    openFlag = True

        return list(stationToDelay.values())

def weekDayFunction(station:str, setupDelayTime:int, isClockwise:bool):
    targetRow = TzeChiang_weekday_dataFrame[TzeChiang_weekday_dataFrame.index == station]
    stationToDelay = dict(zip(stationList, [0]*7))
    openFlag = True if isClockwise else False

    for col in targetRow:
        delay = (targetRow[col].values)[0]
        if openFlag:
            if delay == '--':
                openFlag = False
            elif float(delay) >= 2:
                stationToDelay[col] = round(float(delay))+setupDelayTime
            else:
                stationToDelay[col] = setupDelayTime
        else:
            if delay == '--':
                openFlag = True

    return list(stationToDelay.values())

def longWeekDayFunction(station:str, setupDelayTime:int, isClockwise:bool):
    targetRow = TzeChiang_longWeekend_dataFrame[TzeChiang_longWeekend_dataFrame.index == station]
    stationToDelay = dict(zip(stationList, [0]*7))
    openFlag = True if isClockwise else False

    for col in targetRow:
        delay = (targetRow[col].values)[0]
        if openFlag:
            if delay == '--':
                openFlag = False
            elif float(delay) >= 2:
                stationToDelay[col] = round(float(delay))+setupDelayTime
            else:
                stationToDelay[col] = setupDelayTime
        else:
            if delay == '--':
                openFlag = True

    return list(stationToDelay.values())

def isLocalTrain(trainNumber:int)->bool:
    if trainNumber < 500:
        return False
    return True

def isOnPeak(time:str)->bool:
    if (time >= '06:00') and (time <= '08:00'):
        return True
    if (time >= '17:00') and (time <= '20:00'):
        return True
    return False

def isWeekday(dayOfTheWeek:int)->str:
    if int(dayOfTheWeek) in [1,2,3,4,5]:
        return 'weekday'
    return 'weekend'
