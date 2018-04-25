import numpy
from matplotlib import pyplot as plt

x = numpy.arange (-5,0.1,5)
y = mygauss(x)

plt.ion()
plt.plot(x,y)

plt.clf();plt.plot(x)
x=numpy.arange(-5,5,0.01)
plt.clf();plt.plot(x)

y=mygauss(x)
#quad.quad(mygauss,-25,25)

numpy.sqrt(2*numpy.pi)
a=numpy.sqrt(2*numpy.pi)*0.1
b=quad.quad(mygauss,-25,25)

print (a)
print(b)

##########Check coding!
