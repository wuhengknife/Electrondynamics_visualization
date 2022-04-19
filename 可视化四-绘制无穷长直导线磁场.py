import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
def B(I,x_0,x_1):
    n=x_1.shape[0]
    result=[[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            r=x_1[i,j]-x_0
            temp=np.array([r[1],r[0]*-1])/(r[0]**2+r[1]**2)*I
            result[i].append(temp)
            print(temp)
    return np.array(result)

'''网格设计'''
ny,nz=20,20
y=np.linspace(-5,5,ny)
z=np.linspace(-5,5,nz)
Y,Z=np.meshgrid(y,z)
x_1=np.stack([Y,Z],axis=2)
'''定义直导线'''
I=np.array([1])
pos=np.array([[0,0]])
n=I.shape[0]
I1=np.array([2,2,-2,-2])
pos1=np.array([[1,1],[-1,1],[-1,-1],[1,-1]])
n1=I1.shape[0]
'''绘制磁感线'''
B1=np.zeros((ny,nz,2))
for i in range(n):
    print(I[i],pos[i])
    B1+=B(I[i],pos[i],x_1)
B2=np.zeros((ny,nz,2))
for i in range(n1):
    print(I1[i],pos1[i])
    B2+=B(I1[i],pos1[i],x_1)
'''绘图'''
print(B1.shape)
fig,ax=plt.subplots()
color1=2*np.log(np.hypot(B1[:,:,0],B1[:,:,1]))
print(color1.shape)
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.rcParams['axes.unicode_minus']=False
ax.streamplot(y, z, B1[:,:,0], B1[:,:,1], color=color1, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)
ax.set_title("单个直导线的磁场分布")
'''多直导线的交互'''
fig1,ax1=plt.subplots()
color2=2*np.log(np.hypot(B2[:,:,0],B2[:,:,1]))
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.rcParams['axes.unicode_minus']=False
ax1.streamplot(y, z, B2[:,:,0], B2[:,:,1], color=color2, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)
for i in range(n1):
    ax1.add_artist(Circle(pos1[i], 0.05, color='#aa0000'))
ax1.set_title("多个直导线的分布")
plt.show()