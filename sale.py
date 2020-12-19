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
sale=DataFrame(c.head(500))
print(sale.head(500))
#b=df.dtypes

#parse string to datetime type

sale['Date']=pd.to_datetime(sale['Date'], infer_datetime_format=True)
indexeddf=sale.set_index(['Date'])
print(indexeddf.head(5))

#parsing to format
sale['Date']=pd.to_datetime(sale['Date'], format='%y-%m-%d')

#extracting year, month for specific loc
day=sale.loc[2,'Date'].day_name()

#extracting for all 
day=sale['Date'].dt.day_name()

month=sale['Date'].dt.month_name()

year=sale['Date'].dt.year

#subsetting
sale['Year']=sale['Date'].dt.year
sale['Month']=sale['Date'].dt.month_name()
sale['Day']=day=sale['Date'].dt.day_name()
print(sale.head(5))

#exploring data by month
Salary_situ=sale.groupby(['Month'])[['Sale_rev']]
print(Salary_situ.sum())

#exploring data by sales
Job_salary=sale.groupby(['Product_px'])[['Sale_rev']]
print(Job_salary.sum())


#Who is best, top paying job 
best_sales=sale.groupby(["Product_px", "Unit_px"]).sum().sort_values(["Sale_rev"],ascending=False)
print(best_sales.head(5))

df = px.data.tips()
fig = px.scatter(sale, x="Product_px", y="Sale_rev", trendline="m")
#plotly.offline.plot(fig, filename='o')

df = px.data.tips()
fig = px.scatter(sale, x="Unit_px", y="Sale_rev", trendline="m")
#plotly.offline.plot(fig, filename='o')

#pie charts


df = px.data.tips()
fig = px.pie(sale, values='Sale_rev', names='Month', color_discrete_sequence=px.colors.sequential.Blues)
plotly.offline.plot(fig, filename='sh')


sns.stripplot(x='Sale_rev', y='Month', jitter=0.50, size=9, alpha=0.7, hue='Year', palette='Blues',marker='*', linewidth=1, edgecolor='white',data=sale)
plt.show()