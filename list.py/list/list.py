#if example.py
age_=input("give the age:") 
if age_>="18":
         print("Your are eligible of voting") 

#if else example.py
age_=input("give the age:") 
if age_>="18":
         print("Your are eligible of voting")        
else:
        print("your are not eligible for voting")

#if elif else example.py
marks_=input("give the marks:")
if marks_>="90" and marks_<="100":
         print("Your grade is A")
elif marks_>="60" and marks_<"89":
         print("Your grade is B")    
elif marks_>="50"and marks_<"59":
            print("Your grade is C")
elif marks_>="35"and marks_<"49":
            print("Your grade is D")
else:
            print("Your grade is F")

#while loop example.py
i=1
while i<=10:
    print(i)
    i=i+1
print("done")
#for loop example.py
for i in range(1,11):
    print(i)    
print("done")

#factorial example.py
n=int(input("Enter the number for factorial:"))
t=n
fact=1
while n>0:
    fact=fact*n  
    n=n-1
    print("Factorial:",fact)
print("done")

#table example.py
n=int(input("Enter the number for table:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

print("done")

#list function code
L=[1,2,3,4,9,6,5,8,7,10,3,6,8,9]
print(len(L))
print(min(L))
print(max(L))
print(sum(L))
print(list(reversed(L)))
print(sorted(L))

#list  method code
L=[]
L=[30,90]
L2=list()
n=int(input("enter no of elements:"))
for i in range(n):
    e=int(input("enter elements:"))
    L.append(e)
print("elements of list-1", L)  
print("elements of list-2:",L2)
i=int(input("Enter an Index to insert Element:"))
e=int(input("Enter an element To Insert:"))
L.insert(i,e)
print("List after inserting an element:",L)
e=int(input("Enter an count its occurance:"))
print("the occurance of",e,"in list:",L.count(e))
e=int(input("enter an Element to remove:"))
L.remove(e)
print("List after removing the element:",L)
print("List after popping an element: ",L.pop())
print("List after the popping of element with index:",L.pop(1))
L.reverse()
print("List after Reverse:",L)
L1=[3,4,5,6]
L.extend(L1)
print("List after merging with L1:",L)
print("List after clear with L1:",L.clear)

#fabonacci series
n=int(input("Enter the number of terms:"))  
a=1
b=1
if n<=1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
print("done")

#tuple example.py(built in functions)
t=(1,2,3,4,5,6,7,8,9)
print(len(t))
print(min(t))       
print(max(t))
print(sum(t))
print(sorted(t))
print(tuple(reversed(t)))

#tuple example.py(methods)
t=(1,2,3,4,5,6,7,8,9,3,6,8)
e=t.count(3)
print("the occurance of 3 in tuple:",e)  
f=(t.index(6))
print("the index of 6 in tuple:",f)

#list to tuple conversion
n=int(input("enter no of elements in the list:"))
l=list()
for i in range(n):
    e=int(input("enter elements:"))
    l.append(e)
print("elements of list:",l)
t=tuple(l)
print("elements of tuple:",t)
print("type of t:",type(t))

#set example.py(built in functions)
s={1,2,3,4,5,6,7,8,9}
print(len(s))
print(min(s))
print(max(s))
print(sum(s))
print(sorted(s))
print(set(reversed(s)))

#set example.py(methods)
s={1,2,3,4,5,6,7,8,9,3,6,8}
s.add(10)
print("set after adding an element:",s)
s.remove(3)
print("set after removing an element:",s)
s.pop()
print("set after popping an element:",s)
s.clear()
print("set after clear an element:",s)
s.discard(6)
print("set after discarding an element:",s)
s.update({11,12,13})
print("set after updating an element:",s)
s.union({14,15,16})
print("set after union an element:",s)
s.intersection({5,6,7})
print("set after intersection an element:",s)
s.difference({7,8,9})
print("set after difference an element:",s)
s.symmetric_difference({1,2,3})
print("set after symmetric difference an element:",s)
s.issubset({1,2,3})
print("set after subset an element:",s)
s.issuperset({1,2,3,4,5,6,7,8,9})
print("set after superset an element:",s)
s.isdisjoint({10,11,12})
print("set after disjoint an element:",s)

#set range example.py
s=set(range(1,11))
s={1,2,3,4,5,6,7,8,9,10}
print(s)

#set methods immplementation
s={1,2,3,4,5,6,7,8,9}
s=int(input("enter start position in range..?:"))
e=int(input("enter end position in range..?:"))
sp=int(input("enter step position in range..?:"))
s=set(range(s,e,sp))    
print("set elements are:",s)

#dictionary example.py(built in functions)
d={1:"one",2:"two",3:"three",4:"four",5:"five"}
print(len(d))
print(d.keys())
print(d.values())
print(d.items())
print(d.get(3))
print(d.pop())
print(d.popitem())
dd={6:"six",7:"seven"}
print(d.update(dd))
print(d.clear())