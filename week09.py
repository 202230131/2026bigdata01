from operator import index
import seaborn as sns
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
print(df_dict3.iloc[0:3].drop('2',axis=1))
print(df_dict3.iloc[np.r_[0:1,2:3]])
print(df_dict3.iloc[:,[1,3]])
print(df_dict3.loc[:,'영어':'미세먼지']) #loc는 범위지정
print(df_dict3.loc[df_dict3['국어']>3,['영어','미세먼지']])
print(df_dict3.iat[1,2])
print(df_dict3.at[1,'수학'])
print(df_dict3.sample(frac=0.5))
print(df_dict3.nlargest(2,'수학'))
print(df_dict3.tail(2))
-------------------------------------------#10주차------------------------------------------------------
#라벨이랑 인덱스 차이
print(df_dict3.iat[0,1])
df_dict3.lat[0,1]="23"#오류 / 원소타입이 다름
print(df_dict3(regex='[1-5]$'))# 정규표현식(문자)

df1 = pd.DataFrame({'국':['A',2,'C']},index=[1,3,4])
df2 = pd.DataFrame({'국':['A','B','C'],'수':[1,2,3]},index=[1,2,4])#A,C는 출력되나 2번째 원소는 NAN처리 됨
print(pd.merge(df1,df2,how='left',on='국'))
print(df_dict3.describe())# count,mean,max,min.....
print(df_dict3.info())
print(df_dict3.shape)
print(df_dict3['국'].value_counts())#해당 컬럼의 원소를 카운트
print(df_dict3.shape)
print(df_dict3['국'].nunique())#중복되지않는 원소의 갯수
print(df_dict3.dtypes)#원소의 타입

def square(x):
    return x*x
df = pd.DataFrame({'국':[1,1,1],'영':[2,2,2]})    
#print(df.apply(square))#각 원소를 제곱 함수안에 함수
print(df.apply(lambda x: square(x)))
print(df.apply(lambda x: x*x ))

mpg = sns.load_dataset('mpg')
print(mpg.head())
print(mpg.info())
#결측치를 해결하는 3가지 방법 1.컬럼을 삭제하던가 2.중앙값으로 채우던가 3. 평균으로 채운다.
#dropna는 행만 삭제 drop은 컬럼모두 삭제
#칼럼을 날릴경우
#결측치를 날릴경우 가중치가 적을경우 일부 행만 dropna
# 가중치가 높을경우에는 평균이나 중앙값으로 채워넣는다 중앙값이냐 평균이냐는 float냐 int냐로 나눌수있음

mpg = mpg.drop(columns=['origin','model_year','name'])
print(mpg.head())
print(mpg.info())
mpg.sort_values('mpg', ascending=False)
mpg['horsepower'] = mpg['horsepower'].fillna(
    mpg.groupby('horsepower')['horsepower'].transform('mean')
)
print(mpg.info())






