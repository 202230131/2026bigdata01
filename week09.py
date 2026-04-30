import numpy as np
import pandas as pd

arr2d = np.array(
    [
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
     ]
)
#dataframe은 numpy, label을 붙여서 사용가능
df_2dlist = pd.DataFrame(arr2d, columns=['a', 'b', 'c'], index=['1', '2', '3'])
df_dict = pd.DataFrame({'국어':[1,4,7],'영어':[2,5,8],'수학':[3,6,9]}, index=['1', '2', '3'])
df_dict2 = pd.DataFrame({'국어':[1,4,7],'영어':[2,5,8],'수학':[3,6,9]}, index=['1', '2', '3'])
df_dict3 = pd.DataFrame({'국어':[1,4,7],'영어':[2,5,8],'수학':[3,6,9],'미세먼지':[10,3,11]}, index=['1', '2', '3'])

print(df_dict)
print(df_2dlist)

#---------------------METHOD CHAINNIG----------------------------------------------------------------------------------
df_dict = pd.melt(df_dict).rename(columns={'variable':'var', 'value':'val'}, index={i: 'var' for i in range(10)}).sort_values('val', ascending=False)
df_dict2 = pd.melt(df_dict2).rename(columns={'variable':'var', 'value':'val'}, index={i: 'var' for i in range(10)}).query('val> 5')
#df_dict3 = pd.melt(df_dict3).drop('val', axis=1).sort_values('val', ascending=False).reset_index(drop=True)
print(df_dict)
print(df_dict2)
print(df_dict3.drop(columns=['수학','미세먼지']))
print(df_dict3.iloc[1:3])
print(df_dict3.iloc[:,[0,1,2]])
print(df_dict3.iloc[1:3,2:4]) #iloc는
#print(df_dict3.iloc[0:3].drop('2',axis=1))
print(df_dict3.iloc[np.r_[0:1,2:3]])
print(df_dict3.iloc[:,[1,3]])
print(df_dict3.loc[:,'영어':'미세먼지']) #loc는 범위지정
print(df_dict3.loc[df_dict3['국어']>3,['영어','미세먼지']])
print(df_dict3.iat[1,2])
print(df_dict3.at[1,'수학'])
print(df_dict3.sample(frac=0.5))
print(df_dict3.nlargest(2,'수학'))
print(df_dict3.tail(2))





