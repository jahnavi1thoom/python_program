def even_odd_count(l):
    even_count=0
    odd_count=0
    for i in l:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    print("even count",even_count)
    print("odd count",odd_count)
l=list(map(int,input().split()))
even_odd_count(l)