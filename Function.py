import pylab

def f(x):
    return pylab.maximum(pylab.absolute(x*pylab.sin(x)), pylab.absolute(x*pylab.cos(x)))

def g(x):
    return pylab.minimum(pylab.absolute(x*pylab.sin(x)), pylab.absolute(x*pylab.cos(x)))

'''def f(x):
    return pylab.sin(x) + pylab.cos(2*x)

def g(x):
    return x**3 - 2*x + pylab.cos(x/3)

def h(x):
    return pylab.sin(exp(x))

def s(x):
    return pylab.log(x) + 2*pylab.log10(x)

def t(x):
    return pylab.sin(pylab.sqrt(abs(5*x)))

def u(x):
    return pylab.maximum(pylab.sin(x), pylab.cos(x)**2)

def v(x):
    return pylab.minimum(pylab.sin(x), pylab.cos(2*x))'''

#Setting the range of function
a, b, n = -2*pylab.pi, 2*pylab.pi, 1000

#在 [a,b] 間產生 n 個點存到 xs
xs = pylab.linspace(a, b, n)

#畫圖
pylab.plot(xs, f(xs), 'blue')
pylab.plot(xs, g(xs), 'green')

pylab.grid()

pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x)=max( abs(x sin(x)),abs(x cos(x)) ),g(x)=min( abs(x sin(x)), abs(x cos(x)) )")

pylab.savefig('Output/homework.png')

pylab.show()