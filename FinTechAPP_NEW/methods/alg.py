import pandas as pd
import numpy as np
import quandl
from datetime import datetime, time
from talib import RSI, ADX, MACD, KAMA, MA
import matplotlib.pyplot as plt

#Genernal Functions


def turn_to_list(df, to_get:str):
    return df[to_get].values

#Tech Analysis
#RSI
def rsi_analysis(price: list, time_period:int):
    output = RSI(price, time_period)
    if output[-1] > 25 or output[-1] < 35:
        return "Buy"
    elif output[-1] > 65 or output[-1] < 75:
        return "Sell"
    else:
        return "Hold"

def plot_rsi_analysis(price: list, time_period: int):
    output = RSI(price, time_period)
    plt.plot(output)
    plt.axhline(y=30, color='r', linestyle='-')
    plt.axhline(y=70, color='b', linestyle='-')
    plt.show()

#ADX
def adx_analysis(price: list, time_period:int):
    #Price should be close price
    high = max(price)
    low = min(price)
    real_adx = ADX(high, low, price, time_period)
    if real_adx >=0 and real_adx <= 25:
        return "Weak"
    elif real_adx > 25 and real_adx <= 50:
        return "Strong"
    elif real_adx > 50 and real_adx <= 75:
        return "Very Strong"
    elif real_adx > 75 and real_adx <= 100:
        return "Extremely Strong"
    else:
        return None

#MACD
def macd_analysis(price):
    macd, macdsignal, macdhist = MACD(price, fastperiod=12, slowperiod=26, signalperiod=9)
    if macdhist[-1] > 0: 
        return "uptrend"
    else:
        return "downtrend"
    

    
#KAMA
def kama_analysis(price:list, timeperiod):
    #the default is 30
    if timeperiod == None or timeperiod == "default":
        tp=30
    else:
        tp=int(timeperiod)
        
    output = KAMA(price, tp)
    if price[-1]>output[-1]:
        return "Buy"
    elif price[-1]==output[-1]:
        return "Hold"
    else:
        return "Sell"

        
#MA - moving average
def ma_analysis(price):
    output = MA(price, timeperiod=30, matype=0)
    return output

def draw_ma(price):
    output = ma_analysis(price)
    plt.plot(output)
    plt.plot(price)
    plt.show()
        



