Day 15 - Sampling Theorem (The Nyquist Rule)

This one finally made sampling click for me.

I have been using a 5Hz sine wave as my test signal. According to theory, I need to sample at more than twice that frequency to keep the shape. So Nyquist rate = 2 * 5Hz = 10Hz.

I tested three different sampling rates in Pydroid 3:

1. fs = 100Hz - Clean.
Way above 10Hz. I got a lot of points and the plot matches the real 5Hz sine perfectly.

2. fs = 12Hz - At the edge.
Just 2Hz above Nyquist. Only 12 points in one second, so it looks sparse, but you can still tell it is 5Hz. It works, but you are walking on a thin line.

3. fs = 8Hz - This is where it breaks.
8Hz is less than 10Hz, so it violates Nyquist. The samples I got don't look like 5Hz anymore. They line up and pretend to be a 3Hz wave. That fake wave is aliasing. Once this happens, you can never get the real 5Hz back.

What I learned:
If you sample too slow, you are not saving data, you are creating a lie. High frequency will disguise itself as low frequency.

That is why we have 44.1kHz for audio. Human ear hears up to about 20kHz, so we need more than 40kHz to be safe.

All done on my phone with Pydroid 3. No laptop.

Code: Day15_Sampling_Theorem.py
Plot: Day_15_Sampling_Theorem.png

Next is Day 16 - Aliasing in detail.
