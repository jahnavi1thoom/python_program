def Exception(a,b):
    try:
        div=a//b
        print("division value:",div)
    except:
        if(b==0):
            print("Error:Division by zero is not allowed")
a,b=map(int,input().split())
Exception(a,b)