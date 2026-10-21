Day 13 - Correlation

Today I played with correlation.

So idea is simple:
If I have a signal and I shift it, can I still find how much I shifted it?

I made:
x = 5hz sine wave
y = same x but I rolled it by 10 samples

Then:
1. Autocorrelation - I did x vs x
It peaked at 0. Means it matches itself at zero lag. And it keeps repeating every small time because sine is periodic.

2. Cross-correlation - x vs y
I wanted to see where the peak is. It showed 10 samples. So it actually found the delay I added. That was nice.

What I learned:
- auto correlation helps to know if signal is periodic
- cross correlation helps to find delay between two signals

I used np.correlate with mode='full'. Had to create lag array with np.arange(-len(x)+1, len(x)).

Plot is in day13_correlation.png

Code: day13_correlation.py
