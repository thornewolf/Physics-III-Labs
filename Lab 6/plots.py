import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Formulas
'''
stress = force/area
strain = wire_delta_length/length
youngs = stress/strain
'''

gravity = 9.79525
pi = np.pi
wire_diameter = 0.0007 #m
wire_diameter_uncertianty = 0.000005 #m
wire_crossectional_area = pi * wire_diameter**2 / 4
wire_length = 0.834 #m
wire_length_uncertianty = 0.005 #m


mass = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
wire_delta_length = np.array([0.00, 0.21, 0.39, 0.55, 0.58, 0.80, 0.83, 0.92, 1.02, 1.08, 1.13])

stress = mass * gravity / wire_crossectional_area
strain = wire_delta_length / wire_length


youngs = stress[1:] / strain[1:]

fig_name = "delta wire length vs. suspended mass"
plt.figure(fig_name)

x = mass
y = wire_delta_length
plt.scatter(x,y, c='r', s=5)

best_fit = np.poly1d(np.polyfit(x, y, 1))
actual_slope = best_fit.c[0]
best_fit_s = str(best_fit)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)

plt.legend()
plt.title(fig_name)
plt.xlabel('suspended mass (kg)')
plt.ylabel('delta wire length (m)')
plt.grid(b=True, which = 'both', axis = 'both', linestyle='-', linewidth=1, alpha=0.1)
plt.savefig(f"{''.join(fig_name.split())}.png")

fig_name = "stress vs. strain"
plt.figure(fig_name)

x = strain
y = stress

plt.scatter(x,y, c='r', s=5)

best_fit = np.poly1d(np.polyfit(x, y, 1))
actual_slope = best_fit.c[0]
best_fit_s = str(best_fit)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)

plt.legend()
plt.title(fig_name)
plt.xlabel('strain')
plt.ylabel('stress (N/m^2)')
plt.grid(b=True, which = 'both', axis = 'both', linestyle='-', linewidth=1, alpha=0.1)
plt.savefig(f"{''.join(fig_name.split())}.png")

print(f'''
wire_crossectional_area: {wire_crossectional_area}
''')