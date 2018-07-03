import matplotlib.pyplot as plt
import math

x = math.pi/3
actual = math.sin(x)
s = 0
error = []
nList = [5,10,20,50]

def f(n):
     return ((-1)**n) * (x **(2*n+1))/(math.factorial((2*n+1)))

for n in nList:
    for i in range(n):
        s += f(i)
    error.append(s-actual)
    s = 0

plt.plot(nList,error)
plt.show()
