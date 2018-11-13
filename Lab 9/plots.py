import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#constants
gravity = 9.79525 #m/s^2
pi = np.pi

def graph(fig_name, x, y, xlabel, ylabel, y_error):
    plt.figure(fig_name)
    plt.scatter(x,y, c='k', s=10)
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

    plt.savefig(f"Lab 9/{''.join(fig_name.split())}.png")
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

def percent_difference(observed, theoretical):
    return (observed-theoretical)/theoretical * 100

'''
Formulas
delta_length/initial_length = alpha*delta_temp
'''
fig_name = "Thermal Expansion of a Aluminum Rod"
temperatures = np.array([81, 76, 71, 66, 61, 56, 51, 46, 41, 36, 31, 27]) #C
temperature_uncertainty = 0.5 #C
base_temperature = temperatures[-1]
length_naught = 52/100 #m
length_naught_uncertainty = 0.05/100 #m
lengths = np.array([7.43, 6.98, 6.65, 6.64, 6.65, 6.34, 6.40, 6.10, 6.00, 5.90, 5.57, 5.48])/1000 #m
base_length = lengths[-1] #mm
length_uncertainty = 0.11/1000
delta_temperatures = temperatures - base_temperature
delta_temperature_uncertainty = temperature_uncertainty
delta_lengths = lengths - base_length
fractional_length_change = delta_lengths/length_naught
total_y_uncertainty = np.mean(fractional_length_change*np.mean((delta_temperature_uncertainty/delta_temperatures[:-1])**2 + (length_uncertainty/delta_lengths[:-1])**2 + (length_naught_uncertainty/length_naught)**2))
r = graph(fig_name,delta_temperatures,fractional_length_change,"Change in Temperature (C)",r"Fractional Change in Length", total_y_uncertainty)
slope = r['slope']
book_slope = 2.3*10**-5
pd = percent_difference(slope, book_slope)
print(pd)

fig_name = "Thermal Expansion of a Copper Rod"
temperatures = np.array([81, 76, 69, 66, 61, 56, 51, 46, 41, 36, 31, 27]) #C
temperature_uncertainty = 0.5 #C
base_temperature = temperatures[-1]
length_naught = 52/100 #m
length_naught_uncertainty = 0.05/100 #m
lengths = np.array([7.09, 7.08, 6.79, 6.70, 6.69, 6.79, 6.74, 6.64, 6.47, 6.32, 6.23, 6.14])/1000 #m
base_length = lengths[-1] #mm
length_uncertainty = 0.11/1000
delta_temperatures = temperatures - base_temperature
delta_temperature_uncertainty = temperature_uncertainty
delta_lengths = lengths - base_length
fractional_length_change = delta_lengths/length_naught
total_y_uncertainty = np.mean(fractional_length_change*np.mean((delta_temperature_uncertainty/delta_temperatures[:-1])**2 + (length_uncertainty/delta_lengths[:-1])**2 + (length_naught_uncertainty/length_naught)**2))
r = graph(fig_name,delta_temperatures,fractional_length_change,"Change in Temperature (C)",r"Fractional Change in Length", total_y_uncertainty)
slope = r['slope']
book_slope = 2.3*10**-5
pd = percent_difference(slope, book_slope)
print(pd)
