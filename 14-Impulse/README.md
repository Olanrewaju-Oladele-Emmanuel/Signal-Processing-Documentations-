DAY 14:  IMPULSE RESPONSE & LTI SYSTEMS

Today I learned about LTI.

LTI means Linear Time Invariant. Most circuits are LTI systems.

Main idea surrounding impulse response & LTI systems
If I give a system an impulse (delta), the output is called h.
h is the impulse response. If you know h, you know the whole system.

What I did:
x = 5Hz sine wave (my usual test signal)
h = exp(-t/tau) - this is how an RC low-pass behaves
y = x * h - convolution

What I observed:
y is smoother than x. The system filtered it a little.
In my plot, after 0.5s it decays to zero because of the convolution edge with mode='same'.

So:
delta -> h
any x -> x * h

That is why Day 11 (convolution) and Day 14 are connected.

Plot: day14_impulse.png
Code: day14_impulse.py
Run on Pydroid 3 - no laptop
