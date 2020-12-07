import pylab

def f(x):
    return (pylab.cos(x)**2)/pylab.sqrt(pylab.maximum(1,2*x-1))


#Setting the range of function
a, b, n = 0, 10*pylab.pi, 1000

xs = pylab.linspace(a, b, n)

pylab.figure(figsize=(15,8))

#fig = pylab.gcf()
#fig.set_size_inches(10, 10)

pylab.plot(xs, f(xs), 'blue')

pylab.grid()

pylab.xlabel("X")
pylab.ylabel("Y")
pylab.title("f(x) = cos(x)^2 / sqrt( max(1,2x-1) )")

#pylab.xlim(0, 35)
#pylab.ylim(0, 1)

pylab.axis((0, 35, 0, 1))

#Delete this next line when uploading the homework
pylab.savefig('Output/homework.png')

pylab.show()