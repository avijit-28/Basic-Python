list1=[15,6,8,45,412,10,1]
print('original list is ' ,list1)
for i in range (1,len(list1)):
  key=list1[i]
  j=i-1
  while j>=0 and key<list1[j]:
    list1[j+1]=list1[j]
    j=j-1
    print(list1,end=' ')
    print()
  else:
    list1[j+1]=key
    print(list1,end=' ')
print("list after sorting:", list1)
