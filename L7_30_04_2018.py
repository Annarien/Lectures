class Complex():
    def __init__(self,r=0.0,i=0.0):
        self.r=r
        self.i=i

    def abs(self):
        return numpy.sqrt(self.r*self.r+self.i*self.i)

    def __add__(self,x):
        ans=self.copy()
        if isinstance (val,Complex):
            ans.r=ans.r+val.r
            ans.i=ansi+val.i
        else:
            ans.r=ans.r+val
        return ans


        
        
import numpy

#a.abs()
a=Complex(3,4)
a.abs()

a=Complex(3,5)
a.r
a.i


print (a.r)
print (a.i)

#overloading
a=numpy.random.randn(5)
b=numpy.random.randn(5)
c=a+b
print (c)

d=Complex(2,3)
e=Complex(2,4)

f=d+e
print (f)