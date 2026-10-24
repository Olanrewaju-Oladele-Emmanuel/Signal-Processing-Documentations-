import numpy as np
import matplotlib.pyplot as plt

fm = 5
t = np.linspace(0, 1, 1000)
x = np.sin(2*np.pi*fm*t)

# in this case fs = 100 good
fs1 = 100
t1 = np.arange(0, 1, 1/fs1)
x1 = np.sin(2*np.pi*fm*t1)

# here fs = 8 bad, it will look like 3Hz
fs2 = 8
t2 = np.arange(0, 1, 1/fs2)
x2 = np.sin(2*np.pi*fm*t2)

#  like the first, fs = 6 worse, it will look like 1Hz
fs3 = 6
t3 = np.arange(0, 1, 1/fs3)
x3 = np.sin(2*np.pi*fm*t3)

plt.figure(figsize=(7,8))

plt.subplot(3,1,1)
plt.plot(t, x)
plt.stem(t1, x1)
plt.title("fs=100Hz - sees true 5Hz")

plt.subplot(3,1,2)
plt.plot(t, x)
plt.stem(t2, x2)
plt.plot(t, np.sin(2*np.pi*3*t), 'r--')
plt.title("fs=8Hz - 5Hz looks like 3Hz alias")

plt.subplot(3,1,3)
plt.plot(t, x)
plt.stem(t3, x3)
plt.plot(t, np.sin(2*np.pi*1*t), 'r--')
plt.title("fs=6Hz - 5Hz looks like 1Hz alias")
plt.xlabel("Time")

plt.tight_layout()
plt.savefig("Day_16_Aliasing.png")
plt.show()
