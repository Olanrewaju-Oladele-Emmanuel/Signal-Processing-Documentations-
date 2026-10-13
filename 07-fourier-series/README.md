# Day 07 - Fourier Series

What I did: Built square wave by adding sine waves.

Formula: f(t) = 4/pi * [sin(2*pi*f*t)/1 + sin(2*pi*3f*t)/3 + sin(2*pi*5f*t)/5 + ...]

Parameters: f=1Hz, T=1s, Harmonics = 1,3,5,7,9

Observation: With 1 harmonic it's sine, with 5 it looks like square but has Gibbs ripples at edges. Proves Fourier theory - complex signals = sum of simple sines.

Tools: Python, Pydroid 3, Matplotlib on Android.

Code file: Fourier_series.py
Plot file: day07_fourier_series.png
