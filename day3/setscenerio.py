def scenerio(d1,d2,d3):
      d1=[i.lower() for i in d1]
      d2=[i.lower() for i in d2]
      d3=[i.lower() for i in d3]
      s1=set(d1)
      s2=set(d2)
      s3=set(d3)
      print("day 1 atttendees:",s1)
      print("day2 attendees:",s2)
      print("day3 attendees:",s3)
      d=d1+d2+d3
      s=set(d)
      print("total number of attendees are:",len(s))
      
      print("attendees who atttended all three days are:",s1&s2&s3)
      l=[]
      for i in s:
            if i not in s2 and i not in s3 and i in s1:
                  l.append(i)
            elif i not in s1 and i not in s2 and i in s3:
                  l.append(i)
            elif i not in s1 and i in s2 and i not in s3:
                  l.append(i)
      print("attendees who attended exactly one day are:",l)
      print("day1 and day2 overlap are:",s1&s2)
      print("day2 and day3 overlap are:",s2&s3)
      print("day3 and day1 overlap are:",s3&s1)
d1=list(map(str,input().split()))
d2=list(map(str,input().split()))
d3=list(map(str,input().split()))
scenerio(d1,d2,d3)
      
                  

            
      


