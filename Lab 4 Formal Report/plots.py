import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
    plt.legend()
    N = len(x)
    D = N * sum(x**2) - sum(x)**2
    slope_uncertainty = np.sqrt(N/D)*y_error
    intercept_uncertainty = np.sqrt(sum(x**2)/D)*y_error

    if y_error != None:
        plt.errorbar(x,y,yerr=y_error,fmt='none',ecolor='red')

    plt.savefig(f"Lab 4 Formal Report/images/{''.join(fig_name.split())}.png")
    print(f'''
plotting for {fig_name}
    x = {xlabel}
        avg = {np.mean(x)}
    y = {ylabel}
        avg = {np.mean(y)}
    best fit equation = {best_fit_s[2:]}
        slope = {actual_slope}
        slope_uncertainty = {slope_uncertainty}
        intercept_uncertainty = {intercept_uncertainty}
        ''')
    return {'slope':actual_slope, 'slope_uncertainty':slope_uncertainty,
        'intercept_uncertainty':intercept_uncertainty}

#Varying the radius
r = np.array([0.15, 0.17, 0.18, 0.14, 0.16])
t = np.array([1.597, 1.14, 1.101, 2.36, 1.43])
t_squared = t**2
goal_slope = 0.2418/(4*np.pi**2*0.1365) #Fc/(4pi^2M)T^2
x,y = t_squared,r
graph("Varying Radius", x, y, "Period Squared (s^2)", "Radius (m)", 0.005)

#Varying the force
plt.figure("Varying Force")
f = np.array([0.5396, 1.0301, 0.7358, 1.2263, 0.4415])
t = np.array([1.335, 1, 1.163, 0.948, 1.386])
inverse_t_squared = 1/(t**2)
goal_slope = 4*np.pi**2*0.1365*0.16 #4pi^2Mr * 1/T^2

x,y = inverse_t_squared,f
graph("Varying Force", x, y, "Inverse Period Squared (1/s^2)", "Force (N)", 0.05)



#Varying the mass
m = np.array([0.1462, 0.1065, 0.2063])
t = np.array([1.211, 1.045, 1.339])
f = 0.7358
for index in range(3):
    expected_force = 4*np.pi**2*m[index]*0.16/t[index]
    print(f'''
Varying Mass
The ideal mass is {expected_force}
The actual slope is {f}
The percent difference is {(f-expected_force)/expected_force*100}%
    ''')
