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

#subset data 

odf['Year']=odf['Date'].dt.year
odf['Month']=odf['Date'].dt.month_name()
odf['Day']=day=odf['Date'].dt.day_name()

#exploring data by month
Opperational_view=odf.groupby(['Opp_costs'])[['Costs']]
print(Opperational_view.mean())

Monthly_view=odf.groupby(['Month'])[['Costs']]
print(Monthly_view.mean())
