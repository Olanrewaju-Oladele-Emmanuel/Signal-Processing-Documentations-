import numpy as np
import matplotlib.pyplot as plt

fm = 5  # my signal is 5Hz
t = np.linspace(0, 1, 1000)  # fine time for plotting true signal
x_true = np.sin(2 * np.pi * fm * t)

# sampling test
# Nyquist = 2*fm = 10Hz

fs1 = 100  # good sampling
t1 = np.arange(0, 1, 1/fs1)
x1 = np.sin(2 * np.pi * fm * t1)

fs2 = 12  # just above Nyquist
t2 = np.arange(0, 1, 1/fs2)
x2 = np.sin(2 * np.pi * fm * t2)

fs3 = 8  # below Nyquist - bad
t3 = np.arange(0, 1, 1/fs3)
x3 = np.sin(2 * np.pi * fm * t3)

# plot
plt.figure(figsize=(7,8))

plt.subplot(3,1,1)
plt.plot(t, x_true, color='gray')
plt.stem(t1, x1)
plt.title('fs=100Hz, good sampling')
plt.ylabel('Amp')
plt.grid(True)

plt.subplot(3,1,2)
plt.plot(t, x_true, color='gray')
plt.stem(t2, x2)
plt.title('fs=12Hz, at edge')
plt.ylabel('Amp')
plt.grid(True)

plt.subplot(3,1,3)
plt.plot(t, x_true, color='gray', label='true 5Hz')



plt.plot(t, np.sin(2*np.pi*3*t), 'r--', label='alias 3Hz')
plt.stem(t3, x3)
plt.title('fs=8Hz, aliasing happens')
plt.xlabel('Time [s]')
plt.ylabel('Amp')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('Day_15_Sampling_Theorem.png', dpi=200)
plt.show()

print("Nyquist rate is 10Hz")
print("fs=100 good, fs=12 ok, fs=8 bad")
