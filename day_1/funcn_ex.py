#no return and no arg
def add():
    print(20+30)
add()


#with return and no arg
def add():
    return 23+45
print(add())


#ith arg and return type
def add(a,b):
    return a+b
a=int(input())
b=int(input())
print(add(a,b))


#with arg and no return type
def add(a,b):
    print(a+b)
add(20,12)


#example to conver kilometer to miles
def kilo_to_mile(y):
    mile=y*0.6
    return mile
print("enter kilometer:")
k=int(input())
print(kilo_to_mile(k))