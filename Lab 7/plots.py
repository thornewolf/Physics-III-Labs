import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#constants
gravity = 9.79525 #m/s^2
pi = np.pi

def graph(fig_name, x, y, xlabel, ylabel, y_error):
    plt.figure(fig_name)
    plt.scatter(x,y, c='k', s=2)
    plt.errorbar(x,y,yerr=y_error,fmt='none',ecolor='red')
    best_fit = np.poly1d(np.polyfit(x, y, 1))
    actual_slope = best_fit.c[0]
    best_fit_s = str(best_fit)
    plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)
    plt.title(fig_name)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(b=True, which = 'both', axis = 'both', linestyle='-', linewidth=1, alpha=0.1)

    N = len(x)
    D = N * sum(x**2) - sum(x)**2
    slope_uncertianty = np.sqrt(N/D)*y_error
    intercept_uncertianty = np.sqrt(sum(x**2)/D)*y_error

    if y_error != None:
        plt.errorbar(x,y,yerr=y_error,fmt='none',ecolor='red')

    plt.savefig(f"{''.join(fig_name.split())}.png")
    print(f'''
plotting for {fig_name}
    x = {xlabel}
        avg = {np.mean(x)}
    y = {ylabel}
        avg = {np.mean(y)}
    best fit equation = {best_fit_s[2:]}
        slope = {actual_slope}
        slope_uncertianty = {slope_uncertianty}
        intercept_uncertianty = {intercept_uncertianty}
        ''')
    return {'slope':actual_slope, 'slope_uncertianty':slope_uncertianty, 'intercept_uncertianty':intercept_uncertianty}

'''
Formulas
x = F/k
period = 2*pi*sqrt(mu/k)
mu = m + M/3
'''

fig_name = "Part 1: Streching"
mass = np.array([20.3, 40.0, 60.5, 80.3, 100.5, 120.4, 140.4, 160.5, 180.4, 200.4, 220.5, 240.5, 260.6, 280.3, 300.2])/1000 #kg
mass_uncertianty = 0.05/1000 #kg
delta_x = np.array([1.5, 2.2, 3.1, 3.7, 4.7, 5.4, 6.4, 6.9, 7.6, 8.5, 9.3, 10.2, 10.9, 11.8, 12.5])/100 #m
delta_x_uncertianty = 0.05/100 #m
force = mass * gravity
force_uncertianty = mass_uncertianty * gravity
graph(fig_name, delta_x, force, 'delta_x (m)', 'force (N)', force_uncertianty)
k = force/delta_x
print(f'k = {np.mean(k)}')

fig_name = "Part 2: Ocsillations"
mass = mass
mass_uncertianty = 0.05/1000 #kg
mass_of_spring = 17.5/1000 #kg
mass_of_spring_uncertianty = 0.05/1000 #kg
period = np.array([0.2733, 0.343, 0.393, 0.4125, 0.4355, 0.4605, 0.5048, 0.5358, 0.5565, 0.5828, 0.6213, 0.637, 0.66, 0.6838, 0.7045]) #s
period_squared = period ** 2 #s^2
inertial_mass = mass + mass_of_spring/3
inertial_mass_uncertianty = np.sqrt(mass_uncertianty**2 + mass_of_spring_uncertianty**2/3)
r = graph(fig_name, period_squared, inertial_mass, 't^2 (s)', 'intertial mass (kg)', inertial_mass_uncertianty)
slope = r['slope']
predicted_k = slope*4*pi**2
print(f'    predicted k = {predicted_k}')
