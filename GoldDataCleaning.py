# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:42:20 2017

@author: jswordy
"""
import pandas as pd
import urllib2
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#API Call from Quandl for London Bullion Market Association Gold
#price data.
reqst = "https://www.quandl.com/api/v3/datasets/LBMA/GOLD.json?\
api_key=YOURAPIKEY"
call = urllib2.Request(reqst)
response = urllib2.urlopen(call)
the_page = response.read()
#parsing the JSON returned to extract column names and data
decode = json.loads(the_page)
dataset = decode['dataset']
columns = dataset["column_names"]
data = dataset['data']
#Converting Data to a Dataframe to vizualise data, some historical
#gold prices do not have a closing cost so line 29 takes opening cost
#and places it in closing column
df = pd.DataFrame(data, columns=columns)
df.loc[df['USD (PM)'].isnull(), 'USD (PM)'] = df['USD (AM)']
y = df['USD (PM)']
#Converting date information to matplot native date type
plot_datay = df['Date'].tolist()
x = mdates.datestr2num(plot_datay)
#displaying plot
plt.plot(x, y)
plt.show()


