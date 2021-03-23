yr1=int(input("enter the current cyear"))
yrn=int(input("enter last year"))
for i in range(yr1,yrn+1):
  if (i%4==0 or i%100==0 or i%400==0):
     print(i)
  i=i+1
