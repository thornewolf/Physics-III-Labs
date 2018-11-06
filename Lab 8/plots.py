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
    plt.legend()
    N = len(x)
    D = N * sum(x**2) - sum(x)**2
    slope_uncertainty = np.sqrt(N/D)*y_error
    intercept_uncertainty = np.sqrt(sum(x**2)/D)*y_error

    if y_error != None:
        plt.errorbar(x,y,yerr=y_error,fmt='none',ecolor='red')

    plt.savefig(f"Lab 8/{''.join(fig_name.split())}.png")
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

def hist(fig_name, x, xlabel):
    fig_name = fig_name+" Histogram"
    plt.figure(fig_name)
    plt.title(fig_name)
    plt.grid(axis='y', alpha=0.2)
    std = np.std(x, axis=None, dtype=None, out=None, ddof=0, keepdims=np._NoValue)
    mean = np.mean(x, axis=None, dtype=None, out=None, keepdims=np._NoValue)
    plt.hist(x, bins=None, range=None, density=None, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, normed=None, hold=None, data=None)
    plt.xlabel(xlabel)
    plt.ylabel('occurances')
    print(f'''
    plotting histogram for {fig_name}
    x = {xlabel}
        mean = {mean}
        std = {std}
    ''')

    plt.savefig(f"Lab 8/{''.join(fig_name.split())}.png")
'''
Formulas
R = V/I
'''
fig_name = "Part 1: Resistor"

voltage = np.array([3,4,5,6,7,8,9,10,11,12,13,14,15]) #V
voltage_uncertainty = 0.25 #V
current = np.array([3.2,4.3,5.31,6.35,7.32,8.3,9.32,10.4,11.4,12.39,13.55,14.35,15.45])/1000 #I
current_uncertainty = 0.005/1000 #I
resistance = voltage/current #ohm
resistance_uncertainty = np.mean(resistance*np.sqrt((
    voltage_uncertainty/voltage)**2+(current_uncertainty/current)**2)) #ohm
graph(fig_name,voltage,resistance,"Voltage (V)",r"V/I (ohm)",resistance_uncertainty)
hist(fig_name, resistance, "resistance (ohm)")

fig_name = "Part 2: Lightbulb"
voltage = np.array([0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0])
voltage_uncertainty = 0.25 #V
current = np.array([13.5,18.9,24.6,28.4,30.0,33.7,37.5,40.1,42.2,44.2,47.8,50.2])/1000 #I
current_uncertainty = 0.005/1000 #I
resistance = voltage/current #ohm
resistance_uncertainty = np.mean(resistance*np.sqrt((
    voltage_uncertainty/voltage)**2+(current_uncertainty/current)**2)) #ohm
graph(fig_name,voltage,resistance,"Voltage (V)",r"V/I (ohm)",resistance_uncertainty)
hist(fig_name, resistance, "resistance (ohm)")
