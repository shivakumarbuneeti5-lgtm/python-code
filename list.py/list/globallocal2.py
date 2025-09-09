x=10
def my_function():
    global y
    y=30
    x=20
    print("inside function x:",x)
    print("inside function y:",y)
my_function()
print("outside function x:",x)
print("outside function y:",y)
