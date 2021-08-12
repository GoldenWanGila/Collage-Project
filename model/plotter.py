from re import T
import sklearn.linear_model
import xgboost as xgb
from sklearn.linear_model import LinearRegression
from sympy import *
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from numpy.core import numeric
import seaborn as sns; sns.set()
import matplotlib as mpl
import pandas as pd
import numpy as np

def plot(x:np.ndarray, y:np.ndarray):
    x = x.reshape(-1,1)
    # model = LinearRegression(fit_intercept=True)
    # model.fit(x, y)
    # print("Modela slope:    ", model.coef_[0])
    # print("Modela intercept:", model.intercept_)
    # print("LinearRegression Score: ",model.score(x,y))

    # predict = model.predict(x)
    # plt.plot(x,predict,c="red")
    # plt.scatter(x,y)
    # # plt.xlim(0,25)
    # # plt.ylim(0,25)
    # plt.show()

    # k= model.coef_[0]
    # l= model.intercept_
    # xsymb,ysymb = symbols('x,y')
    # print(solve([k*xsymb+l-ysymb,xsymb-ysymb],[xsymb,ysymb]))
    # print("算出允許誤差")
    # print("xgboost、lasso比較")
    xgbrModel=xgb.XGBRegressor()
    xgbrModel.fit(x,y)
    predicted=xgbrModel.predict(x)
    # print("xg Score: ",xgbrModel.score(x,y))
    # plt.scatter(x, y, s=10, label='True')
    # plt.scatter(x, predicted, color="r",s=10, label='Predicted')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.legend()
    # # plt.xlim(0,25)
    # # plt.ylim(0,25)
    # plt.show()
    v = mean_squared_error(y,predicted)
    print(sqrt(v))

def arrangeDataFrame(x_dataFrame:pd.DataFrame,y_dataFrame:pd.DataFrame,direction:int):
    x_dataFrame_direction = x_dataFrame[x_dataFrame['direction']==direction]
    y_dataFrame_direction = y_dataFrame[y_dataFrame['direction']==direction]

    if len(set(x_dataFrame_direction['date'])) != len(set(y_dataFrame_direction['date'])):
        same_dates = [date for date in set(y_dataFrame_direction['date']) if (date in set(x_dataFrame_direction['date']))]
        x_dataFrame_direction = x_dataFrame_direction[x_dataFrame_direction['date'].isin(same_dates)]
        y_dataFrame_direction = y_dataFrame_direction[y_dataFrame_direction['date'].isin(same_dates)]

    same_nums = [num for num in set(y_dataFrame_direction['num']) if (num in set(x_dataFrame_direction['num']))]
    x_target_dataFrame = x_dataFrame_direction[x_dataFrame_direction['num'].isin(same_nums)]
    x_target_dataFrame.sort_values(by=['date','num'], inplace=True)
    x_target_dataFrame.reset_index(inplace=True)
    y_target_dataFrame = y_dataFrame_direction[y_dataFrame_direction['num'].isin(same_nums)]
    y_target_dataFrame.sort_values(by=['date','num'], inplace=True)
    y_target_dataFrame.reset_index(inplace=True)

    # 獲取 delay不存在的 row index
    null_index = list(x_target_dataFrame[x_target_dataFrame['delay'].isnull()].index)
    null_index.extend(list(y_target_dataFrame[y_target_dataFrame['delay'].isnull()].index))
    null_index = set(null_index)

    # 將delay不存在的 row 從資料中移除
    x_target_dataFrame = x_target_dataFrame.drop(index=null_index)
    y_target_dataFrame = y_target_dataFrame.drop(index=null_index)

    x = x_target_dataFrame['delay'].to_numpy()
    y = y_target_dataFrame['delay'].to_numpy()
    return x,y

def getRMSE(x:np.ndarray, y:np.ndarray):
    x = x.reshape(-1,1)
    xgbrModel=xgb.XGBRegressor()
    xgbrModel.fit(x,y)
    predicted=xgbrModel.predict(x)
    v = mean_squared_error(y,predicted)
    return sqrt(v)