import numpy
import time
from matplotlib import pyplot as plt

#time taken by computer to do a fft
n = 2**16
x = numpy.random.randn(n)                                          #random n
t1 = time.time();y = numpy.fft.fft(x)                              #t1 is start time
t2 = time.time()                                                   #t2 is end time
print("The time taken to do a fft of "+str(n)+" is " + str(t2-t1)) #time taken for a fft 