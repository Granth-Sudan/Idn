x=69
while x!=0:
 a=input("give command:")
 if (a=="HELP" or a=="-h" or a=="help" or a==" -h"):
    b='\nread or -r to read the whole database\n search or -s to seach\n make or -m to add data\n-srt or sort to sort data \n -d or delete to delete entry\n exit() or exit to exit \n '
    print(b)
 if (a=="read" or a=="-r" ):
  with open("file.txt" ,"r") as f:
   print(" the file context: ")
   print("\n",f.read())
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
     b=(new+"  , "+nm+" , "+cl+" , "+mrks+"  , "+st+"\n")
     f.write(b)
     print(b)
 if (a=="-srt" or a=="sort"):  
  with open("file.txt","r") as f: 
   lines=f.readlines()
   lines.sort()
  with open("file.txt","w") as f:
    for line in lines:
      f.write(line )
 if (a=="-d" or a== "delete"):
   with open("file.txt","r")as f:
    lines=f.readlines()
    with open("file.txt","w") as fw:
     inp=input(str("give me a id no:"))
     for line in lines:
      if line.find(inp)==-1:
        fw.write(line)
        print("deleted")
          
 if (a=="gg" or a=="group"):
  print("conributors are,'','','','','',")
 if (a=="exit" or a=="exit()"):
  x=0
