import math

def fibonacci(n):
	if n==0:
		return 0
	else:
		ultimo=1
		penultimo=0
		i=1
		while i<n:
			suma=ultimo+penultimo
			penultimo=ultimo
			ultimo=suma
			i=i+1
		return ultimo
	
def serieFibonacci(n):
	x=[0,1]
	if n==0:
		return [0]
	while len(x)<n:
		x[len(x):]=[x[len(x)-1]+x[len(x)-2]]
	return x
		
def esPrimo(x):
	if x<=1:
		return False
	elif x<=3:
		return True
	elif x%2==0  or x%3==0:
		return False
	i=5                               #k=1
	while i**2<=x:
		if x%i==0 or x%(i+2)==0:  #{6k-1, 6k+1} | k=1->{5,7}; k=2-> {7,9}; ... 
		  return False
		i=i+6                     #k=k+1
	return True

def conjeturaCollatz(x):
	arreglo=[]
	while x != 1:
		pasos=len(arreglo)
		arreglo[pasos:]=[x]
		if x%2==0:
			x=int(x/2)
		else:
			x=3*x+1
	pasos=pasos+1
	arreglo[pasos:]=[1]
	return {'n': pasos , 'vector': arreglo }

def mcd(x1,x2):
	if x2>x1:
		reserva=x1
		x1=x2
		x2=reserva
	while x2!=0:
		reserva=x1
		x1=x2
		x2=reserva%x2
	return x1

def mcm(x1,x2):
	return x1*x2/mcd(x1,x2)

def formaIrreducible(x):
	str_x=str(x)
	n=str_x.find(".")
	if n==-1:
	    return str_x
	p=int(str_x[0:n]+str_x[n+1:len(str_x)])
	q=10**(len(str_x)-n-1)
	n=mcd(p,q)
	p=int(p/n)
	q=int(q/n)
	return str(p)+ '/' + str(q)
