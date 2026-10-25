DAY 17: FIR FILTER DESIGN

Part of my 30 days signal processing challenge.

WHAT I DID

Tried to design a low pass FIR filter using window method.

fs = 200 Hz
fc = 20 Hz cutoff
N = 51 taps
Window = Hamming

HOW IT WORKS

Ideal low pass filter impulse response is sinc function
h = sin(2*pi*fc*(n-M)/fs) / (pi*(n-M))
At center I used 2*fc/fs to avoid divide by zero

Then apply Hamming window to reduce ripple
w[n] = 0.54 - 0.46*cos(2*pi*n/(N-1))

Multiply and normalize

Test with signal: 5Hz + 50Hz noise
The filter should keep 5Hz and remove 50Hz

FILES

day17_fir_filter_design.py - main code
day17_fir_filter_design.png - output plot

OUTPUT

Top plot is frequency response - shows low pass.
Bottom plot is input vs filtered output - 50Hz noise is reduced.

WHAT I LEARNED

Why we need window - ideal sinc is infinite and has ripple
Hamming window smooths the cutoff
Manual convolution helped me understand filtering

TOOLS: Python, numpy, matplotlib, Pydroid 3

DATE: Oct 18, 2025
