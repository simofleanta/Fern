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

