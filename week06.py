import numpy as np

#np.array([1, 2, 3]): 리스트를 넘파이 배열로 변환.
#np.zeros((행, 열)) / np.ones(): 0 또는 1로 채워진 배열 생성.
#np.arange(시작, 끝, 간격): 파이썬 range와 유사하게 균일한 간격의 배열 생성.
#np.linspace(시작, 끝, 개수): 지정된 범위 내에서 균등한 간격으로 특정 개수만큼 생성.

l1 = [1,2,3]
array01 = np.array(l1)
print(array01)
print(l1)


array02 = np.arange(0,10 ,2)
print(array02)

array03 = np.zeros((2, 3))
print(array03)

array04 = np.ones((2, 3))
print(array04)

array05 = np.full((2, 3), 5)
print(array05)

array06 = np.random.rand(2,3)
print(array06)

array = np.linspace(0,10,10)
print(array)