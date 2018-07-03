import math
from matplotlib.pyplot import *


x =math.pi/3
actual = math.sin(x)
s = 0
n=10

def f(n):
    return ((-1)**n) * (x **(2*n+1))/(math.factorial((2*n+1)))

for n in range(n):
    s += f(n)
error = (actual - s )
print(error)
