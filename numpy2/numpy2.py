"""
Date: 2025.03.14
Program: np-array (Numpy Array)
"""

import numpy as np

"""
a = np.array([[1, 2], [3, 4]])
b = np.array([[4, 5], [6, 7]])
r1 = a + b
r2 = a - b
r3 = a * b
r4 = a / b

print(r1)
print(r2)
print(r3)
print(r4)
"""



"""
# p90 Slicing (배열 쪼개기)
m1 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9],
               [0, 1, 2]])


print(m1)
print(m1[0][2])     #index는 0부터 시작
print(m1[2])
print(m1[1:])

print(m1[1:][0:2])

print("m1.shpae: ", m1.shape)
len0, len1 = m1.shape
print("len0: ", len0)
print("len1: ", len1)
for i in range(len0):
    for j in range(len1):
        print(m1[i][j], m1[i,j])     

print(m1[1: , 0:2])
"""



"""
# 구구단 출력
# 2 * 1 = 2
for i in range(2,10) :
    for j in range(1,10) :
        print(i, "*", j, "=", i*j)
"""



"""
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])
logic =  a [a % 2 == 0]         #a를 2로 나눴을 때 나머지가 0인 수들의 원소 추출
print(logic)
"""



# append, reshape
a = np.array([1, 2])      # 1X2
b = np.array([[4, 5], [7, 8]])     # 2X2
c = np.append(a,b)      # 1X9
print(c)

# 행렬의 크기를 변환 .reshape()
d = np.reshape(c, (-1, 3))
print(d)




