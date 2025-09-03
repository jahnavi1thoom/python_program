def dayToYear(d):
    year=d//365
    m=d-(year*365)
    month_rem=m//30
    return year,month_rem

d=int(input("enter number of days:"))
result=dayToYear(d)
print(result)
