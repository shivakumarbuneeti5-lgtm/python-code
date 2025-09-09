# random approch 1

import math
a=int(input("enter a list number:"))
x=int(input("enter a list number:"))
y=int(input("enter a list number:"))
print("square root :", math.sqrt(a))
print("factorial :", math.sqrt(a))
print("exponent :", math.sqrt(a))
print("greatest common :", math.sqrt(a))

# module 2

import math as m, random as r
x=int(input("enter 1st name:"))
y=int(input("enter 2nd name:"))
print("GCD of",x,"and",y,"is:",m.gcd(x,y))
print("Rand num b/w 100,200 is:",r.randint(100,200))
print("rand num b/w 10,100 is:",r.randrange(10,100,10))
print("random num b/w 0,1 is:",r.random())

#  approch 3
from math import sqrt,factorial
from random import randint
n=int(input("enter n for square root:"))
print("random number is:",randint(100,200))
n=int(input("enter n for factorial:"))
print("factorial is:",factorial(n))

# approch 4
from math import sqrt as sq
from random import randint as ri,random as rd
n=int(input("enter n for square root:"))
print("square root is",sq(n))
print("random number 100-500 is:",ri(100,500))
print("random number 0-1 is: ",rd())

# approch 5

from math import*
from random import*
n=int(input("enter n for square root:"))
print("square root is:",sqrt(n))
print("random number 100-500 is:",randrange(100,500))
print("random number 0-1is:",random())

 