import numpy as np
import matplotlib.pyplot as plt
import math
dp=input('Enter the dp value ;')
ds=input('Enter the ds value ;')
ws=float(input('Enter the ws value ;'))
wp=input('Enter the wp value ;')
a=math.log((1.0/(dp*dp)-1)/(1.0/(ds*ds)-1))
b=math.log(wp/ws)
N=math.ceil(0.5*(a/b))
print N
wc=(wp/(1.0/(dp*dp)-1)**(0.5/N))
print wc
w=np.linspace(0,2000,1000)
h_w=1/(1+(w/wc)**(2*N))**0.5
h=-10*np.log10(1/(1+(w/wc)**(2*N))
plt.plot(w,h_w)
plt.show()
plt.plot(w,h)
plt.show()


