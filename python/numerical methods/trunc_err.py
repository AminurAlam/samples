import numpy as np
import matplotlib.pyplot as plot

n = 10**4
x = 0
X = []
N = []

for i in range(1, n+1):
    x = x + (1/n)
    item = float(x)
    item2 = float(n)

    X.append(item)
    N.append(item2)

plot.figure()
plot.plot(N, X, marker='.')
plot.xlabel('N')
plot.xlabel('X')
plot.grid()
plot.show()
