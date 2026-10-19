Day 11:  Convolution

Today I learned how filtering actually works behind the scenes.

For the past 10 days I have been working with sine waves, Fourier, IFFT filter, and windowing. Today I connected it all.

What I did:
I took a simple sine wave (like Day 01) and passed it through an exponential decay filter. That filter is the impulse response h(t). The output is the convolution of both.

Formula: y(t) = x(t) * h(t)

Why it matters for my field:
As an Electrical/Electronics graduate, this is exactly what happens in a circuit. Input signal enters a system, the system has its own response, and what comes out is the convolution. Before today I knew filters removed frequencies, today I saw the time-domain maths that does it.

What you will see in the plot:
1. Top - My input sine wave (windowed to 1 second)
2. Middle - The filter's impulse response
3. Bottom - The output after convolution. The shape changed, that is the filter working.

Tools: Python, numpy.convolve, matplotlib. All done on Colab mobile.

Challenge: Getting the time axes to align after convolution. The output is longer than the input, which makes sense because the filter has memory.

Next is Day 12 - STFT, which will use the windowing I learned in Day 10.

- Olanrewaju Oladele Emmanuel 
