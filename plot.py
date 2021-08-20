import matplotlib.pyplot as plt
import numpy as np

a1=0
b1=0
a2=0
b2=0


# input section
upx = float(input('upx = '))
upy = float(input('upy = '))

dnx = float(input('dnx = '))
dny = float(input('dny = '))

# formulating parameters for input in the quadradic 
x = np.arange(0,upx)

a1 = float(upy/(2*upx*upx))
b1 = float(upy/(2*upx))

y1 = a1*x*x + b1*x
py1 = a1*upx*upx + b1*upx

plt.plot(x,y1, 'r-')
# formulating parameters for input in the quadradic 
x = np.arange(0,dnx)

a2 = float(dny/(2*dnx*dnx))
b2 = float(dny/(2*dnx))

y2 = a2*x*x + b2*x
py2 = a2*dnx*dnx + b2*dnx

plt.plot(x,y2, 'r-')
# straight line intersection
p1 = [upx, py1]
p2 = [dnx, py2]

x_val = [p1[0], p2[0]]
y_val = [p1[1], p2[1]]

# plot
plt.plot(x_val, y_val, 'r-')
plt.show()