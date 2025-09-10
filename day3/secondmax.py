def secondlargest(l):
    largest=-1
    second_largest=-1
    for i in range(len(l)):
        if l[i]>largest:
            second_largest=largest
            largest=l[i]
    return second_largest
l=list(map(int,input().split()))
print(secondlargest(l))