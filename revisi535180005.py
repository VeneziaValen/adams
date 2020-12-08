### soal dari buku Schaum's Outlines: Differential Equations, 4th Edition
### nomor 19.7
### y' = y-x
### y(0) = 2
### x = 0,...,1


import numpy as np
import math
def f(x,y):
	return 1+2*y-y**(2)
ea = 1*10**(-6)
err= 1
x0 = 0
y0 = 0
xf = 2
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
	arrerr = np.zeros([n])
	y[0] = y0
	py = np.zeros([n])
	for i in range(0,4):
		py[i] = None
		arrerr[i] = None

	for i in range(1,4):
		k1 = deltax*f(x[i-1],y0)
		k2 = deltax*f(x[i-1]+deltax/2,y0+k1/2)
		k3 = deltax*f(x[i-1]+deltax/2,y0+k2/2)
		k4 = deltax*f(x[i-1]+deltax,y0+k3)
		y[i] =  y0 + (k1 + 2*k2 + 2*k3 + k4)/6
		y0 = y[i]

	for i in range(4,n):
		py[i] = deltax/24*(55*f(x[i-1],y[i-1]) - 59*f(x[i-2],y[i-2]) + 37*f(x[i-3],y[i-3]) - 9*f(x[i-4],y[i-4]) )  + y[i-1] 
		y[i] = round(deltax/24*( 9*f(x[i],py[i]) + 19*f(x[i-1],y[i-1]) - 5*f(x[i-2],y[i-2]) + f(x[i-3],y[i-3]) ) + y[i-1],6)
		arrerr[i] = round(abs((y[i]-py[i])/y[i]),6)*19/270
		err = arrerr[4]

	print("x_n\t   py_n0\t           y_n1\t   galat")
	for i in range(n):
		print (round(x[i],3),"\t",format(py[i],'6f'),"\t",format(y[i],'6f'),"\t",'{:.2e}'.format(arrerr[i],'6f'))

	if(arrerr[iter+3]) > 1*10**(-6):
		deltax = deltax/2
		y0 = 0
	elif(arrerr[iter+3]) < 1*10**(-8):
		deltax = deltax*2
		y0 = 0
	else:
		deltax = deltax
		break
	



#plt.plot(x,y,'o')
#plt.xlabel("Value of x")
#plt.ylabel("Value of y")
#plt.title("Approximation Solution with Adams-Bashforth-Moulton Method")
#plt.show()

#table 19-6
