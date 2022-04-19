import numpy as np
import matplotlib.pyplot as plt
from pylab import meshgrid, arange, streamplot, show
import mpl_toolkits.mplot3d
from mpl_toolkits.mplot3d import Axes3D

x, y = meshgrid(arange(-2, 2, 0.04), arange(-2, 2, 0.04))
# [X,Y,Theta]=np.mgrid[-0.5:0.5:0.05, -0.5:0.5:0.05,0:2*np.pi:np.pi/20]

vx = 2 * x - y
vy = y + x
R = 0.35
X, Y, Theta = meshgrid(arange(-2, 2, 0.04), arange(-2, 2, 0.04), arange(0, 2 * np.pi, np.pi / 20))
# Theta = meshgrid(arange(0,2*np.pi,np.pi/20))

r = np.sqrt(X ** 2 + (Y - R * np.sin(Theta)) ** 2 + (R * np.cos(Theta)) ** 2)
r3 = r ** 3
I = 100
mu0 = 4 * np.pi * 1e-7
C0 = mu0 / (4 * np.pi) * I

dBx = -C0 * R * (R - Y * np.sin(Theta)) / r3
dBy = -C0 * X * R * np.sin(Theta) / r3
dBz = -C0 * X * R * np.cos(Theta) / r3

Bx = np.pi / 40 * np.trapz(dBx, axis=2)
By = np.pi / 40 * np.trapz(dBy, axis=2)
Bz = np.pi / 40 * np.trapz(dBz, axis=2)
print(Bz)
print(Bz.shape)
plt.figure(1)
# streamplot(x, y, vy, vx)
streamplot(x, y, Bx, By)
streamplot(x, y, Bx, Bz)
show()

fig = plt.figure(2)
# ax = fig.add_subplot(111, projection='3d')
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, Bz, rstride=1, cstride=1, cmap='rainbow')  # 绘面
B = Bz
ax.contour(x, y, B, zdir='z', offset=0, cmap="rainbow")  # 生成z方向投影，投到x-y平面
ax.contour(x, y, B, zdir='x', offset=-6, cmap="rainbow")  # 生成x方向投影，投到y-z平面
ax.contour(x, y, B, zdir='y', offset=6, cmap="rainbow")  # 生成y方向投影，投到x-z平面

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

plt.figure()
CS = plt.contour(x, y, B, 2)
plt.clabel(CS, inline=1, fontsize=10)
plt.title('Simplest default with labels')

# 定义图像和三维格式坐标轴
fig = plt.figure()
ax1 = Axes3D(fig)

Bx = np.pi / 40 * np.trapz(dBx, axis=2)
By = np.pi / 40 * np.trapz(dBy, axis=2)
Bz = np.pi / 40 * np.trapz(dBz, axis=2)
r = R
a, b = 0.0, 5
theta = np.arange(0, 4 * np.pi, np.pi / 20)
x1 = a + r * np.cos(theta)
y1 = [0] * len(theta)
z1 = r * np.sin(theta)
xd = 0
yd = 0
zd = 0
ax1.scatter3D(xd, yd, zd, cmap='Blues')  # 绘制散点图
ax1.plot3D(x1, y1, z1, 'gray')  # 绘制空间曲线

plt.show()
fig = plt.figure()

ax1 = Axes3D(fig)
r = R
a, b = 0.0, 5
theta = np.arange(0, 4 * np.pi, np.pi / 20)
x1 = a + r * np.cos(theta)
y1 = [0] * len(theta)
z1 = r * np.sin(theta)
xd = 0
yd = 0
zd = 0
ax1.scatter3D(xd, yd, zd, cmap='Blues')  # 绘制散点图
ax1.plot3D(x1, y1, z1, '-->', linewidth=2, color='#B87333')  # 绘制空间曲线
r = R - 0.5
a, b = 0.0, 5
theta = np.arange(0, 4 * np.pi, np.pi / 20)
x1 = a + r * np.cos(theta)
y1 = [0] * len(theta)
z1 = r * np.sin(theta)
ax1.plot3D(x1, y1, z1, '-->', linewidth=2, color='#B87333')  # 绘制空间曲线
the = np.arange(0, 2 * np.pi, np.pi / 8)
for i in range(1, len(CS.allsegs) - 1):
    if (i != int((len(CS.allsegs)) / 2)):
        dat0 = CS.allsegs[i][0]
    for j in the:
        ax1.plot3D(dat0[:, 0] * np.cos(j), dat0[:, 1], dat0[:, 0] * np.sin(j), '-->', linewidth=0.5, color='gray')

