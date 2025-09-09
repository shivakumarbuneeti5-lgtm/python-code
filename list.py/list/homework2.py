# Python Operators Example

a = 10
b = 3
x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Arithmetic Operators 
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

# Relational / Comparison Operators 
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# Logical Operators
print("(a > 5 and b < 5):", (a > 5 and b < 5))
print("(a > 5 or b > 10):", (a > 5 or b > 10))
print("not(a > 5):", not(a > 5))

# Assignment Operators 
c = a
print("c =", c)
c += 5
print("c += 5 →", c)
c -= 2
print("c -= 2 →", c)
c *= 2
print("c *= 2 →", c)
c /= 3
print("c /= 3 →", c)
c //= 2
print("c //= 2 →", c)
c %= 3
print("c %= 3 →", c)
c **= 2
print("c **= 2 →", c)

# Bitwise Operators
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)

# Identity Operators 
print("x is y:", x is y)      # False (different objects)
print("x is z:", x is z)      # True (same object)
print("x is not y:", x is not y)

# Membership Operators 
print("2 in x:", 2 in x)
print("5 not in x:", 5 not in x)

# Python List – All Operations in One Code

#Creating Lists
list1 = [10, 20, 30, 40, 50]
list2 = ["apple", "banana", "cherry"]
list3 = [1, 2.5, "hello", True]

print("list1 =", list1)
print("list2 =", list2)
print("list3 =", list3)

#Accessing Elements 
print("First element of list1:", list1[0])
print("Last element of list1:", list1[-1])

#Slicing 
print("list1[1:4] =", list1[1:4])
print("list1[:3] =", list1[:3])
print("list1[2:] =", list1[2:])

# Updating Elements 
list1[1] = 200
print("After updating index 1:", list1)

#List methods
list1.append(60)         # Add at end
print("append(60):", list1)
list1.insert(2, 25)      # Insert at position
print("insert(2,25):", list1)
list1.extend([70, 80])   # Extend with another list
print("extend([70,80]):", list1)
list1.remove(200)        # Remove specific value
print("remove(200):", list1)
popped = list1.pop()     # Pop last element
print("pop():", list1, " | Popped:", popped)
del list1[0]             # Delete by index
print("del list1[0]:", list1)
list1.clear()            # Clear all elements
print("clear():", list1)

#Re-creating list1 for further operations 
list1 = [10, 20, 30, 40, 50, 20, 30]

# List Functions 
print("Length:", len(list1))
print("Max:", max(list1))
print("Min:", min(list1))
print("Sum:", sum(list1))
print("Count of 20:", list1.count(20))
print("Index of 30:", list1.index(30))
list1.sort()
print("Ascending sort:", list1)
list1.sort(reverse=True)
print("Descending sort:", list1)

# Copying 
list_copy = list1.copy()
print("Copy of list1:", list_copy)

# Looping through List 
for item in list2:
    print("Item:", item)

#List Comprehension 
squares = [x*x for x in range(6)]
print("Squares:", squares)

# Nested Lists 
nested = [[1, 2], [3, 4], [5, 6]]
print("nested =", nested)
print("Access nested[1][0]:", nested[1][0])

# Python Tuple – All Operations in One Code

# Creating Tuples 
t1 = (10, 20, 30, 40, 50)
t2 = ("apple", "banana", "cherry")
t3 = (1, 2.5, "hello", True)
t4 = (5,)  # single element tuple (note the comma)

print("t1 =", t1)
print("t2 =", t2)
print("t3 =", t3)
print("t4 =", t4)

# Accessing Elements
print("First element of t1:", t1[0])
print("Last element of t1:", t1[-1])

#Slicing
print("t1[1:4] =", t1[1:4])
print("t1[:3] =", t1[:3])
print("t1[2:] =", t1[2:])

# Creating a Tuple 
t = (10, 20, 30, 20, 40, 20)
print("Tuple:", t)

# Tuple Methods
print("Count of 20:", t.count(20))   # count() method
print("Index of 30:", t.index(30))   # index() method


#Tuple Immutability 
try:
    t[0] = 99  # This will raise an error
except TypeError as e:
    print("Error (Tuples are immutable):", e)

#Tuple Packing & Unpacking 
packed = (100, 200, 300)
a, b, c = packed
print("Packed tuple:", packed)
print("Unpacked values → a:", a, "b:", b, "c:", c)


# Tuple Functions 
t5 = (10, 20, 30, 40, 20, 30)
print("t5 =", t5)
print("Length:", len(t5))
print("Max:", max(t5))
print("Min:", min(t5))
print("Sum:", sum(t5))
print("Count of 20:", t5.count(20))
print("Index of 30:", t5.index(30))

# Nesting 
nested = ((1, 2), (3, 4), (5, 6))
print("nested =", nested)
print("Access nested[1][0]:", nested[1][0])

# Tuple Packing & Unpacking 
packed = (100, 200, 300)
a, b, c = packed
print("Packed tuple:", packed)
print("Unpacked values → a:", a, "b:", b, "c:", c)

# Looping through Tuple 
for item in t2:
    print("Item:", item)

# Python Dictionary – All Operations in One Code

# Creating Dictionaries 
dict1 = {"name": "Alice", "age": 20, "city": "Hyderabad"}
dict2 = dict(id=101, branch="ECE")
print("dict1 =", dict1)
print("dict2 =", dict2)

# Accessing Elements 
print("Name:", dict1["name"])             # Access by key
print("Age (using get):", dict1.get("age"))

# Updating & Adding Elements 
dict1["age"] = 21              # Update value
dict1["college"] = "ABC Univ"  # Add new key-value
print("Updated dict1:", dict1)

# Removing Elements 
dict1.pop("city")           # Remove by key
print("After pop('city'):", dict1)
dict1.popitem()             # Remove last inserted item
print("After popitem():", dict1)
del dict1["age"]            # Delete specific key
print("After del age:", dict1)
dict1.clear()               # Clear dictionary
print("After clear():", dict1)

#Re-creating dict1 for further operations 
dict1 = {"name": "Alice", "age": 20, "city": "Hyderabad", "age": 20}

# Dictionary Methods 
print("Keys:", dict1.keys())       # keys()
print("Values:", dict1.values())   # values()
print("Items:", dict1.items())     # items()
print("Get with default:", dict1.get("gender", "Not Found"))
print("Count of keys:", len(dict1))  # len()

#Copy & Update 
dict_copy = dict1.copy()          # copy()
print("Copy of dict1:", dict_copy)
dict2.update({"section": "A"})    # update()
print("Updated dict2:", dict2)

# Looping through Dictionary 
for k in dict1:
    print("Key:", k, "| Value:", dict1[k])

for k, v in dict1.items():
    print("Key:", k, "→ Value:", v)

# Dictionary Comprehension 
squares = {x: x*x for x in range(1, 6)}
print("Squares dict:", squares)

#Nested Dictionary 
students = {
    1: {"name": "Alice", "age": 20},
    2: {"name": "Bob", "age": 21},
}
print("students =", students)
print("Access students[1]['name']:", students[1]["name"])

# Creating Sets 
set1 = {10, 20, 30, 40, 50}
set2 = set(["apple", "banana", "cherry"])
set3 = set()   # Empty set (use set(), not {})
print("set1 =", set1)
print("set2 =", set2)
print("set3 =", set3)

#Built-in Functions
nums = {5, 10, 15, 20}
print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Sorted:", sorted(nums))   # returns list

#Built-in Methods

# Sample sets
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

print("set1 =", set1)
print("set2 =", set2)

# Adding Elements 
set1.add(50)       # add()
print("After add(50):", set1)
set1.update([60, 70])  # update()
print("After update([60,70]):", set1)

#Removing Elements 
set1.remove(20)    # remove() – error if not found
print("After remove(20):", set1)
set1.discard(100)  # discard() – no error if not found
print("After discard(100):", set1)
popped = set1.pop()  # pop() – removes random element
print("After pop():", set1, "| Popped:", popped)
set_copy = set1.copy()   # copy()
print("Copy of set1:", set_copy)
set1.clear()       # clear()
print("After clear():", set1)

#Set Operations
print("Union:", set_copy.union(set2))                   # union()
print("Intersection:", set_copy.intersection(set2))     # intersection()
print("Difference:", set_copy.difference(set2))         # difference()
print("Symmetric Difference:", set_copy.symmetric_difference(set2))  # symmetric_difference()

# Update Variants 
a = {1, 2, 3}
b = {3, 4, 5}
a.update(b)   # union update
print("update:", a)

a = {1, 2, 3}
a.intersection_update({2, 3, 4})
print("intersection_update:", a)

a = {1, 2, 3, 4}
a.difference_update({2, 3})
print("difference_update:", a)

a = {1, 2, 3}
a.symmetric_difference_update({3, 4, 5})
print("symmetric_difference_update:", a)

# Relation Methods 
s1 = {1, 2}
s2 = {1, 2, 3, 4}
print("s1 is subset of s2:", s1.issubset(s2))     # issubset()
print("s2 is superset of s1:", s2.issuperset(s1)) # issuperset()
print("s1 is disjoint with {5,6}:", s1.isdisjoint({5, 6})) # isdisjoint()

# Python Conditional Statements

x = 15
y = 20

#Simple if 
if x < y:
    print("x is less than y")

# if-else 
if x % 2 == 0:
    print("x is Even")
else:
    print("x is Odd")

# if-elif-else
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")

# Nested if 
num = 18
if num >= 0:
    if num % 2 == 0:
        print("num is Positive and Even")
    else:
        print("num is Positive and Odd")
else:
    print("num is Negative")

# Shorthand if (single line) 
a = 5
b = 10
if a < b: print("a is smaller (shorthand if)")

# Shorthand if-else (ternary operator) 
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)

# Nested Ternary Example 
n = -5
result = "Positive" if n > 0 else "Zero" if n == 0 else "Negative"
print("Number is:", result)

# Python While Loops – All in One Code

#While loops
# Basic While Loop 
i = 1
while i <= 5:
    print("i =", i)
    i += 1

# While Loop with Condition 
x = 10
while x > 0:
    print("x =", x)
    x -= 2

# Infinite While Loop (with break) 
y = 1
while True:
    print("y =", y)
    if y == 3:
        print("Breaking loop at y =", y)
        break
    y += 1

# While Loop with Continue 
z = 0
while z < 5:
    z += 1
    if z == 3:
        print("Skipping", z)
        continue
    print("z =", z)

# While Loop with Pass 
a = 0
while a < 3:
    if a == 1:
        pass  # placeholder, does nothing
    print("a =", a)
    a += 1

# While Loop with Else 
b = 1
while b <= 3:
    print("b =", b)
    b += 1
else:
    print("Loop ended normally (no break used)")

# Nested While Loops 
m = 1
while m <= 2:
    n = 1
    while n <= 3:
        print(f"m={m}, n={n}")
        n += 1
    m += 1

#for loops

# Basic For Loop with range() 
for i in range(5):   # 0 to 4
    print("i =", i)

# For Loop with Custom Range 
for i in range(2, 11, 2):  # start=2, stop=10, step=2
    print("Even number:", i)

# For Loop with List 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# For Loop with Tuple 
tup = (1, 2, 3, 4)
for item in tup:
    print("Tuple item:", item)

# For Loop with String 
for ch in "Python":
    print("Char:", ch)

# For Loop with Dictionary 
student = {"name": "Navadeep", "age": 18, "branch": "ECE"}
for key in student:
    print("Key:", key, "| Value:", student[key])

#For Loop with Set 
colors = {"red", "green", "blue"}
for c in colors:
    print("Color:", c)

# Nested For Loops 
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

# For Loop with Break 
for num in range(1, 10):
    if num == 5:
        print("Breaking at", num)
        break
    print(num)

# For Loop with Continue 
for num in range(1, 6):
    if num == 3:
        print("Skipping 3")
        continue
    print(num)

#For Loop with Pass 
for num in range(1, 4):
    if num == 2:
        pass  # does nothing, just placeholder
    print("Number:", num)

# For Loop with Else 
for i in range(3):
    print("i =", i)
else:
    print("Loop finished successfully (no break)")

# For Loop with Enumerate() 
items = ["pen", "book", "bag"]
for index, value in enumerate(items):
    print(f"Index={index}, Value={value}")

#For Loop with Zip() 
names = ["Ram", "Sam", "Ravi"]
marks = [85, 90, 78]
for n, m in zip(names, marks):
    print(f"Name={n}, Marks={m}")

# For Loop with List Comprehension 
squares = [x*x for x in range(1, 6)]
print("Squares:", squares)

# Break statement

# Break in For Loop 
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

#Break in While Loop 
n = 1
while n <= 10:
    if n == 6:
        print("Breaking the loop at n =", n)
        break
    print("n =", n)
    n += 1





#return statements    

#  Simple return
def add(a, b):
    return a + b

result = add(10, 20)
print("Addition =", result)


# Return multiple values
def calculate(a, b):
    return a + b, a - b, a * b

sum_, diff, prod = calculate(5, 3)
print("Sum:", sum_)
print("Difference:", diff)
print("Product:", prod)


#  Return inside conditional
def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("7 is", check_even(7))
print("10 is", check_even(10))


#  Function without return (returns None)
def greet(name):
    print("Hello,", name)

output = greet("shiva")
print("Return value:", output)   # None




#pass statements
#  Using pass in a loop
for i in range(5):
    if i == 3:
        pass  # does nothing
    print("i =", i)


#  Using pass in a function
def my_function():
    pass   # function is empty for now

print("Function defined but does nothing")


# Using pass in a class
class MyClass:
    pass   # class body left empty

obj = MyClass()
print("Object created from empty class")


# Using pass in if statement
x = 10
if x > 5:
    pass  # we will write logic later
else:
    print("x is small")



#continue statements
#continue in for loop
print("For Loop Example:")
for i in range(6):
    if i == 3:
        continue   # skip 3
    print(i)

#continue in while loop
print("\nWhile Loop Example:")
x = 0
while x < 6:
    x += 1
    if x == 4:
        continue   # skip 4
    print(x)

#continue inside nested loop
print("\nNested Loop Example:")
for i in range(1, 4):       # outer loop
    for j in range(1, 4):   # inner loop
        if j == 2:
            continue   # skip inner loop when j=2
        print(f"(i={i}, j={j})")







#assret statements
# 1. Basic assert
x = 5
assert x > 0
print("✅ Basic assert passed: x is positive")

# 2. Assert with custom error message
y = 10
assert y < 20, "y must be less than 20"
print("✅ Assert with message passed: y is less than 20")

# 3. Assert in function
def divide(a, b):
    assert b != 0, "❌ Denominator cannot be zero"
    return a / b

print("✅ Function assert:", divide(10, 2))

# 4. Assert inside loop
numbers = [2, 4, 6, 8, 10]

for n in numbers:
    assert n % 2 == 0, f"❌ Odd number found: {n}"
    print(f"✅ Number {n} is even")

    # 1. Simple function
def greet():
    print("Hello! Welcome to Python functions.")
greet()


# 2. Function with parameters
def add(a, b):
    print("Sum =", a + b)
add(5, 3)


# 3. Function with return value
def square(x):
    return x * x
print("Square of 4 =", square(4))


# 4. Function with default arguments
def intro(name, course="B.Tech"):
    print(f"My name is {name} and I study {course}")
intro("shiva")
intro("shiva", "ECE")


# 5. Function with keyword arguments
def profile(name, age):
    print(f"Name: {name}, Age: {age}")
profile(age=18, name="shiva")


# 6. Function with variable length arguments (*args)
def total_sum(*numbers):
    print("Total =", sum(numbers))
total_sum(10, 20, 30, 40)


# 7. Function with keyword variable length arguments (**kwargs)
def student_details(**info):
    for key, value in info.items():
        print(f"{key} → {value}")
student_details(name="shiva", age=18, branch="ECE")


# 8. Recursive function
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    else:                  # recursive case
        return n * factorial(n - 1)
print("Factorial of 5 =", factorial(5))


# 9. Lambda function (anonymous function)
cube = lambda x: x ** 3
print("Cube of 3 =", cube(3))



#Approches in functions

#approach-1 
#example 1
def arthemetic_operations(a,b):
    c=a**b
    d=a+b
    e=a-b
    f=a/b
    g=a*b
    print("Exponential of Two Values is =",c)
    print("sum of Two Values is =",d)
    print("Difference of Two Values is =",e)
    print("division of Two Values is =",f)
    print("Product of Two Values is =",g)
    

x=int(input("Enter 1st value:"))    
y=int(input("Enter 2nd value:"))
arthemetic_operations(x,y)  

#example 2:
def arthemetic_operations(a,b):
    c=a**b
    d=a+b
    e=a-b
    f=a/b
    g=a*b
    print("Exponential of Two Values is =",c)
    print("sum of Two Values is =",d)
    print("Difference of Two Values is =",e)
    print("division of Two Values is =",f)
    print("Product of Two Values is =",g)

arthemetic_operations(10,5)



#approach-2 
# example 1

def arthemetic_opertor():
    a=int(input("enter the value:"))
    b=int(input("enter the value:"))
    c=a+b
    d=a-b
    e=a*b
    g=a%b
    h=a//b
    i=a**b
    if b==0:
        print("Division by zero not allowed")
    else:
        f=a/b
    print("sum of ({},{}) is= {}".format(a,b,c))
    print("sub of ({},{}) is= {}".format(a,b,d))
    print("mul of ({},{}) is= {}".format(a,b,e))
    print("div of ({},{}) is= {}".format(a,b,f))
    print("mod of ({},{}) is= {}".format(a,b,g))
    print("floor div of ({},{}) is= {}".format(a,b,h))
     #print("expo of ({},{}) is= {}".format(a,b,i)) #traditional way    
    print("expo of ",a,"and",b,"is=:",i)#unique way
arthemetic_opertor() 

#ex2
def arthemetic_opertor():
    a=6
    b=19
    c=a+b
    d=a-b
    e=a*b
    g=a%b
    h=a//b
    i=a**b
    if b==0:
        print("Division by zero not allowed")
    else:
        f=a/b
    print("sum of ({},{}) is= {}".format(a,b,c))
    print("sub of ({},{}) is= {}".format(a,b,d))
    print("mul of ({},{}) is= {}".format(a,b,e))
    print("div of ({},{}) is= {}".format(a,b,f))
    print("mod of ({},{}) is= {}".format(a,b,g))
    print("floor div of ({},{}) is= {}".format(a,b,h))   
    print("expo of ",a,"and",b,"is=:",i)
arthemetic_opertor()  


#approach-3 
# example 1

def arthemetic_op():
    a=float(input("Enter first number:"))
    b=float(input("Enter second number:"))
    c=a+b
    d=a-b
    e=a*b
    if b==0:
          print("Division by zero not allowed")     
    else:
        f=a/b
    g=a%b
    return("Sum of ({},{}) is= {}\n"
           "sub of ({},{}) is= {}\n"
            "mul of ({},{}) is= {}\n"
            "div of ({},{}) is= {}\n"
            "mod of ({},{}) is= {}\n"
            ).format(a,b,c,a,b,d,a,b,e,a,b,f,a,b,g)

    
print(arthemetic_op())


#approach4
def arthemetic_op(a,b):
    c=a+b
    d=a-b
    e=a*b
    g=a%b   
    if b==0:
          print("Division by zero not allowed")
    else:
         f=a/b
    print("sum of({},{})is={}".format(a,b,c))
    print("sub of({},{})is={}".format(a,b,d))
    print("mul of({},{})is={}".format(a,b,e))
    print("div of({},{})is={}".format(a,b,f))
    print("mod of({},{})is={}".format(a,b,g))
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
arthemetic_op(a,b)        


#problems using functions
def num_here(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
n = int(input("Enter a number:"))
print(num_here(n))

#factorial example.py
n=int(input("Enter the number for factorial:"))
t=n
fact=1
while n>0:
    fact=fact*n  
    n=n-1
    print("Factorial:",fact)
print("done")
#factorial
'''def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number:"))
print("Factorial of {} is {}".format(num,factorial(num)))'''
#factorial using loop
def factorial_loop(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact 
num=int(input("Enter the number:"))
print("Factorial of {} is {}".format(num,factorial_loop(num)))

#positional parametre.py
#example 1
def studentData(stno,studept,stuname,stage,stmarks):
    print("{}\t{}\t{}\t{}\t{}\t".format(stno,studept,stuname,stage,stmarks))
print("_"*50)    
print("student Details")
print("_"*50)
print("stno\tstudept\tstuname\tstage\tstmarks")
print("_"*50)
studentData(10,"ECE","Madhu",26,95)
print("_"*50)
def studentData(stno,studept,stuname,stage,stmarks):
    print("{}\t{}\t{}\t{}\t{}\t".format(stno,studept,stuname,stage,stmarks))
print("_"*50)    
print("student Details")
print("_"*50)
print("stno\tstudept\tstuname\tstage\tstmarks")
print("_"*50)
studentData(10,"ECE","shiva",26,95)
print("_"*50)
def studentData(stno,studept,stuname,stage,stmarks):
    print("{}\t{}\t{}\t{}\t{}\t".format(stno,studept,stuname,stage,stmarks))
print("_"*50)    
print("student Details")
print("_"*50)
print("stno\tstudept\tstuname\tstage\tstmarks")
print("_"*50)
studentData(10,"ECE","PREMKUMAR",26,95)
print("_"*50)
def studentData(stno,studept,stuname,stage,stmarks):
    print("{}\t{}\t{}\t{}\t{}\t".format(stno,studept,stuname,stage,stmarks))
print("_"*50)    
print("student Details")
print("_"*50)
print("stno\tstudept\tstuname\tstage\tstmarks")
print("_"*50)
studentData(10,"ECE","PRAVEEN",26,95)
print("_"*50)
def studentData(stno,studept,stuname,stage,stmarks):
    print("{}\t{}\t{}\t{}\t{}\t".format(stno,studept,stuname,stage,stmarks))
print("_"*50)    
print("student Details")
print("_"*50)
print("stno\tstudept\tstuname\tstage\tstmarks")
print("_"*50)
studentData(10,"ECE","ADITYA",26,95)
print("_"*50)


#default parametre:-
def dispstudent(stno,sname,marks,course="python",dept="IT"):
    print("{}\t{}\t{}\t{}\t{}".format(stno,sname,marks,course,dept))
print("_"*60)    
print("student information:")
print("_"*60)   
print("stno\tName\tMarks\tcourse\tDepartment") 
print("_"*60)    
dispstudent(10,"Nava",34.56) 
dispstudent(20,"Mani",3.56,) 
dispstudent(30,"rana",3.6,"java") 
dispstudent(40,"Para",3.6,"c") 
dispstudent(50,"Mara",3.4,"Ds","cse") 
print("_"*60)


#kwd_arguments:-
#example 1
def employeeinfo(empno,name,sal,dsgn):
    print("{}\t{}\t{}\t{}\t".format(empno,name,sal,dsgn))
print("_"*60)
print("employee information:")   
print("_"*60)
print("empo\tName\tsal\tdsgn") 
print("_"*60)   
employeeinfo(10,"ND",5.9,"SE")
employeeinfo(10,dsgn="JP",sal=5.8,name="SE")
employeeinfo(20,dsgn="JD",sal=6.9,name="MD")
employeeinfo(dsgn="SD",empno=30,sal=10.2,name="PK")

#example 2
def servantsinfo(svno,svname,svsal,svskill):
    print("{}\t{}\t{}\t{}\t".format(svno,svname,svsal,svskill))
print("_"*60) 
print("employ information:")
print("_"*60) 
print("number\tName\tsal\tskill") 
print("_"*60) 
servantsinfo() 



#variable length parametre:-    
#vlp
def ck(*names):
    for i in names:
        print("Hello,{}".format(i))
ck("Hyderabad","Secunderabad","peddapalli","Maisammaguda")
ck("chennai")
ck("Village","Town","City") 


#keyboard variable lenght argument:-
def empinfo(**info):
    for k,v in info.items():
        print("{}:{}".format(k,v))
empinfo(empno=10,ename="ND",esal=5.9,edsgn="SE")
empinfo(empno=20,ename="PK",esal=6.9,edsgn="JD",ecity="Hyd")
empinfo(empno=30,ename="MD",esal=10.2,edsgn="MD",ecity="Hyd",estate="TG")
empinfo(empno=40,ename="JP",esal=15.9,edsgn="SD",ecity="Hyd",estate="TG",ecountry="India")
empinfo(empno=50,ename="AD",esal=25.9,edsgn="AD",ecity="Hyd",estate="TG",ecountry="India",ecompany="TCS")
empinfo()

# Global variable
x = 50

def demo():
    # Local variable
    y = 10
    print("Inside function: x =", x)   # access global
    print("Inside function: y =", y)   # local variable

demo()

print("Outside function: x =", x)  # global accessible here
# print("Outside function: y =", y)  # ❌ error: y is local


# Example of modifying global variable inside function
count = 0   # global variable

def update_count():
    global count   # declare we want to use global variable
    count += 1
    print("Inside function: count =", count)

update_count()
update_count()

print("Outside function: count =", count)  # reflects updates

#lambda functions in operations
a=int(input("enter a:"))
b=int(input("enter b:"))
sum = lambda a, b : a + b #sum in lamda function
print("Sum is:", sum(a,b))
product = lambda a, b : a * b #product in lamda function
print("product is:",product(a,b))
difference= lambda a,b : a-b #difference in lamda function
print("difference is:",difference(a,b)) 
division= lambda a,b : a/b #division in lamda function
print("division is:",division(a,b))
modulus= lambda a,b : a%b #modulus in lamda function
print("modulus is:",modulus(a,b))


#even odd in lambda function
c=int(input("enter c:"))
evenodd = lambda a : "even" if a%2==0 else "odd"
print(c,"is",evenodd(c))


#factorial in lambda function
d=int(input("enter d:"))
fact = lambda n: 1 if n==0 or n==1 else n * fact(n-1)
print("Factorial is:",fact(d))

#difference between lambda and normal function:-
#normal function
def tempconvert(c):
    f=(1.8)*c + 32
    return f
print("Temperature in Fahrenheit is:", tempconvert(37))


#Lamda Functions:-
tempconvert = lambda c: (1.8)*c + 32
print("Temperature in Fahrenheit is:", tempconvert(37))

# -------------------------
# mymath.py (module 1)
# -------------------------
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# -------------------------
# myutils.py (module 2)
# -------------------------
def greet(name):
    return f"Hello, {name}!"

def is_even(num):
    return num % 2 == 0


# -------------------------
# main.py (main program)
# -------------------------
# Normally these would be in separate files, but shown together here

import types

# Create fake modules for this single-file demo
mymath = types.ModuleType("mymath")
setattr(mymath, "add", add)
setattr(mymath, "subtract", subtract)

myutils = types.ModuleType("myutils")
setattr(myutils, "greet", greet)
setattr(myutils, "is_even", is_even)

# ----- Using the modules -----
print("Addition:", mymath.add(10, 5))
print("Subtraction:", mymath.subtract(10, 5))

print(myutils.greet("shiva"))
print("Is 8 even?", myutils.is_even(8))
print("Is 7 even?", myutils.is_even(7))



#pre defines modules
# 1. math module
import math
print("📌 Math Module:")
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))
print("Value of pi:", math.pi)
print("-" * 40)

# 2. random module
import random
print("📌 Random Module:")
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice:", random.choice(["apple", "banana", "cherry"]))
print("-" * 40)

# 3. datetime module
import datetime
print("📌 Datetime Module:")
now = datetime.datetime.now()
print("Current date & time:", now)
print("Today:", now.date())
print("Year:", now.year, "Month:", now.month, "Day:", now.day)
print("-" * 40)

# 4. os module
import os
print("📌 OS Module:")
print("Current working directory:", os.getcwd())
print("Files in current folder:", os.listdir())
print("-" * 40)

# 5. sys module
import sys
print("📌 Sys Module:")
print("Python version:", sys.version)
print("System path (first 2):", sys.path[:2])  # only first 2 paths for short output
print("-" * 40)

#6. statistics module
import statistics
print("📌 Statistics Module:")
data = [10, 20, 30, 40, 50, 50]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))
print("-" * 40)

# 7. platform module
import platform
print("📌 Platform Module:")
print("System:", platform.system())
print("Release:", platform.release())
print("Processor:", platform.processor())
print("-" * 40)

#user defines modules
# --------------------------
# Create a user-defined module (simulated here)
# Normally this would be saved as mymodule.py
# --------------------------
def greet(name):
    return f"Hello, {name}! Welcome to Modules."

def add(a, b):
    return a + b

pi = 3.14159


# --------------------------
# Different ways of importing
# --------------------------

print("📌 Way 1: import module")
import types
mymodule = types.ModuleType("mymodule")
mymodule.greet = greet
mymodule.add = add
mymodule.pi = pi

print(mymodule.greet("shiva"))
print("Addition:", mymodule.add(10, 5))
print("Pi:", mymodule.pi)
print("-" * 40)


print("📌 Way 2: from module import function")
# Direct access without module name
from _main_ import greet, add
print(greet("Student"))
print("Addition:", add(7, 3))
print("-" * 40)


print("📌 Way 3: import module as alias")
import _main_ as mm
print(mm.greet("Alias Example"))
print("Addition:", mm.add(2, 8))
print("Pi:", mm.pi)
print("-" * 40)


print("📌 Way 4: from module import *")
from _main_ import *
print(greet("Wildcard Import"))
print("Addition:", add(4, 6))
print("Pi:", pi)
print("-" * 40)

#math module
import math
n=int(input())
a=int(input())
b=int(input())
print("power of n is:",pow(n,2))
print("square root of n is:",math.sqrt(n))
print("Factorial of n is:",math.factorial(n))
print("gcd of a,b is:",math.gcd(a,b))
print("exponential of a,b is :",math.exp(n))
print("fabs of n is :",math.fabs(n))

#random math module
import math,random
x=int(input())
y=int(input())
s=int(input())
print("gcd of",x,"and",y,"is:",math.gcd(x,y))
print("random no between",x,"and",y,"is:",random.randint(x,y))
print("random range:",random.randrange(x,y,s))

#math range module
import math as m,random as r
x=int(input("enter the value 1:"))
y=int(input("enter the value 2:"))
s=int(input())
print("gcd of",x,"and",y,"is:",m.gcd(x,y))
print("random no between",x,"and",y,"is:",r.randint(x,y))
print("random range:",r.randrange(x,y,s))

#module 2
from math import sqrt,factorial
from random import randint
from random import randrange
x=int(input())
y=int(input())
s=int(input())
print("square root  of",x,"is:",sqrt(x))
print("random no between",x,"and",y,"is:",randint(x,y))
print("random range:",randrange(x,y,s))

#module 3
from math import sqrt as sq,factorial as ft
from random import randint as ri,randrange as rd
x=int(input())
y=int(input())
s=int(input())
print("square root  of",x,"is:",sq(x))
print("random no between",x,"and",y,"is:",ri(x,y))
print("random range:",rd(x,y,s))
print("factorial of x is",ft(x))

#module 4
from math import*
from random import*
x=int(input())
y=int(input())
s=int(input())
print("square root  of",x,"is:",sqrt(x))
print("random no between",x,"and",y,"is:",randint(x,y))
print("random range:",randrange(x,y,s))
print("factorial of x is",factorial(x))

#package
#By using the sys.path.append
#project structure
'''project/
│
├── main.py
└── external/
    └── mypackage/
        ├── _init_.py
        ├── mathops.py
        └── stringops.py'''

#mathops.py
def add(a, b):
    return a + b

def mul(a, b):
    return a * b
#stringops.py
def greet(name):
    return f"Hello, {name}!"

def reverse(text):
    return text[::-1]
#main.py
import sys
import os

# Step 1: Append external folder to sys.path
sys.path.append(os.path.abspath("external"))

# Step 2: Import the package from external folder
import mypackage

# Step 3: Use package functions
print("Addition:", mypackage.add(10, 5))
print("Multiplication:", mypackage.mul(4, 6))
print("Greeting:", mypackage.greet("shiva"))
print("Reverse:", mypackage.reverse("Python Modules"))

#By using the PYTHONPATH environmental variable:-

#square pattern
n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()  
#increasing triangle
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print() 
#decresing triangle
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()   
# triangle1
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")    
    print()  
#  trangle2:
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n):
        print(" ",end=" ") 
    print()
#triangle3
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")    
    print()   
#triangle4
n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    print()   
#180" triangle
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")  
    print() 
#reverse 180" triangle
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")  
    print()
#diamond  
n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")  
    print()           
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")  
    for i in range(i,n):
        print("*",end=" ")
    print() 
#butterfly:-