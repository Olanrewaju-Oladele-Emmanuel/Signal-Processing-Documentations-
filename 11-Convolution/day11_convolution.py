import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 500)
input_signal = np.sin(2 * np.pi * 3 * t) * (t < 1)  # Your sine wave
h = np.exp(-5 * t) * (t < 0.8)  # Impulse response (RC filter)

conv_result = np.convolve(input_signal, h, mode='full')
t_conv = np.linspace(0, 4, len(conv_result))

plt.figure(figsize=(8,6))
plt.subplot(3,1,1)
plt.plot(t, input_signal); plt.title('Input - Sine Wave'); plt.grid(True)
plt.subplot(3,1,2)
plt.plot(t, h, color='orange'); plt.title('Impulse Response h(t)'); plt.grid(True)
plt.subplot(3,1,3)
plt.plot(t_conv, conv_result, color='green'); plt.title('Output y(t)=x*h'); plt.grid(True)
plt.tight_layout()
plt.savefig('day11_convolution.png', dpi=300)
plt.show()
