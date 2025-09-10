def vowel_consonent(l,v):
    v_count=0
    c_count=0
    for i in l:
        if i in v:
            v_count+=1
        else:
            c_count+=1
    return v_count,c_count
l=input()
v=['a','e','i','o','u']
print("Total number of vowels and consonenets:",vowel_consonent(l,v))
