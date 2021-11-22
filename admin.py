def admin1():
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
    