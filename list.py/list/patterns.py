# pattern 1
# square
for i in range(6):
    for j in range(6):
        print("?",end=" ")
    print()

# pattern 2
# right angle triangle
for i in range(5):
    for j in range(i+1):
        print("?",end=" ")
    print()
    

# pattern 3
#  reverse right angle triangle   
for i in range(5): 
    for j in range(5-i):
        print("+",end=" ")
    print()
    
 # pattern 4
 # piramid   
for i in range(5):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("@",end=" ")
    for j in range(i):
        print("@",end=" ")
    print()

# parameter 5
# dimond
n = 5  

# Top half
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Bottom half
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))        