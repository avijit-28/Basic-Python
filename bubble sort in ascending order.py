list1=[13,65,21,54,35,45,6]
print("original list is", list1)
n=len(list1)
for i in range(n):
  for  j in range (0,n-i-1):
    if list1[j]>list1[j+1]:
      list1[j],list1[j+1]=list1[j+1],list1[j]
print("list after sorting is",list1)
