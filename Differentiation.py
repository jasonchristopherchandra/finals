from matplotlib.pyplot import plot,show

def f(x):
    return 2*(x**2)+(6*x)+4

def diff(x,h):
    return -3*f(x)-4*(x+h)-f(x-(2*h))/(2*h)

x = 2
h = [0.01,0.05,0.1,0.2,0.5]
error = []

actual = 4*x+6

for i in h:
    est = diff(x,i)
    err = abs(est- actual)
    error.append(err)
    print(actual,est, err)

plot(h,error)
show()
