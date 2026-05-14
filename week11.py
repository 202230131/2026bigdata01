import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'국':[7, 6, 7],
                        '영':[2, 4, 8],
                        '수':[3, 5, 9],
                        '화':[10, 3, 11]}, index=[1, 2, 3]) #90도로 꺾어서 봐야함
print(df.info())
print(df.describe())
print(df.describe(include='all'))
print(df.describe(include='all').transpose())
print(df.memory_usage())
print(len(df))

mpg = sns.load_dataset('mpg')
print(mpg['model_year'].value_counts().sort_values(ascending=False))
mpg = mpg.drop(columns=['model_year','origin','name'])
print(mpg.info())
print(mpg.head())
#print(mpg.sort_values('mpg',ascending=False))
mpg['horsepower'] = mpg['horsepower'].fillna(mpg.groupby('cylinders')['horsepower'].transform('median'))
print(mpg.info())

print((mpg.groupby('cylinders')['horsepower'].median()))
#---------------------------------------------------------------------------------------------------------------------

ex = sns.load_dataset('exercise')
print(ex['kind'].value_counts())
print(ex['time'].value_counts())
print(ex['diet'].value_counts())
print(ex.info())
print(ex[ex['diet'] == 'low fat'])
print(ex[ex['diet'] == 'no fat'])
print(len(ex[ex['diet'] == 'no fat']))
running_df = ex[ex['kind'] == 'running']
print(running_df)
sns.catplot(running_df, x='time',y='pulse',hue='diet',kind='point')
#print(sns.catplot(running_df, x='time',y='pulse',kind='point'))

plt.show()

ex1 = ex[(ex['diet'] == 'low fat') & (ex['time'] == '30 min') & (ex['kind'] == 'running')]
print(ex1)
mean_pulse = ex1['pulse'].mean()
print(mean_pulse)