def checknumber(a):
    if a>=0:
        return "Positive"
    else:
        return "Negative"
a=int(input("enteer a number:"))
print(checknumber(a))