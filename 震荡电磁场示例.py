import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm, SymLogNorm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import pycharge as pc

# %% Calculate and plot E field
# Create charge and simulation objects
charge = pc.OscillatingCharge(origin=(0, 0, 0), direction=(1, 0, 0),
                              amplitude=1e-10, omega=5e17)
simulation = pc.Simulation(charge)

# Create meshgrid in x-y plane between -10 nm to 10 nm at z=0
lim = 10e-9
npoints = 1000  # Number of grid points
coordinates = np.linspace(-lim, lim, npoints)  # grid from -lim to lim
x, y, z = np.meshgrid(coordinates, coordinates, 0, indexing='ij')  # z=0

# Calculate E field components at t=0
E_x, E_y, E_z = simulation.calculate_E(t=0, x=x, y=y, z=z)

# Plot E_x, E_y, and E_z fields
E_x_plane = E_x[:, :, 0]  # Create 2D array at z=0 for plotting
E_y_plane = E_y[:, :, 0]
E_z_plane = E_z[:, :, 0]

# Create figs and axes, plot E components on log scale
fig, axs = plt.subplots(1, 3, sharey=True)
norm = SymLogNorm(linthresh=1.01e6, linscale=1, vmin=-1e9, vmax=1e9)
extent = [-lim, lim, -lim, lim]
im_0 = axs[0].imshow(E_x_plane.T, origin='lower', norm=norm, extent=extent)
im_1 = axs[1].imshow(E_y_plane.T, origin='lower', norm=norm, extent=extent)
im_2 = axs[2].imshow(E_z_plane.T, origin='lower', norm=norm, extent=extent)

# Add labels
for ax in axs:
    ax.set_xlabel('x (nm)')
axs[0].set_ylabel('y (nm)')
axs[0].set_title('E_x')
axs[1].set_title('E_y')
axs[2].set_title('E_z')

# Add colorbar to figure
Ecax = inset_axes(axs[2],
                  width="6%",  # width = 5% of parent_bbox width
                  height="100%",  # height : 50%
                  loc='lower left',
                  bbox_to_anchor=(1.05, 0., 1, 1),
                  bbox_transform=axs[2].transAxes,
                  borderpad=0,
                  )
E_cbar = plt.colorbar(im_2, cax=Ecax)  # right of im_2
E_cbar.ax.set_ylabel('E (N/C)', rotation=270, labelpad=12)

plt.show()
# %% Calculate and plot B field
# Create charge and simulation objects
charge = pc.OscillatingCharge(origin=(0, 0, 0), direction=(1, 0, 0),
                              amplitude=1e-10, omega=5e17)
simulation = pc.Simulation(charge)

# Create meshgrid in x-y plane between -10 nm to 10 nm at z=0
lim = 10e-9
npoints = 1000  # Number of grid points
coordinates = np.linspace(-lim, lim, npoints)  # grid from -lim to lim
x, y, z = np.meshgrid(coordinates, coordinates, 0, indexing='ij')  # z=0

# Calculate B field components at t=0
B_x, B_y, B_z = simulation.calculate_B(t=0, x=x, y=y, z=z)

# Plot E_x, E_y, and E_z fields
B_x_plane = B_x[:, :, 0]  # Create 2D array at z=0 for plotting
B_y_plane = B_y[:, :, 0]
B_z_plane = B_z[:, :, 0]

# Create figs and axes, plot E components on log scale
fig, axs = plt.subplots(1, 3, sharey=True)
norm = SymLogNorm(linthresh=1.01e-3, linscale=1, vmin=-1, vmax=1)
extent = [-lim, lim, -lim, lim]
im_0 = axs[0].imshow(B_x_plane.T, origin='lower', norm=norm, extent=extent)
im_1 = axs[1].imshow(B_y_plane.T, origin='lower', norm=norm, extent=extent)
im_2 = axs[2].imshow(B_z_plane.T, origin='lower', norm=norm, extent=extent)

# Add labels
for ax in axs:
    ax.set_xlabel('x (nm)')
axs[0].set_ylabel('y (nm)')
axs[0].set_title('B_x')
axs[1].set_title('B_y')
axs[2].set_title('B_z')

# Add colorbar to figure
Ecax = inset_axes(axs[2],
                  width="6%",  # width = 5% of parent_bbox width
                  height="100%",  # height : 50%
                  loc='lower left',
                  bbox_to_anchor=(1.05, 0., 1, 1),
                  bbox_transform=axs[2].transAxes,
                  borderpad=0,
                  )
E_cbar = plt.colorbar(im_2, cax=Ecax)  # right of im_2
E_cbar.ax.set_ylabel('B (T)', rotation=270, labelpad=12)

plt.show()
# %% Calculate and plot scalar and vector potentials
# Create charge and simulation objects
charge = pc.OscillatingCharge(origin=(0, 0, 0), direction=(1, 0, 0),
                              amplitude=1e-10, omega=5e17)
simulation = pc.Simulation(charge)

# Create meshgrid in x-y plane between -10 nm to 10 nm at z=0
lim = 10e-9
npoints = 1000  # Number of grid points
coordinates = np.linspace(-lim, lim, npoints)  # grid from -lim to lim
x, y, z = np.meshgrid(coordinates, coordinates, 0, indexing='ij')  # z=0

# Calculate potentials at t=0
V = simulation.calculate_V(t=0, x=x, y=y, z=z)
A_x, A_y, A_z = simulation.calculate_A(t=0, x=x, y=y, z=z)

# Plot scalar potential
V_plane = V[:, :, 0]  # Create 2D array at z=0 for plotting
fig, ax = plt.subplots()
norm = LogNorm(vmin=1e-1, vmax=1e1)
extent = [-lim, lim, -lim, lim]
im_V = ax.imshow(V_plane.T, origin='lower', norm=norm, extent=extent)
ax.set_xlabel('x (nm)')
ax.set_ylabel('y (nm)')
ax.set_title('V')
Ecax = inset_axes(ax,
                  width="6%",  # width = 5% of parent_bbox width
                  height="100%",  # height : 50%
                  loc='lower left',
                  bbox_to_anchor=(1.05, 0., 1, 1),
                  bbox_transform=ax.transAxes,
                  borderpad=0,
                  )
E_cbar = plt.colorbar(im_V, cax=Ecax)  # right of im_V
E_cbar.ax.set_ylabel('V (V)', rotation=270, labelpad=12)
plt.show()

# Plot vector potential
A_x_plane = A_x[:, :, 0]
A_y_plane = A_y[:, :, 0]
A_z_plane = A_z[:, :, 0]
fig, axs = plt.subplots(1, 3, sharey=True)
norm = SymLogNorm(linthresh=1.01e-12, linscale=1,
                  vmin=-1e-9, vmax=1e-9)
extent = [-lim, lim, -lim, lim]
im_Ax = axs[0].imshow(A_x_plane.T, origin='lower', norm=norm, extent=extent)
im_Ay = axs[1].imshow(A_y_plane.T, origin='lower', norm=norm, extent=extent)
im_Az = axs[2].imshow(A_z_plane.T, origin='lower', norm=norm, extent=extent)
for ax in axs:
    ax.set_xlabel('x (nm)')
axs[0].set_ylabel('y (nm)')
axs[0].set_title('A_x')
axs[1].set_title('A_y')
axs[2].set_title('A_z')
Ecax = inset_axes(axs[2],
                  width="6%",  # width = 5% of parent_bbox width
                  height="100%",  # height : 50%
                  loc='lower left',
                  bbox_to_anchor=(1.05, 0., 1, 1),
                  bbox_transform=axs[2].transAxes,
                  borderpad=0,
                  )
E_cbar = plt.colorbar(im_Az, cax=Ecax)  # right of im_Az
E_cbar.ax.set_ylabel('A (V*s/m)', rotation=270, labelpad=12)
plt.show()