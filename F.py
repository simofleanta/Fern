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

#parse string to datetime type

df['Date']=pd.to_datetime(df['Date'], infer_datetime_format=True)
indexeddf=df.set_index(['Date'])
print(indexeddf.head(5))

#parsing to format
df['Date']=pd.to_datetime(df['Date'], format='%y-%m-%d')

#extracting year, month for specific loc
day=df.loc[2,'Date'].day_name()

#extracting for all 
day=df['Date'].dt.day_name()

month=df['Date'].dt.month_name()

year=df['Date'].dt.year

#subsetting
df['Year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month_name()
df['Day']=day=df['Date'].dt.day_name()
print(df.head(5))

#exploring data by month
Salary_situ=df.groupby(['Month'])[['Sale_rev']]
print(Salary_situ.sum())

#exploring data by sales
Job_salary=df.groupby(['Product_px'])[['Sale_rev']]
print(Job_salary.sum())

#Who is best, top paying job 
best_paid=df.groupby(["Product_px", "Unit_px"]).sum().sort_values(["Sale_rev"],ascending=False)
print(best_paid.head(5))

#pie charts

product=df
df = px.data.tips()
fig = px.pie(product, values='Product_px', names='Month', color_discrete_sequence=px.colors.sequential.Blues)
plotly.offline.plot(fig, filename='sh')







