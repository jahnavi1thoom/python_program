c_num=int((input("enter number of consumer:")))
for i in range(c_num):
   c_name=input("enter consumer name:")
   pmr=int(input("enter current month reading:"))
   lmr=int(input("enter last month reading:"))
   cost_punit=3.80
   #print("c_name:",c_name,"\tc_number:",c_num,"\tpmr:",pmr,"\tlmr:",lmr)
   print("name\t\t number\t\t pmr\t lmr\t ")
   print(c_name,"\t",c_num,"\t",pmr,"\t",lmr,"\t")
   #print(f"name:{c_name} number:{c_num} pmr:{pmr} lmr:{lmr}")
   print("total units:",pmr-lmr)
   print("current bill:",round((pmr-lmr)/cost_punit,2))
