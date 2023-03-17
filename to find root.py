import math
print("for quadratic equation, ax**2+bx+c=0, enter coefficient below:")
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if a==0:
  print("value a",a,"should not be zero")
  print("\n Aborting!!!!")
else :
  delta=b**b-4*a*c
  if delta >0:
    root1=(-b - math.sqrt(delta))/(2*a)
    root2=(-b + math.sqrt(delta))/(2*a)
    print("roots are real and unequal")
    print("ROOT1",root1, "ROOT2",root2)
  elif delta==0:
    roo1=-b/(2*a)
    print("roots are real and unequal")
    print("ROOT1",root1, "ROOT2",root2)
  else:
    print("roots are complex or imaginary")
