str1=input("enter a string")
str2=input("enter substring from str1")
len_str1=len(str1)
len_str2=len(str2)
start=count=0
end=len_str1
while True:
  pos=str1.find(str2,start,end)
  if pos !=-1:
    count+=1
    start=pos+len_str2
  else:
    break
  if start>=len_str1:
    break
print("no occurence of ",str2, ':',count)
