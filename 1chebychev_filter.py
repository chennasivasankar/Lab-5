def CN(n,x):
	if (x<1):
		s=np.cos(N*np.arccos(x))
	else:
		s=np.cosh(N*np.arccosh(x))
	return s
import math
import matplotlib.pyplot as plt
import numpy as np
dp=float(input('Enter the dp value ;'))
ds=float(input('Enter the ds value ;'))
fs=float(input('Enter the fs value ;'))
fp=float(input('Enter the fp value ;'))
wp=2*np.pi*fp
ws=2*np.pi*fs
a=1.0/(dp**2)-1
b=1.0/(ds**2)-1
e=np.sqrt(a)
N=int(np.ceil(np.arccosh(np.sqrt(b/a))/np.arccosh(ws/wp)))
print N
w=np.linspace(0,2*np.pi*10000,2000)
H=np.zeros(2000)
for i in range(2000):
	H[i]=1/(1+(e*CN(N,w[i]/wp))**2)**0.5
plt.plot(w,H)
plt.show()
