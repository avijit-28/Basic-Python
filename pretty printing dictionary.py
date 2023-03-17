n=int(input("no. of student"))
compwinners={}
for a in range(n):
  key=input("enter the student name")
  value=int(input("no. of competetions won"))
  compwinners[key]=value
print("the dictionary is  :-  ",compwinners)
import json
print(json.dumps(compwinners, indent=2))
