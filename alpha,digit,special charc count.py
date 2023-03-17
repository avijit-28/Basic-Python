alphacount=digitcount=spacecount=0
a=input("enter any sentence")
print(len(a))
for b in a:
  if b.isalpha():
    alphacount+=1
  elif b.isdigit():
    digitcount+=1
  elif b.isspace():
    spacecount+=1
print("alphabet",alphacount)
print("digit",digitcount)
print("special character",len(a)-(alphacount+digitcount+spacecount))
