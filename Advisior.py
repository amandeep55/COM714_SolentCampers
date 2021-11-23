def Advisior1():
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
Advisior()