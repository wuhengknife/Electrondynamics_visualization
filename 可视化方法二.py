import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
def U(q, r0, x, y):
    """Return the electric field vector E=(Ex,Ey) due to charge q at r0."""
    den = np.hypot(x - r0[0], y - r0[1])
    return q / den
plt.rcParams['font.sans-serif']=['SimHei']#黑体
plt.rcParams['axes.unicode_minus']=False
'''定义电荷'''
nq = 2
charges = []
for i in range(nq):
    if i % 2 == 0:
        q = 1
    else:
        q = -1
    charges.append((q, (np.cos(2 * np.pi * i / nq+np.pi/2), np.sin(2 * np.pi * i / nq+np.pi/2))))
'''绘制电容器电荷'''
nq1=80
pos1=np.linspace(-0.3,0.3,40)
charges1=[]
for i in range(nq1):
    if i % 2 == 0:
        q = 1
        charges1.append((q, (pos1[i//2], 0.2)))
    else:
        q = -1
        charges1.append((q, (pos1[i // 2], -0.2)))

'''定义网格'''
# Grid of x, y points
nx, ny = 64, 64
x = np.linspace(-2, 2, nx)
y = np.linspace(-2, 2, ny)
X, Y = np.meshgrid(x, y)
'''电势数组'''
U_array = np.zeros((nx, ny))
for charge in charges:
    delta_U = U(*charge, x=X, y=Y)
    U_array += delta_U
'''电容器电势'''
U_array1 = np.zeros((nx, ny))
for charge in charges1:
    delta_U = U(*charge, x=X, y=Y)
    U_array1 += delta_U
'''求电场'''
Ey, Ex = np.gradient(-U_array)
Ey1, Ex1 = np.gradient(-U_array1)#绘制电容器电场
'''绘图'''
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot the streamlines with an appropriate colormap and arrow style
color = 2 * np.log(np.hypot(Ex, Ey))
ax.streamplot(x, y, Ex, Ey, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

# Add filled circles for the charges themselves
charge_colors = {True: '#aa0000', False: '#0000aa'}
for q, pos in charges:
    ax.add_artist(Circle(pos, 0.05, color=charge_colors[q > 0]))

ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.set_title('磁偶极子')
'''电容器绘图'''
fig = plt.figure()
ax1= fig.add_subplot(111)

# Plot the streamlines with an appropriate colormap and arrow style
color = 2 * np.log(np.hypot(Ex1, Ey1))
ax1.streamplot(x, y, Ex1, Ey1, color=color, linewidth=1, cmap=plt.cm.inferno,
              density=2, arrowstyle='->', arrowsize=1.5)

# Add filled circles for the charges themselves
charge_colors = {True: '#aa0000', False: '#0000aa'}
for q, pos in charges1:
    ax1.add_artist(Circle(pos, 0.02, color=charge_colors[q > 0]))

ax1.set_xlabel('$x$')
ax1.set_ylabel('$y$')
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)
ax1.set_aspect('equal')
ax1.set_title('电容器电场线分布')
plt.show()