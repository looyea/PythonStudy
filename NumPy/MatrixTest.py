# _*_ coding:utf-8 _*_
import numpy
from numpy import matrix


m1 = matrix([1,2])
m2 = matrix([3,4])

print(m1 + m2)
print(m1 * m2.T)

print(numpy.multiply(m1 * m2))

print (m1.mean())
print (m2.sort())
print (m2.argsort())
