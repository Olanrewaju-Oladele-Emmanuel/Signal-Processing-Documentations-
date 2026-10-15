Day 08 - Fourier Transform

What I did: Converted time-domain signal to frequency-domain using FFT.

Signal used: sin(5Hz) + 0.5*sin(15Hz) + 0.3*sin(50Hz noise)
Sampling: fs=500Hz, T=1s

Key Learning:
- Time domain shows WHEN signal happens.
- Frequency domain shows WHAT frequencies make it.
- FFT reveals hidden frequencies our eyes cannot see in time plot.
- Peaks at 5Hz, 15Hz, 50Hz match my formula.

Tool: np.fft.fft(), np.fft.fftfreq()

Observation: This is why FFT is used in audio, radio, vibration analysis - to find hidden components.

Code: fourier_transform.py
Plot: day08_fourier_transform.png
