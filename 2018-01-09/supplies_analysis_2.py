import pandas as pd
import morestats as m

df = pd.read_csv('supplies.csv')

df.groupby(['Region','Rep'])['Total'].agg(['mean', 'sum', 'count'])

regions = df.groupby(['Region'])['Total'].agg(['mean', 'sum', 'count'])

repcouts = df.groupby(['Region'])['Rep'].agg(['count'])
reps = df.groupby(['Region'])['Rep'].unique()
frames = [repcouts,reps]
result = pd.concat(frames, axis =1)
