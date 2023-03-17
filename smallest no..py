a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a>b:
  if c>b:
    print(b,"is the smallest no.")
  else:
    print(c,"is the smallest no.")
elif a<c:
  print(a,"is the smallest no.")
else:
  print(c,"is the smallest no.")
