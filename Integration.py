from sympy import *

x = symbols("x")
abcd = Integral((sin(x)/(1+x**2)),(x,0,pi/2))
print(abcd.evalf())
