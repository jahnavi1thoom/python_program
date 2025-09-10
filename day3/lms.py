def add(d,key,value):
    d.update({key:value})
    return d
def remove(d,key):
    del d[key]
    return d
def search(d,key):
    if key in d:
        print("key found")
    else:
        print("element not found")
def display(d):
    for key,value in d.items():
        print(key," ",value)
def total(d):
   return len(d)
def exist(d,value):
    for i in d.values():
        if value==i:
            return True
        else:
            return False
d={}
t=int(input())
for i in range(t):
    choice=int(input())
    match choice:
        case 1:
            key=input()
            value=input()
            add(d,key,value)
            print("itenm added")
        case 2:
            key=input()
            remove(d,key)
            print("itenm removed:",key)
        case 3:
            key=input()
            print("itenm searchrd:",search(d,key))
        case 4:
            print(display(d))
        case 5:
            print(total(d))
        case 6:
            print("sorted list",exist(d,key))
        case 7:
           print("exiting")










