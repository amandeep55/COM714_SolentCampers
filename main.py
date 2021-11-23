import csv
file1 = open('login.csv')
csvreader = csv.reader(file1)
header = []
header = next(csvreader)
rows=[]
for row in csvreader:
    rows.append(row)
import  os
def Advisior():
  import csv
  import os
  book = open('bookings.csv')
  csvreader1 = csv.reader(book)
  header = []
  header = next(csvreader1)
  booking=[]
  for row in csvreader1:
          booking.append(row)
  av = open('aval.csv')
  csvreader2 = csv.reader(av)
  header = []
  header = next(csvreader2)
  ava=[]
  for row in csvreader2:
          ava.append(row)
  print("<------Login successfull as Advisior--------->")
  print("1.check boookings  :: ")
  print("2.Booking approvel  :: ")
  print("3.Check avaliablety :: ")
  a=int(input())
  if a==1:
    print("Location      TYPE       Date        UserID")
    for i in range(len(booking)):
      print(booking[i][0],"    ",booking[i][1],"   ",booking[i][2],"    ",booking[i][3])
    Advisior()
  elif a==2:
    print("SNo    ","Location      TYPE       Date        UserID")
    for i in range(len(booking)):
      print(i+1,"    ", booking[i][0],"    ",booking[i][1],"   ",booking[i][2],"    ",booking[i][3])
    a=(int(input("select booking ::")))-1
    for i in range(len(ava)):
      if booking[a][0]==ava[i][0] and ava[i][2]==str(0) and ava[i][3]==booking[a][1].lower():
        print("Booking successfull")
        ava[i][2]=1

        Advisior()
  elif a==3:
    print("Location     cab number     condition")
    for i in range(len(ava)):
      print(ava[i][0],"     ",ava[i][1],"     ",ava[i][2])
    Advisior()
  else:
    print("Wrong input")
  file="aval.csv"
  if(os.path.exists(file) and os.path.isfile(file)):
    os.remove(file)
  fields=["Location","cab number","condition","type"]
  with open("aval.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)
    csvwriter.writerows(ava)
  file="bookings.csv"
  if(os.path.exists(file) and os.path.isfile(file)):
    os.remove(file)
  fields=["Locations","Type","Date","UserID","Status"]
  with open("bookings.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields)
    csvwriter.writerows(ava)
def admin():
  import csv,os
  av = open('aval.csv')
  csvreader2 = csv.reader(av)
  header = []
  header = next(csvreader2)
  ava=[]
  for row in csvreader2:
      ava.append(row)
  print("<----------------login successfull as a admin------------>")
  print("1. Check summary of the van::")
  print("2. add new van::")
  a=int(input())
  if a==1:
    print("Location     cab number     condition    type")
    for i in range(len(ava)):
      print(ava[i][0],"     ",ava[i][1],"     ",ava[i][2],"     ",ava[i][3])
    admin()
  elif a==2:
    l=input("Enter the locations ::")
    n=input("Enter the cab number::")
    c=input("enter the condition(in 1 or 0)::")
    t=input("Enter the type ::")
    k=[]
    k.append(l)
    k.append(n)
    k.append(c)
    k.append(t)
    ava.append(k)
    file="aval.csv"
    if(os.path.exists(file) and os.path.isfile(file)):
      os.remove(file)
    fields=["Location","cab number","condition","type"]
    with open("aval.csv", 'w') as csvfile: 
      csvwriter = csv.writer(csvfile) 
      csvwriter.writerow(fields)
      csvwriter.writerows(ava)
    admin()
  else:
    print("Wrog input logout successfully")
def customer(e):
  print("<----Login successfull as a Customer--->")
  print("select your choice::")
  print("1.Request to advisior to Book the van")
  print("2.See the summary")
  print("for logout press any key::")
  a=int(input())
  k=[]
  r=[]
  l=0
  t=0
  ti=0
  vn=0
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



def main():
  filename = "bookings.csv"
  fields=["Locations","Type","Date","UserID","Status"]
  with open("bookings.csv", 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
  print("<----------Please login --------->")
  u=int(input("Enter the type of user 1 (customer) 2(Advisior) 3 (Admin)::-"))
  if u==1 or u==2 or u==3:
    pass
  else:
    print("wrong credintial login again")
    main()
  e=input("Enter the UserID::-")
  p=input("password::-")
  for i in range(len(rows)):
    if rows[i][0]==e:

      a=i
      print(a)
      if rows[a][0]==e and rows[a][1]==p and rows[a][2]==str(u):
        if rows[a][2]=="1":
          customer(e)
        elif rows[a][2]=="2":
          Advisior()
        elif rows[a][2]=="3":
          admin()
      else:
        print("wrong credintial login again")
        main()
    else:
      pass
main()
