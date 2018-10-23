import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#Varying the radius
plt.figure("Varying Radius")
r = np.array([0.15, 0.17, 0.18, 0.14, 0.16])
t = np.array([1.597, 1.14, 1.101, 2.36, 1.43])
t_squared = t**2
goal_slope = 0.2418/(4*np.pi**2*0.1365) #Fc/(4pi^2M)T^2
x,y = t_squared,r
plt.scatter(x,y, c='r', s=5)

best_fit = np.poly1d(np.polyfit(x, y, 1))
actual_slope = best_fit.c[0]
best_fit_s = str(best_fit)

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)
plt.legend()

plt.title('Varying Radius')
plt.xlabel('Period Squared (s^2)')
plt.ylabel('Radius (m)')

print(f'''
Varying Radius
The ideal slope is {goal_slope}
The actual slope is {actual_slope}
The percent difference is {(actual_slope-goal_slope)/goal_slope*100}%
    ''')
plt.savefig('VaryingRadius.png')

#Varying the force
plt.figure("Varying Force")
f = np.array([0.5396, 1.0301, 0.7358, 1.2263, 0.4415])
t = np.array([1.335, 1, 1.163, 0.948, 1.386])
inverse_t_squared = 1/(t**2)
goal_slope = 4*np.pi**2*0.1365*0.16 #4pi^2Mr * 1/T^2

x,y = inverse_t_squared,f
plt.scatter(x,y, c='r', s=5)

best_fit = np.poly1d(np.polyfit(x, y, 1))
actual_slope = best_fit.c[0]
best_fit_s = str(best_fit)

plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'k--', label=best_fit_s)
plt.legend()

plt.title('Varying Force')
plt.xlabel('Inverse Period Squared (1/s^2)')
plt.ylabel('Force (N)')

print(f'''
Varying Force
The ideal slope is {goal_slope}
The actual slope is {actual_slope}
The percent difference is {(actual_slope-goal_slope)/goal_slope*100}%
    ''')
plt.savefig('VaryingForce.png')



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


plt.ion()
plt.show()
plt.pause(10)