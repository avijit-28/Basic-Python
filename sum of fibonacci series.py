n=int(input("enter any number :"))
first=0
second=1
print(first)
print(second)
for a in range(1, n+1):
  third=first+second
  print(third, end='')
  first, second= second, third
  print()
  
