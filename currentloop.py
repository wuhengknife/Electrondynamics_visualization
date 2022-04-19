import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

r = np.linspace(0.01,1,234)
theta = np.linspace(0.001,np.pi-0.001,200)

[R,T] = np.meshgrid(r,theta)
Y = R*np.cos(T)
X = R*np.sin(T)

a = 0.2
tmp1 = 3.5*a/np.sqrt(a**2 + R**2 + 2*a*R*np.sin(T))
k2 = 4*a*R*np.sin(T)/(a**2 + R**2 + 2*a*R*np.sin(T))
tmp2 = (2 - k2)*sp.ellipk(k2) - 2*sp.ellipe(k2)
tmp3 =  tmp1*tmp2/k2
result1 = R*np.sin(T)*tmp3




a = 0.5
tmp1 = -.3*a/np.sqrt(a**2 + R**2 + 2*a*R*np.sin(T))
k2 = 4*a*R*np.sin(T)/(a**2 + R**2 + 2*a*R*np.sin(T))
tmp2 = (2 - k2)*sp.ellipk(k2) - 2*sp.ellipe(k2)
tmp3 =  tmp1*tmp2/k2
result2 = R*np.sin(T)*tmp3

result = result1
result = result1 + result2


plt.contour(X,Y,result,100)
plt.contour(-X,Y,result,100)
#plt.contour(X,-Y,T2,30)
plt.axis('equal')
plt.show()
