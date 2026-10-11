import numpy as np
import matplotlib.pyplot as plt

# Time
t = np.linspace(0, 2*np.pi, 500)

# Three signals - same frequency, different phase
s0 = np.sin(t + 0)
s90 = np.sin(t + np.pi/2)
s180 = np.sin(t + np.pi)

# Plot
plt.figure(figsize=(8,4))
plt.plot(t, s0, label='Phase 0°')
plt.plot(t, s90, label='Phase 90°')
plt.plot(t, s180, label='Phase 180°')
plt.title('Day 5: Phase Shift')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('day5.png', dpi=150)
plt.show()
