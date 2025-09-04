d1={'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine",'0':"zero"}
n=(input("enter a number"))
st=""
for i in n:
    st=st+" " +d1[i]

print(st)
