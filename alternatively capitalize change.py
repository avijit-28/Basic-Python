str1=input("enter string")
len_str1=len(str1)
print("original string", str1)
str2=" "
for a in range(0,len_str1,2):
  str2+=str1[a]
  if a<len_str1 -1:
    str2+=str1[a+1].upper()
print(str2)

