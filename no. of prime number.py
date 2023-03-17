for a in range (1,31):
  count=0
  for b in range (1,a+1):
    if a%b==0:
      count+=1
  if count==2:
    print(a)
