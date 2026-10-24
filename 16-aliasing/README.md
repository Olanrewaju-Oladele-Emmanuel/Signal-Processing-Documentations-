Day 16 Aliasing Effect

WHAT I WANTED TO DO
To see what happens when we sample a signal with fs less than 2 times fm. This is aliasing.

KEY CONCEPT 
We have fm = 5Hz sine wave.
Nyquist says fs must be greater than 2 times fm, so fs must be greater than 10Hz to get correct signal.
If fs is less than 10Hz, the 5Hz signal will appear as low frequency alias.

Formula for alias I used: f alias = |fs - fm| for this simple case where fs is close to fm

My code: day16_aliasing.py
First I made original signal: fm=5, t from 0 to 1 with 1000 points, x = sin(2 pi fm t)
Then sampled with 3 different fs:

1. fs1 = 100Hz
   t1 = arange(0,1,1/fs1), x1 = sin(2 pi fm t1)
   This is good sampling, 100 is greater than 10, so no alias.

2. fs2 = 8Hz
   t2 = arange(0,1,1/8), x2 = sin(2 pi fm t2)
   This is bad, 8 is less than 10, so alias. Expected alias = |8-5| = 3Hz. I plotted red dashed 3Hz to compare.

3. fs3 = 6Hz
   t3 = arange(0,1,1/6), x3 = sin(2 pi fm t3)
   This is worse, 6 is less than 10, alias = |6-5| = 1Hz. I plotted red dashed 1Hz.

Then I plotted 3 subplots one below the other.
Blue line is original 5Hz wave
Stem is sampled points
Red dashed is alias frequency that we think we see

What I saw in the plot: Day_16_Aliasing.png

Top plot fs=100Hz: stem points sit exactly on blue wave. We see true 5Hz. No alias. This is correct sampling.

Middle plot fs=8Hz: stem points dont follow blue wave. They follow red dashed 3Hz wave. So if someone only sees sampled points, he will think signal is 3Hz not 5Hz. This is alias.

Bottom plot fs=6Hz: same thing, stem points follow red dashed 1Hz wave. So 5Hz looks like 1Hz. Very wrong. This is worse aliasing.

CONCLUSION / WHAT I LEARNT
When fs is less than Nyquist rate, we get wrong frequency. The signal folds. So for 5Hz we must use fs at least 10Hz, practically more like 20Hz. If we sample slow, we lose original info and get fake low freq.

This is why in real ADC we always use anti-aliasing filter before sampling.

Files
day16_aliasing.py
Day_16_Aliasing.png

Done in Pydroid 3 with numpy and matplotlib.
