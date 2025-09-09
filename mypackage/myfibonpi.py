def fibo(n):
    a=1
    b=1
    print(a)
    print(b)
    for _ in range(n):
        c=a+b
        print(c)
        a=b
        b=c
def evenodd(n):
    if n%2==0:
        return "EVEN"
    else:
        return "ODD"