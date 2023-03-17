lowercount=uppercount=0
a=input("enter any sentence")
c=len(a)
for b in a:
  if b.islower():
    lowercount+=1
  elif b.isupper():
    uppercount+=1
print(c)
print("tolal lowercase letter:",lowercount)
print("total uppercase letter:",uppercount)
