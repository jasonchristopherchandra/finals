from math import sqrt
import matplotlib.pyplot as plotter

myfile = open("test.csv")

x = []
y = []
x3 = []
root = []

for i in range (0,5):
    line = myfile.readline()
    splitter = line.split(",")
    x.append(int(splitter[0]))
    y.append(int(splitter[1]))

myfile.close()

for z in range(0,5):
    x3.append(x[z]**3)
    root.append(sqrt(x[z]+y[z]))

xside = plotter.subplot(1,2,1)
xside.plot(x,x3)
yside = plotter.subplot(1,2,2)
yside.plot(y,root)
plotter.show()
