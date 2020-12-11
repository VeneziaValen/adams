import numpy as np
from matplotlib import pyplot as plt
import math
import prettytable
def f(x,y):
	return math.sin(math.radians(x*y**(2)))
ea = 8*10**(-8)
err= 1

x0 = 1
y0 = 3
xf = 2
iter = 0
it = [0]
h = 0.2


while(err > ea):
	iter=iter+1
	it.append(iter)
	print("iterasi: " ,iter)
	n= int(((xf-x0)/h)+1)
	x = np.linspace(x0,xf,n)
	print("n: " ,n)
	print("h: ", h)
	p = prettytable.PrettyTable(["X", "AB","AM","Error"])
	y = np.zeros([n])
	y[0] = y0
	py = np.zeros([n])
	error = np.zeros([n])
	error[0] = 1
	for i in range(0,4):
		py[i] = None

	for i in range(1,4):
		k1 = h*f(x[i-1],y0)
		k2 = h*f(x[i-1]+h/2,y0+k1/2)
		k3 = h*f(x[i-1]+h/2,y0+k2/2)
		k4 = h*f(x[i-1]+h,y0+k3)
		y[i] =  y0 + (k1 + 2*k2 + 2*k3 + k4)/6
		y0 = y[i]
		error[i] =1

	for i in range(4,n):
		py[i] = h/24*(55*f(x[i-1],y[i-1]) - 59*f(x[i-2],y[i-2]) + 37*f(x[i-3],y[i-3]) - 9*f(x[i-4],y[i-4]) )  + y[i-1] 
		y[i] = h/24*( 9*f(x[i],py[i]) + 19*f(x[i-1],y[i-1]) - 5*f(x[i-2],y[i-2]) + f(x[i-3],y[i-3]) ) + y[i-1]
		error[i] = abs((y[i]-py[i])/y[i])
  
	for j in range(n):
		p.add_row([round(x[j],3),py[j],y[j],error[j]])
	print(p)
 
	err = abs((y[4]-py[4])/y[4])
	e = err*19/270
	if(e>10**(-8)):
		h=h/2
		y0=y[0]
	elif(e<10**(-10)):
		h = h*2
		y0=y[0]
	else:
		h = h

	print("Error = ", err)
	print("Galat = ", e,"\n")
 
plt.subplot(211)	
plt.plot(x,py,'bo', label = 'prediktor')
plt.plot(x,y,'r-*', label = 'korektor')
plt.legend(loc = "upper left")
plt.ylabel("Nilai y")
plt.subplot(212)
plt.plot(x,error,'g-')
plt.xlabel("Nilai x")
plt.ylabel("error")
plt.show()