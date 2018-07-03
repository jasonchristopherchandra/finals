import math
import numpy

x = math.pi/3 

def f(n):
    return (-1)**n * (x)**(2*n+1)/(2*n+1)

def array_est(n):
    result = 0.0
    for i in range(n):
        result += f(i)
    return result

nList = [3,5,10,20]

actual = numpy.arctan(x)

for i in nList:
    esti = array_est(i)
    error = (esti-actual)
    print(str(i) + "  "+ str(esti)+ "  "+str(actual)+ "  "+str(error))
