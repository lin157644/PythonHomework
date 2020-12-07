import pylab

def f(t):
    return (1.2732*pylab.sin(2*t) + 0.4244*pylab.sin(6*t) + 0.25465*pylab.sin(10*t) + 0.18189*pylab.sin(14*t) + 0.14147*pylab.sin(18*t))
#def df(t):
#    return (2*1.2732*pylab.cos(2*t) + 6*0.4244*pylab.cos(6*t) + 10*0.25465*pylab.cos(10*t) + 14*0.18189*pylab.cos(14*t) + 18*0.14147*pylab.cos(18*t))


#Setting the range of function
a, b, n = -pylab.pi, pylab.pi, 1000

h = (b-a)/(n-1)

def df2(t, h):
    return (f(t+h)-f(t))/h

xs = pylab.linspace(a, b, n)

ys = f(xs)
#ys1 = df(xs)
ys2 = df2(xs, h)

pylab.figure(figsize=(9,5), facecolor='w')

#fig = pylab.gcf()
#fig.set_size_inches(10, 10)

pylab.plot(xs, ys,'blue',lw=2, label='h(t)')
#pylab.plot(xs, ys1, 'green', lw=1, label='h\'(t)')
pylab.plot(xs, ys2, 'green', lw=1, label='h\'(t)')

pylab.grid()

pylab.xlabel("t", fontweight='bold', size='xx-large')
pylab.ylabel("S", fontweight='bold', size='xx-large')

pylab.title("sawtooth function approximation and derivative")

#pylab.xlim(0, 35)
#pylab.ylim(0, 1)

pylab.legend(loc=4)

pylab.axis((-3.5, 3.5, -14, 14))

#Delete this next line when uploading the homework
pylab.savefig('Output/homework.png')

pylab.show()