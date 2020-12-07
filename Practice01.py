import pylab

def f(x):
    return pylab.maximum(pylab.absolute(x*pylab.sin(x)), pylab.absolute(x*pylab.cos(x)))

def g(x):
    return pylab.minimum(pylab.absolute(x*pylab.sin(x)), pylab.absolute(x*pylab.cos(x)))

#Setting the range of function
a, b, n = -2*pylab.pi, 2*pylab.pi, 1000

xs = pylab.linspace(a, b, n)

pylab.plot(xs, f(xs), 'blue')
pylab.plot(xs, g(xs), 'green')

pylab.grid()

pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x)=max( abs(x sin(x)),abs(x cos(x)) ),g(x)=min( abs(x sin(x)), abs(x cos(x)) )")

pylab.savefig('homework.png')

pylab.show()