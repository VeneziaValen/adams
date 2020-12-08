### soal dari buku Schaum's Outlines: Differential Equations, 4th Edition
### nomor 19.7
### y' = y-x
### y(0) = 2
### x = 0,...,1



import numpy as np
from matplotlib import pyplot as plt
import math
def f(x,y):
	return math.sin(math.radians(x*y**(2)))
ea = 8*10**(-8)
err= 1
error= [err]
x0 = 1
y0 = 3
xf = 2
iter = 0
it = [0]
deltax = 0.2


while(err > ea):
	iter=iter+1
	it.append(iter)
	print("iterasi: " ,iter)
	n= int(((xf-x0)/deltax)+1)
	x = np.linspace(x0,xf,n)
	print("n: " ,n)
	print("h: ", deltax)

	y = np.zeros([n])
	y[0] = y0
	py = np.zeros([n])
	for i in range(0,4):
		py[i] = None
	for i in range(1,4):
		k1 = deltax*f(x[i-1],y0)
		k2 = deltax*f(x[i-1]+deltax/2,y0+k1/2)
		k3 = deltax*f(x[i-1]+deltax/2,y0+k2/2)
		k4 = deltax*f(x[i-1]+deltax,y0+k3)
		y[i] =  y0 + (k1 + 2*k2 + 2*k3 + k4)/6
		y0 = y[i]

	for i in range(4,n):
		py[i] = deltax/24*(55*f(x[i-1],y[i-1]) - 59*f(x[i-2],y[i-2]) + 37*f(x[i-3],y[i-3]) - 9*f(x[i-4],y[i-4]) )  + y[i-1] 
		y[i] = deltax/24*( 9*f(x[i],py[i]) + 19*f(x[i-1],y[i-1]) - 5*f(x[i-2],y[i-2]) + f(x[i-3],y[i-3]) ) + y[i-1]

	print("x_n\t   py_n\t           y_n")
	for i in range(n):
		print (round(x[i],3),"\t",format(py[i],'6f'),"\t",format(y[i],'6f'))

	err = abs((y[4]-py[4])/y[4])
	e = err*19/270
	if(e>10**(-8)):
		deltax=deltax/2
		y0=y[0]
	elif(e<10**(-10)):
		deltax = deltax*2
		y0=y[0]
	else:
		deltax = deltax
	error.append(err)
	print(err)
	print(e)

	
