def greater(a,b,c):
    if a>b:
        if a>c:
            print(a,"is greater")
        else:
            print(c,"is graeter")
    else:
        if b>c:
            print(b,"is graeter")
        else:
            print(c,"is greater")
a,b,c=map(int,input().split())
greater(a,b,c)