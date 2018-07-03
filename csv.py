from math import sqrt

myfile = open("test.csv")

x = []
y = []

for i in range(0,5):
    line = myfile.readline();
    splitter = line.split(",")
    x.append(int(splitter[0]))
    y.append(int(splitter[1]))
1
myfile.close()

for z in range(0,5):
    print(str(x[z]),"  ",str(x[z]**3),"  ",str(y[z]),"  ",str(sqrt(x[z]+y[z])))
