import pandas as pd
import seaborn as sns 
from pandas import DataFrame
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
import numpy as np
import plotly
import statistics
import plotly.express as px
import stats
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import plotly.express as px
from datetime import datetime
from matplotlib import rcParams


c=pd.read_csv('costs.csv')
print(c.columns)
df=DataFrame(c.head(500))
print(df.head(500))
#b=df.dtypes

#parse string t ta datetime  type

#df['Date']=pd.to_datetime(df['Date'], infer_datetime_format=True)
#indexeddf=df.set_index(['Date'])
#print(indexeddf.head(5))

#another way

"""df['Date']=pd.to_datetime(df['Date'], format='%y-%m-%d')
day=df.loc[2,'Date'].day_name()

day=df['Date'].dt.day_name()
print(day)
month=df['Date'].dt.month_name()
print(month)
year=df['Date'].dt.year
print(year)"""

staff=pd.read_csv('employees.csv')
print(staff.columns)
sdf=DataFrame(c.head(500))
print(sdf.head(500))
#b=df.dtypes

sdf['Date']=pd.to_datetime(df['Date'], infer_datetime_format=True)
indexeddf=sdf.set_index(['Date'])
print(indexeddf.head(5))

sdf['Date']=pd.to_datetime(sdf['Date'], format='%y-%m-%d')
day=sdf.loc[2,'Date'].day_name()

day=sdf['Date'].dt.day_name()
print(day.head(3))
month=sdf['Date'].dt.month_name()
print(month.head(3))
year=sdf['Date'].dt.year
print(year.head(3))









