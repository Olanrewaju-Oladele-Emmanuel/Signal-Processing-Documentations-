import numpy as np
import matplotlib.pyplot as plt

f = 5
T = 1/f
t = np.linspace(0,1,1000)

y1 = np.sin(2*np.pi*f*t)
y2 = np.sin(2*np.pi*f*t)
y3 = np.sin(2*np.pi*f*t + np.pi)

# adding
y_add = y1 + y2
y_sub = y1 + y3

print(f, T, max(y_add), max(y_sub))

plt.subplot(2,1,1)
plt.plot(t, y1, label='y1')
plt.plot(t, y2, '--', label='y2')
plt.plot(t, y_add, 'g', label='sum')
plt.title('Constructive')
plt.legend()
plt.grid()

plt.subplot(2,1,2)
plt.plot(t, y1, label='y1')
plt.plot(t, y3, '--', label='y3')
plt.plot(t, y_sub, 'g', label='sum=0')
plt.title('Destructive pi shift')
plt.legend()
plt.grid()

plt.savefig('day06.png')
plt.show()
