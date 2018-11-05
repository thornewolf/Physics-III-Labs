import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Formulas
'''
stress = force/area
strain = wire_delta_length/length
youngs = stress/strain
youngs = force*length/(area*wire_delta_length)
'''

gravity = 9.79525 #m/s^2
pi = np.pi
wire_diameter = 0.7/1000 #m
wire_diameter_uncertianty = 0.0005/1000 #m
wire_crossectional_area = pi * wire_diameter**2 / 4 #m^2
wire_crossectional_area_uncertianty = np.sqrt(2)*wire_diameter_uncertianty/wire_diameter*wire_crossectional_area
wire_length = 83.4/100 #m
wire_length_uncertianty = 0.5/100 #m

mass = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) #kg
wire_delta_length = np.array([0.00, 0.21, 0.39, 0.55, 0.58, 0.80, 0.83, 0.92, 1.02, 1.08, 1.13]) #mm
wire_delta_length_uncertianty = np.array([0.005 for i in range(11)])/1

stress = mass * gravity / wire_crossectional_area #N/m^2
stress_uncertianty = wire_crossectional_area_uncertianty/wire_crossectional_area * stress
fractional_stress_uncertianty = stress_uncertianty/stress

strain = wire_delta_length / wire_length*1 #no units
strain_uncertianty = np.mean( np.sqrt((wire_delta_length_uncertianty[1:]/wire_delta_length[1:])**2 + (wire_length_uncertianty/wire_length)**2) * strain[1:])

youngs = stress[1:] / strain[1:]
youngs_uncertianty = np.mean(np.sqrt( (strain_uncertianty/strain[1:])**2 + (stress_uncertianty[1:]/stress[1:])**2 ) * youngs)
fractional_youngs_uncertianty = youngs_uncertianty/youngs

fig_name = "delta wire length vs. suspended mass"
plt.figure(fig_name)

x = mass
y = wire_delta_length
y_error = wire_delta_length_uncertianty[0]
print(y_error)
plt.scatter(x,y, c='k', s=5)
plt.errorbar(x[1:],y[1:],yerr=y_error,fmt='none',ecolor='red')

best_fit = np.poly1d(np.polyfit(x, y, 1))
actual_slope = best_fit.c[0]
best_fit_s = str(best_fit)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)

plt.legend()
plt.title(fig_name)
plt.xlabel('suspended mass (kg)')
plt.ylabel('delta wire length (mm)')
plt.grid(b=True, which = 'both', axis = 'both', linestyle='-', linewidth=1, alpha=0.1)
plt.savefig(f"{''.join(fig_name.split())}.png")

fig_name = "stress vs. strain"
plt.figure(fig_name)

x = strain[2:]
y = stress[2:]
x_error = strain_uncertianty
y_error = stress_uncertianty[0]

plt.scatter(x,y, c='k', s=5)
plt.errorbar(x[1:],y[1:],yerr=y_error,xerr=x_error,fmt='none',ecolor='red')

#plt.axis([min(x)*0.4-0.0001, max(x), min(y)*0.4, max(y)])

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

youngs: {np.mean(youngs)}
youngs_uncertainty: {youngs_uncertianty}
fractional_youngs_uncertianty: {np.mean(fractional_youngs_uncertianty)}

stress: {np.mean(stress)}
stress_uncertianty: {np.mean(stress_uncertianty)}
fractional_stress_uncertianty: {np.mean(fractional_stress_uncertianty)}

strain: {np.mean(strain)}
strain_uncertianty: {strain_uncertianty}
fractional_strain_uncertianty: {strain_uncertianty/np.mean(strain)}

stress vs strain slope: {best_fit_s}

''')