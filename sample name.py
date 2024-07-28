x=69
while x!=0:
 a=input("give command:")
 if (a=="HELP" or a=="-h" or a=="-help" or a==" -h"):
    b='read or -r to read the whole database\n search or -s to seach\n make or -m to add data\n-re or replace to replace data '
    print(b)
 if (a=="read" or a=="-r" ):
  with open("file.txt" ,"r") as f:
   print(" the file context: ")
   print(f.read())
 if (a== "search" or a== "-s"):
  b= input("name or uniqe id or status: ") 
  with open("file.txt","r") as f:
   for line in f:
    if b in line:
     print(line)
    else:
      print("there is a typo or there is no entry")
 if (a=="-m" or a=="make"):
   with open("file.txt","a") as f:
     new=input("id:")
     nm=input("name:")
     cl=input("class:")
     mrks=input("marks:")
     st=input("status:")
     b=("\n"+new+" , "+nm+" , "+cl+" , "+mrks+"  , "+st)
     f.write(b)
     print(b)
#  working on it
#  if (a=="-re" or a=="replace"):
#    with open("file.txt","r+w")
 if (a=="gg" or a=="group"):
  print("conributors are,'','','','','',")
 if (a=="exit" or a=="exit()"):
  x=0