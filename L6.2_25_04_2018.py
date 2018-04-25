import numpy

#make a dictionary containing cube from 1-10
numbers= numpy.arange(0,11,1)

cubes = {}

for x in numbers:
    y = x**3
    cubes[x]=y
    print ("The cube of "+ str(x) +" is "+ str(y))
      # making a z dictionary
      # print (cubes)

print (cubes)

#for x in cubes.keys():                #want to list it nicely
    #print (x, cubes())


