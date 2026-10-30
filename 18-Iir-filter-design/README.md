Day 18:  IIR Filter Design

WHAT I DID TODAY:
Today, I did IIR low pass filter. Reason is yesterday I did FIR so today I need to do IIR to compare both types of filters. This is Phase 4 practical filters.

THEORY I USED
IIR means Infinite Impulse Response. Reason it is called infinite is because it uses feedback of past output, so its impulse response never really becomes zero, it keeps ringing.

FIR equation is y = b0_x + b1_x[n-1]. Reason it has no feedback is it only uses input, so it is always stable.[n]

IIR equation is y = b_x +... - a_y[n-1] - a_y[n-2]. Reason for minus a_y term is because we feed back past output. That feedback makes it more efficient.[n]

WHY I CHOSE 15HZ CUTOFF
Reason is my signal has 5Hz clean and 50Hz noise. So cutoff must be between them. If I choose 15Hz, 5Hz will pass because 5 is less than 15, and 50 will be blocked because 50 is greater than 15. If I choose 30Hz, 50Hz will still be close and not well blocked.

1st order IIR
Formula y = alpha_x + (1-alpha)_y[n-1]. Reason alpha is calculated as 1 - exp(-2_pi_fc/fs) is because this maps analog cutoff to digital. Alpha decides how much new input to take. If alpha is high, more new input passes.[n]

2nd order IIR
Coefficients b0 0.067 b1 0.134 b2 0.067 a1 -1.143 a2 0.412. Reason I used 2nd order is because 1st order slope is only -20dB per decade, not sharp. 2nd order gives -40dB per decade, so 50Hz will be cut more. Reason I got coefficients from online calculator is because designing Butterworth by hand needs bilinear transform which is long.

CODE STEPS
I created t from 0 to 2 seconds. Reason 2 seconds is enough to see filtering.
Created noisy signal clean 5Hz plus 0.8 times 50Hz. Reason 0.8 amplitude for noise is to make noise visible but not overpower clean.
Applied for loop for IIR. Reason I used loop is because y needs y[n-1] which you cannot vectorize easily.
Did FFT before and after. Reason is to prove in frequency domain that 50Hz peak is gone.[n]

RESULT
2nd order filtered better than 1st order. Reason is 2nd order has two poles, so sharper roll off. First order still left small 50Hz ripple.

OBSERVATION
IIR needs only 5 coefficients vs FIR needs 20 taps for same cutoff. Reason IIR is efficient is because feedback reuses energy. But IIR can become unstable if a1 a2 wrong. Reason is poles can go outside unit circle and output grows to infinity. FIR has no poles, only zeros, so always stable.

PROBLEM I FACED
Pydroid lagged in for loop. Reason is Python loop is slow on phone. Had to run twice.

Next is Day 19 High pass and Band pass filters.

Tools used: Pydroid 3, numpy matplotlib
