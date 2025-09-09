squares=[x**2 for x in range(5) ]
print(squares)

squares=[x**2 for x in range(5) ]
print("odd squares:",squares)


squares=[x**2 for x in range(5) if x%2==0 ]
print("even squares:",squares)

squares=[x+2 for x in range(5) if x%2==0]
print("even:",squares)

squares=[x+1 for x in range(5) if x%2==0 ]
print("odd:",squares)

