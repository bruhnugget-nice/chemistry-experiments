import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
df=df[['z', 'n', 'symbol', 'binding']]
df=df.dropna()

fig = px.scatter_3d(df, x='z', y='n', z='binding', color='symbol')
fig.show()