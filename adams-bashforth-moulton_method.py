### soal dari buku Schaum's Outlines: Differential Equations, 4th Edition
### nomor 19.7
### y' = y-x
### y(0) = 2
### x = 0,...,1


import numpy as np
from matplotlib import pyplot as plt
def f(x,y):
	return y-x
ea = 8*10**(-8)
err= 1
x0 = 0
y0 = 2
xf = 1
iter = 0
it = [0]
deltax = 0.1


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

	err = abs((y[n-1]-py[n-1])/y[n-1])
	print(err)
	print(err*19/270)
	if((err*19/270)>10**(-8)):
		deltax=deltax/2
	elif((err*19/270)<10**(-10)):
		deltax = deltax*2
	else:
		deltax = deltax
		exit()
	



#plt.plot(x,y,'o')
#plt.xlabel("Value of x")
#plt.ylabel("Value of y")
#plt.title("Approximation Solution with Adams-Bashforth-Moulton Method")
#plt.show()

#table 19-6
