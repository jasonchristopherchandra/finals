import sympy

def f(x):
    return sympy.sin(x)/(1+x**2)
def simpsons(a,b,n):
    h = (b-a)/n
    x = a
    s = 0
    for i in range(1,n):
        x = x+ h
        if i%2 == 0:
            m = 2
        else:
            m = 4
        s = s + m * f(x)
    return (b-a) * (f(a)+s+f(b)) / (3*n)

n = [2,5,10,100]
a = 0
b = sympy.pi/2

x = sympy.symbols("x")
abcd = sympy.Integral((sympy.sin(x)/(1+x**2)),(x,0,sympy.pi/2))
abcde = abcd.evalf()

for i in n:
    approx = simpsons(a,b,i)
    approx = approx.evalf()
    err = approx - abcde
    print(100 * abs(err/abcde))
