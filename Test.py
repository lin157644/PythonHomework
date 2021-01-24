from pylab import *

def f(t):
    return 0.08+0.12*(1-exp(-0.02*t))

xs = linspace(0, 100, 500)

plot(xs, f(xs))

show()