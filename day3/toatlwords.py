def total_words(l):
    count=1
    for i in l:
        if i.isspace():
            count+=1

    return count
l=input()
print("total number of words:",total_words(l))
        