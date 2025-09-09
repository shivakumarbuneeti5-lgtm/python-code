
print("Hello, World!")
# int data type
a=50
print(a)
print(type(a))
#float data type
x=54.65
print(type(x))
#string data type
name="python"
country="india"
print(name,country)
print(type(name),type(country))
#bool data type
a=True
b=False
print(a,b)
print(type(a),type(b))
#complex data type
a=3+6j
b=-4j
c=complex(7,9)
print(a,b,c)
print(type(a),type(b),type(c))
#input()function
#syntax 1:
x=input()
print(x)
type(x)
#syntax 2:
y=input("enter value")
print(y,type(y))
s="python"
len(s)
my_list=[40,75,99,44]
len(my_list)
my_tuple=(35,66,39,21,43)
len(my_tuple)
a=40
b=40
c=80
id(a)
id(b)
id(c)
i=[34,76]
id(i)
a=50
b=60
c=a+b
s="345"
int(s)
f=35.75
int(f)
b=True
int(b)
c=3+2j
int(c)
#any data type to float data type
a=34
float(a)
b=False
float(b)
c="367.55"
float(c)
367.55
d=2+7j
float(d)
#any data type to str data type
a=345
str(a)
b=867.4
str(b)
c=True
str(c)
d=3+5j
str(d)
#any data type to bool data type
a=59
bool(a)
s="flase"
bool(s)
f=35.45
bool(f)
c=5-6j
bool(c)
# any data type to complex data type
a=359
complex(a)
b=60.78
complex(b)
c=True
complex(b)
c=True
complex(c)
s="34+6j"
complex(s)

a = 10
b = 3
print(a + b) 
print(a - b) 
print(a * b)
print(a / b) 
print(a // b) 
print(a % b) 
print(a ** b)
x = 5
y = 10
print(x == y) 
print(x != y) 
print(x < y) 
print(x > y) 
print(x <= y)
print(x >= y)


age = 25
print(age == 25) 
print(age != 30) 
print(age > 18) 
print(age <= 21) 
# Chaining Comparisons (A powerful Python feature)
x = 10
print(5 < x < 15)



has_license = True
has_car = False
age = 22
# Can legally drive if they are over 18 AND have a license
can_drive = age > 18 and has_license
print(can_drive) 
# Can get a ride if they have a car OR a friend has a car
has_friend_with_car = True
can_get_ride = has_car or has_friend_with_car
print(can_get_ride) 
# Is not eligible for a student discount if they are NOT under 26
is_student = not(age >= 26)
print(is_student)


x = 10 
y = 4 
print(x & y) 
print(x | y) 
print(x ^ y) 
print(~x) 
print(x << 1) 
print(x >> 1)

#<<left shit operator
a=64
b=a<<5
b
x = 5
result = x << 2
print(f"Binary of {x}: {bin(x)}") 
print(f"After << 2: {bin(result)}") 
print(f"Decimal result: {result}")

print(3 << 3)

x = 20
result = x >> 2
print(f"Binary of {x}: {bin(x)}") 
print(f"After >> 2: {bin(result)}") 
print(f"Decimal result: {result}")

print(29 >> 2)
#^XOR operator
a=553
b=344
c=a^b
c
#bitwise & operator
a=353
b=863
c=a&b
c
#bitwise | opretor
x=934
y=212
z=x|y
z
# bitwise~not operator
x=54
y=~x
y
#in,not in operators
my_list=[44,65,"we",75.34,32]
44 in my_list
44 not in my_list
99 in my_list
99 not in my_list

my_list = [1, 2, 3, 4, 5]
my_string = "Hello World"
print(3 in my_list) 
print(10 not in my_list) 
print("Hello" in my_string) 
print("z" not in my_string) 

# is , is not operators
x=[ 1,2,3]
y=[1,2,3,]
x is y
x is not y
a=34
b=34
a is not b

[1, 2, 3]
b = [1, 2, 3] 
c = a 
print(a == b) 
print(a is b) 
print(a is c) 
# Special Case with Small Integers and Strings:
# Python optimizes memory for small integers and common strings,
# so they might point to the same object.
x = 256
y = 256
print(x is y)
x = 257
y = 257
print(x is y) 
# The safe bet is to use is only for None, True, False.
print(x is None)
# ternary operator program
# voter card eligibility check
age=int(input("enter your age:"))
message="you are elible"
if age>= 18:
  status="Adult"
else:
  status="not_eligible"
  
# printing the result

print(message)


# Traditional if-else

age=20
if age >= 18:
 status = "Adult"
else:
 status = "Minor"
# Using Ternary Operator
status = "Adult" if age >= 18 else "Minor"
print(status) 
# Another example
is_raining = True
activity = "Stay inside" if is_raining else "Go for a walk"
print(activity) 

I=[20,40,60,70,122]
I[3]=666
I
I[-1]=666
I


# Empty_List:

l=[]
print(l)
print(type(l))
lst=list()
print(lst)
print(type(lst))

# Non_Empty_List:

l=[20,54,64,"Welcome",3+4j,False]
print(l)
type(l)
l1=[22,33,44]
l2=[77,88,99]
l3=[l1+l2]
l3
l4=l3+[300,400,900]
l4
l=[200,300,400,500,700,900]
l
200 in l
250 in l
200 in l
250 not in l
l=[30,50,60,55,76]
print([-1])
l[5]
l(-3)
l=[20,30,40,50,60,70,80,90,100,120]
l
l[2:7]
l[2:10:3]
l[-3:-8]
l[-3:-8:-3]
l=[20,30,40,50,60,70,80,90,110,120]
l[:6]
l[:4]
l[::4]
l[:-4]
l[::-3]
l[:10:4]
l[:-6:-2]
l=[20,40,60,70,80,90]
len(l)
max(l)
min(l)
sum(l)
sorted(l)
sorted(l,reverse=True)
sorted(l,reverse=False)
list(reversed(l))

# List comparision
l1=[20,60]
l2=[20,60]
l3=[60,20]
l4=[70,90]
l1==l2
l1==l3
l1==l4
l1.sort()==l3.sort()

# List object from range,tuple,set

l=list(range(30,90,12))
l
l1=list((50,80,55))
l1
s={70,54,33}
l2=list(s)
l2

# list elements accessing
# for loop

l=[20,64,4,"Do",2+3j]
for i in l:
    print(i)

t=()
type(t)
print(t)
tp=tuple()
type(tp)
print(tp)
t=(30,50.68,87)
type(t)
t

# Tuple from list, set and range():

t1=tuple(range(5,50,20))
t1
t2=tuple([40,50,90])
t2
s=(40,33,54)
t3=tuple(s)
s
t3
t=(20,50,70,10)
type(t)
print(t[3])
print(t[-5])
t[4]
t[-1]
t=(20,30,40,50,60,70,80,90,110,120)
type(t)
t
t[2:7]
t[2:10:3]
t[-3:-8:-3]
t=(20,30,40,50,60,70,80,90,100,110,120)
t[:6]
t[4:]
t[::4]
t[::-3]
t[-4::-3]
t[::]

# tuples merging

t1=(22,33,44)
t2=(99,88,77,33)
t3=t1+t2
t3
t4=t3+(101,102,103)
t4

# Elements serching in tuple object

t=(200,300,800,900)
200 in t
200 not in t
99 in t
99 not in t
 #Tuples Comparasions

t1=(20,60)
t2=(60,20)
t3=(90,40)
t4=(20,60)
t1==t4
t1==t2
sorted(t1)==sorted(t2)
t1 is t2