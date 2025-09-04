def CurrentBill(pmr,lmr):
    tu=pmr-lmr
    if tu<=50:
        cb=3.80*tu
    elif tu>50 and tu<=100:
        cb=(50*3.80)+(tu-50)*4.20
    elif tu>100 and tu<=200:
        cb=(50*3.80)+(50*4.20)+(tu-100)*5.10
        
    elif tu>200 and tu<=300:

        cb=(50*3.80)+(50*4.20)+(100*5.10)+(tu-200)*6.30
        
    else:
        cb=(50*3.80)+(50*4.20)+(100*5.10)+(100*6.30)+(tu-300)*7.5
    return cb
pmr,lmr=map(int,input().split())
print(CurrentBill(pmr,lmr))


        
