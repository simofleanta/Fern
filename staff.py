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

#open file
staff=pd.read_csv('employees.csv')
print(staff.columns)
sdf=DataFrame(staff.head(50))
print(sdf.head(50))
#b=df.dtypes

sdf['Date']=pd.to_datetime(sdf['Date'], infer_datetime_format=True)
indexeddf=sdf.set_index(['Date'])
#print(indexeddf.head(5))

sdf['Date']=pd.to_datetime(sdf['Date'], format='%y-%m-%d')
day=sdf.loc[2,'Date'].day_name()
day=sdf['Date'].dt.day_name()
month=sdf['Date'].dt.month_name()
year=sdf['Date'].dt.year

#subset time series so we can explore data by time series

sdf['Year']=sdf['Date'].dt.year
sdf['Month']=sdf['Date'].dt.month_name()
sdf['Day']=day=sdf['Date'].dt.day_name()
print(sdf.head(50))
print(sdf.to_csv("staff_paid.csv"))

#exploring data by month
Salary_situ=sdf.groupby(['Month'])[['Salary']]
print(Salary_situ.sum())

#exploring salary by job 
Job_salary=sdf.groupby(['Job'])[['Salary']]
print(Job_salary.sum())

#Who is best, top paying job 
best_paid=sdf.groupby(["Job", "Name"]).sum().sort_values(["Salary"],ascending=False)
print(best_paid)

#pie charts 

s=sdf
df = px.data.tips()
fig = px.pie(s, values='Salary', names='Job', color_discrete_sequence=px.colors.sequential.Blues)
#plotly.offline.plot(fig, filename='s')

s_month=sdf
df = px.data.tips()
fig = px.pie(s_month, values='Salary', names='Month', color_discrete_sequence=px.colors.sequential.Blues)
#plotly.offline.plot(fig, filename='s')

s=sdf
df = px.data.tips()
fig = px.pie(s, values='Salary', names='Job', color_discrete_sequence=px.colors.sequential.Blues)
plotly.offline.plot(fig, filename='s')

#Are salaries higher in 2019 than in 2018?
s=sdf
df = px.data.tips()
fig = px.pie(s, values='Salary', names='Year', color_discrete_sequence=px.colors.sequential.Blues)
#plotly.offline.plot(fig, filename='s')

s_name=sdf
df = px.data.tips()
fig = px.pie(s_name, values='Salary', names='Name', color_discrete_sequence=px.colors.sequential.Blues)
#plotly.offline.plot(fig, filename='s')

#Bar chart

sdf_job=sdf.groupby(['Job'])['Salary'].sum()
job=pd.DataFrame(data=sdf_job)
salary_bar=job.sort_values(by='Salary',ascending=False,axis=0)

fig = px.bar(salary_bar, x="Salary", y=salary_bar.index, color='Salary',color_continuous_scale='Blues',title="Average Salary per job")
#plotly.offline.plot(fig, filename='s')








