 Day 20 / 30 | AM Modulation

What I did today:
I was trying to understand how AM radio actually works. The idea is, you have a slow signal (your voice) and a fast signal (carrier). AM just makes the carrier loud or quiet based on your voice.

What the code does:
1. Creates a slow message = 5Hz
2. Creates a fast carrier = 50Hz  
3. Mixes them using AM formula: `(1 + m _ message) _ carrier`
4. Plots everything so you can see it

How to run it:
- I used Pydroid 3 on my phone
- Just install matplotlib and numpy: `pip install matplotlib numpy`
- Copy the code and run, you will see 3 graphs
- The third graph is the important one. The black dashed line is your message.

What I learned:
If modulation index `m` is more than 1, the signal scatters. Keep it below 1. Real radio uses same idea but carrier is like 1MHz.

Day 20 done. Next is FM.

