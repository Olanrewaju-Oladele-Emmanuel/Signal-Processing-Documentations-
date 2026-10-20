Day 12 - I FINALLY SAW FREQUENCY MOVE WITH TIME

For 11 days, my Fourier Transform could tell me WHAT frequencies are in my signal.
But it could never tell me WHEN they happened.

Today that changed.

 WHAT I DID

I made a simple trick signal to test myself:
First second: I played a 5Hz wave
Second second: I switched to 20Hz

In time domain, you can see it — slow waves, then fast waves.
But if I do normal FFT (Day 08), it just says "you have 5Hz and 20Hz" — no timing.

So I built STFT.

WHAT IS STFT IN PLAIN WORDS?

Take your signal. Cut it into small pieces. Like slicing bread.
I used Hamming window from Day 10 for each slice, so edges don't leak.
Then do small FFT for each slice.
Stack them together.

What you get is a spectrogram — time goes left to right, frequency goes bottom to top.

In my plot below, you can see it clearly: yellow bright line at 5Hz for 0-1s, then it jumps to 20Hz for 1-2s. That jump is the whole point.

 WHY DO I CARE?

This is how Shazam knows your music, how speech recognition knows when you said "hello", how doctors read EEG.

It's not theory anymore — it's how real systems see non-stationary signals.

I coded it manually on Pydroid 3 with just NumPy. No fancy library. Window size 32, hop 8.

WHAT I LEARNED TODAY

Small window = you know exactly WHEN, but you blur frequency.
Big window = you know exact frequency, but you lose WHEN.

You can't have both perfect. That's the trade-off.

Day 10 Windowing was not just theory. Today I finally used it.

Tomorrow: Day 13 - Correlation. Let's see how to find if two signals look alike.

- OLANREWAJU OLADELE Emmanuel
