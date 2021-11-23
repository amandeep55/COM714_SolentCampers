r=[]
import os,csv
def customer(e):
  print("<----Login successfull as a Customer--->")
  print("select your choice::")
  print("1.Request to advisior to Book the van")
  print("2.See the summary")
  print("for logout press any key::")
  a=int(input())
  k=[]
  l=0
  t=0
  ti=0
  s="pending"
  if a==1:
    l=str(input("ENter the location:"))
    t=str(input("Enter the van size small/medium/large::"))
    ti=str(input("enter tha date::"))
    
    r.append([l,t,ti,e,s])
    print("Request added successfuly",r)
    customer(e)
  elif a==2:
    print("location name:",l)
    print("van number",vn)
    print("van type:",t)
    print("data:",ti)
    print("Status:",s)
    customer(e)
  else:
    print("Thanks for services")
  with open("bookings.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(r)


