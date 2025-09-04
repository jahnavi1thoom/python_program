def StudentDetails(marks):
    if marks>40 and marks<=50:
        return "C grade"
    elif marks>51 and marks<=70:
        return "B grade"
    elif marks>71 and marks<=80:
        return "A grade"
    elif marks<40:
        return "Fail"
    else:
        return "Destension"
marks=int(input("enter the marks"))
print(StudentDetails(marks))