import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
'''定义三维磁场分布'''
def B(dl,x_0,x_1):
    n=x_1.shape[0]
    m=x_0.shape[0]
    result=[[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            sum1=0
            for k in range(m):
                r=x_1[i,j]-x_0[k]
                sum1+=np.cross(dl[k],r)/(r[0]**2+r[1]**2+r[2]**2)**1.5
                print(sum1)
            result[i].append(sum1)
    return  result





'''定义线圈分布'''
m=21
theta=np.linspace(0,2*np.pi,m)
x_0=np.array([[np.sin(i),np.cos(i),0] for i in theta])
dl=np.array([x_0[i+1]-x_0[i] for i in range(m-1)])
x_0=x_0[:-1]
x_01=np.array([[2*np.sin(i),2*np.cos(i),0] for i in theta])
dl_1=np.array([x_01[i]-x_01[i+1] for i in range(m-1)])
x_01=x_01[:-1]
'''定义网络'''
ny,nz=20,20
y=np.linspace(-5,5,ny)
z=np.linspace(-5,5,nz)
Y,Z=np.meshgrid(y,z)
X=np.zeros((ny,nz))
x_1=np.stack([X,Y,Z],axis=2)
result1=np.array(B(dl,x_0,x_1))
result2=np.array(B(dl_1,x_01,x_1))
By=result1[:,:,1]
Bz=result1[:,:,2]
factor=1#定义因子
By1=result1[:,:,1]+result2[:,:,1]*factor
Bz1=result1[:,:,2]+result2[:,:,2]*factor
By2=result1[:,:,1]+result2[:,:,1]*(-1)
Bz2=result1[:,:,2]+result2[:,:,2]*(-1)
fig,axs=plt.subplots(3,1,figsize=(8,18))
color = 2 * np.log(np.hypot(By, Bz))
color1=2*np.log(np.hypot(By1,Bz1))
color2=2*np.log(np.hypot(By2,Bz2))
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.rcParams['axes.unicode_minus']=False
axs[0].streamplot(y, z, By, Bz, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)
axs[0].set_title('单个圆环的磁感线')
axs[1].streamplot(y, z, By1, Bz1, color=color1, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)
axs[1].set_title("反向电流圆环的磁感线")
axs[2].streamplot(Y, Z, By2, Bz2, color=color1, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)
axs[2].set_title("同相电流的磁感线")

plt.show()