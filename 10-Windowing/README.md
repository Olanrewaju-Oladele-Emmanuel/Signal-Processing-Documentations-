Day 10 of 30: I Finally Understood Why My FFT Was Lying To Me

For 9 days I have been doing FFT and wondering why my clean 5Hz signal was showing as messy frequencies everywhere.

Today I got the answer: WINDOWING.

The Real Problem

Imagine you are recording someone singing, and you suddenly cut the recording in the middle of a word. That sudden cut creates a pop sound, right?

That is exactly what we do to signals. We take 1 second of data and cut it sharply. That sharp cut creates fake frequencies that were never in the original signal. We call it spectral leakage.

What Windowing Does

Windowing is just a polite way of cutting. Instead of cutting sharply like using scissors, you fade the signal in and fade it out gently like fading music.

Without window: Signal ends abruptly, FFT shows blurry, scattered frequencies
With window: Signal fades smoothly, FFT shows one clean, sharp peak

I Tested 4 Windows Today

1. Rectangular - No fading. Worst. Never use it.
2. Hanning - Gentle fade. Good for most work.
3. Hamming - Slightly better than Hanning when two frequencies are close.
4. Blackman - Heavy fading. Cleanest spectrum, but makes the peak a bit wider.

The Lesson That Hit Me

There is no perfect window. It is a trade off. If you want less leakage, you must accept a slightly wider peak. You choose what matters more for your project.

This is the kind of small detail that separates student work from professional DSP work.

Plot: plots/day10_windowing.png
Code: code/day10_windowing.py

On to Day 11.
