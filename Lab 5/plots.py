import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

fig_name = "Elastic collisions with m1 == m2"
plt.figure(fig_name)
m1 = 199.5 #g
m2 = 199.5 #g
v1 = np.array([0.817, 0.595, 0.283, 0.252, 0.317])
v2_prime = np.array([0.614, 0.311, 0.193, 0.172, 0.208])
expected_slope = 2*m1/(m1+m2)

x = v1
y = v2_prime
plt.scatter(x,y, c='r', s=5)

best_fit = np.poly1d(np.polyfit(x, y, 1))
actual_slope = best_fit.c[0]
best_fit_s = str(best_fit)

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)

plt.legend()
plt.title(fig_name)
plt.xlabel('v1 (m/s)')
plt.ylabel('v2_prime (m/s)')

print(f'''
{fig_name}
The ideal slope is {expected_slope}
The actual slope is {actual_slope}
The percent difference is {(actual_slope-expected_slope)/expected_slope*100}%
    ''')
plt.savefig(f"{''.join(fig_name.split())}.png")


fig_name = "Elastic collisions with m1 != m2"
plt.figure(fig_name)
m1 = 199.5/1000 #kg
m2 = 249.5/1000 #kg
v1 = np.array([0.425, 0.297, 0.267, 0.361, 0.323])
v1_prime = np.array([0.07, 0.052, 0.074, 0.054, 0.056])
v2_prime = np.array([0.333, 0.232, 0.202, 0.267, 0.245])
expected_slope = 2*m1/(m1+m2)

x = v1
y = v2_prime
plt.scatter(x,y, c='r', s=5)

best_fit = np.poly1d(np.polyfit(x, y, 1))
actual_slope = best_fit.c[0]
best_fit_s = str(best_fit)

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)

plt.legend()
plt.title(fig_name)
plt.xlabel('v1 (m/s)')
plt.ylabel('v2_prime (m/s)')

kinetic_energy = 0.5*m1*v1**2
kinetic_energy_prime = 0.5*m1*v1_prime**2 + 0.5*m2*v2_prime**2
n = (kinetic_energy - kinetic_energy_prime)/kinetic_energy
n_bar = sum(n)/len(n)
print(f'''
{fig_name}
The ideal slope is {expected_slope}
The actual slope is {actual_slope}
The percent difference is {(actual_slope-expected_slope)/expected_slope*100}%
kinetic_energy = {kinetic_energy}
kinetic_energy_prime = {kinetic_energy_prime}
n = {n}
n_bar = {n_bar}
    ''')
plt.savefig(f"{''.join(fig_name.split())}.png")






fig_name = "Inelastic collisions with m1 == m2"
plt.figure(fig_name)
m1 = 199.5 #g
m2 = 199.5 #g
v1 = np.array([0.801, 0.487, 0.313, 0.21, 0.706])
v1_prime = np.array([0.337, 0.214, 0.148, 0.139, 0.31])
expected_slope = m1/(m1+m2)

x = v1
y = v1_prime
plt.scatter(x,y, c='r', s=5)

best_fit = np.poly1d(np.polyfit(x, y, 1))
actual_slope = best_fit.c[0]
best_fit_s = str(best_fit)

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)

plt.legend()
plt.title(fig_name)
plt.xlabel('v1 (m/s)')
plt.ylabel('v2_prime (m/s)')

print(f'''
{fig_name}
The ideal slope is {expected_slope}
The actual slope is {actual_slope}
The percent difference is {(actual_slope-expected_slope)/expected_slope*100}%
    ''')
plt.savefig(f"{''.join(fig_name.split())}.png")


fig_name = "Inelastic collisions with m1 != m2"
plt.figure(fig_name)
m1 = 199.5/1000 #kg
m2 = 249.5/1000 #kg
v1 = np.array([0.46, 0.809, 0.236, 0.215, 0.221])
v1_prime = np.array([0.227, 0.396, 0.125, 0.1, 0.146])
expected_slope = m1/(m1+m2)

x = v1
y = v1_prime
plt.scatter(x,y, c='r', s=5)

best_fit = np.poly1d(np.polyfit(x, y, 1))
actual_slope = best_fit.c[0]
best_fit_s = str(best_fit)

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)

plt.legend()
plt.title(fig_name)
plt.xlabel('v1 (m/s)')
plt.ylabel('v2_prime (m/s)')

kinetic_energy = 0.5*m1*v1**2
kinetic_energy_prime = 0.5*(m1+m2)*v1_prime**2
n = (kinetic_energy - kinetic_energy_prime)/kinetic_energy
n_bar = sum(n)/len(n)
print(f'''
{fig_name}
The ideal slope is {expected_slope}
The actual slope is {actual_slope}
The percent difference is {(actual_slope-expected_slope)/expected_slope*100}%
kinetic_energy = {kinetic_energy}
kinetic_energy_prime = {kinetic_energy_prime}
n = {n}
n_bar = {n_bar}
    ''')
plt.savefig(f"{''.join(fig_name.split())}.png")