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

#best sale rev
best_sales=sale.groupby(["Product_px", "Unit_px"]).sum().sort_values(["Sale_rev"],ascending=False)
print(best_sales.head(5))

print(best_sales.to_markdown())

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

#striplot
sns.stripplot(x='Sale_rev', y='Month', jitter=0.50, size=9, alpha=0.7, hue='Year', palette='Blues',marker='*', linewidth=1, edgecolor='white',data=sale)
plt.show()

################################################################################################################

#STAFFING 

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
#plotly.offline.plot(fig, filename='s')

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

December=sdf[sdf.Month=='December']
print(December.to_markdown())

sns.stripplot(x='Salary', y='Job', jitter=0.30, size=7, alpha=0.7, hue='Year', palette='Blues',marker='D', linewidth=1, edgecolor='white',data=sdf)
plt.show()

###################################################################################################################

#Operational 

#open file
o=pd.read_csv('opp.csv')
print(o.columns)
odf=DataFrame(o.head(50))
print(odf.head(53))
#b=df.dtypes

#indexing to datetime
odf['Date']=pd.to_datetime(odf['Date'], infer_datetime_format=True)
indexeddf=odf.set_index(['Date'])
print(indexeddf.head(5))

#parsing to format
odf['Date']=pd.to_datetime(odf['Date'], format='%y-%m-%d')

#extracting for all 
day=odf['Date'].dt.day_name()
month=odf['Date'].dt.month_name()
year=odf['Date'].dt.year

print(odf.to_csv("odf.csv"))

#subset data 

odf['Year']=odf['Date'].dt.year
odf['Month']=odf['Date'].dt.month_name()
odf['Day']=day=odf['Date'].dt.day_name()

#exploring data by month
Opperational_view=odf.groupby(['Opp_costs'])[['Costs']]
print(Opperational_view.mean())

Monthly_view=odf.groupby(['Month'])[['Costs']]
print(Monthly_view.mean())

#Where is the money?

#highest costs in months
highest_costs=odf.groupby(["Opp_costs", "Month"]).sum().sort_values(["Costs"],ascending=False)
print(highest_costs)

opp_costs=odf.groupby(["Opp_costs"]).sum().sort_values(["Costs"],ascending=False)
print(opp_costs)

#hottet month

Hot_month=odf.groupby(["Month"]).sum().sort_values(["Costs"],ascending=False)
print(Hot_month)

#pie charts

o=odf
df = px.data.tips()
fig = px.pie(o, values='Costs', names='Opp_costs', color_discrete_sequence=px.colors.sequential.Blues)
#plotly.offline.plot(fig, filename='o')

#Hottest months
o=odf
df = px.data.tips()
fig = px.pie(o, values='Costs', names='Month', color_discrete_sequence=px.colors.sequential.Blues)
#plotly.offline.plot(fig, filename='o')

#hottest year

o=odf
df = px.data.tips()
fig = px.pie(o, values='Costs', names='Year', color_discrete_sequence=px.colors.sequential.Blues)
#plotly.offline.plot(fig, filename='o')

#hottet year markdown

Hot_month=odf.groupby(["Year"]).sum().sort_values(["Costs"],ascending=False)
print(Hot_month.to_markdown())


#Bar chart

odf_cost=odf.groupby(['Opp_costs'])['Costs'].mean()
cost=pd.DataFrame(data=odf_cost)
cost_bar=cost.sort_values(by='Costs',ascending=False,axis=0)

fig = px.bar(cost_bar, x="Costs", y=cost_bar.index, color='Costs',color_continuous_scale='Blues',title="Cost per opperations")
#plotly.offline.plot(fig, filename='o')

#markdown tables on banking 
R_D=odf[odf.Opp_costs=='R&D']
print(R_D.to_markdown())

#cost in December 
December=odf[odf.Month=='December']
print(December.to_markdown())








