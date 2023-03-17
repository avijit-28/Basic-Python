line=input("enter a line")
sub=input("enter substring")
lenght=len(line)
sub=len(sub)
start=count=0
end=lenght
while True:
  pos=line.find(sub,start,end)
  if pos!=-1:
    count+=1
    start=pos+count
  else:
    break
  if start>=lenght:
    break
  print("no. of occurence of", sub,":", count)
