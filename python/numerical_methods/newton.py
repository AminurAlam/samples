import math
import numpy as np
from copy import *

x = [10, 20, 30, 40, 50]
y = [46, 66, 81, 93, 101]

n = len(x)
b = [0,0,0,0,0]
h = x[1] - x[0]
xn = 15
r=(xn-x[0])/float(h) # r = 0.5
s = y[0]
a = copy(y)

for j in range(1, n):
    for i in range(n-1, j-1, -1):
        a[i] = a[i] - a[i-1]
print(a)


print(a)
tem=1
n=len(a)-1
fact=1
for i in range(1,n+1):
    fact =  fact *i
    tem=tem*(r-i+1)/fact
    s+=tem *a[i] 
print("Newtons Interpolation",s)
