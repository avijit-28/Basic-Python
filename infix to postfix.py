# for examples :-
"a+(b*c-(d/e^f)*g)*h"
"(a*(b+((c+d)*(e+f))/g))*h"
"a+((b+c)+(d+e)*f)/g"
str1=input(" Enter any equation : ")

lst1=" ".join(str1)
lst2=lst1.split()
print(lst2) # break all characters
lst3=[]
lst4=[]
for i in range (len(lst2)):
    a=lst2[i]
    print(a)
    if a=="(":
        lst3.append(a) #appending operator
        print("stack",lst3)
    elif a==")":
      while lst3[-1] != "(":
            t=lst3.pop()
            lst4.append(t)
      else:
        lst3.pop()
        print("stack",lst3)
        print(lst4)
    elif a!="^" and a!="/" and a!="*" and a!="+" and a!="-" and a!="(" and a!=")" :
        lst4.append(a) # appending operand (like a,b,..,z or A,B,..,Z)
        print(lst4)
    elif a=="^":
        ro=a
        print("ro",ro)
        if lst3==[]:
            lst3.append(a)
            print("stack",lst3)
        else:
            lst3.append(a)
            print("stack",lst3)
            
    elif a=="/":
      if lst3==[]:
        lst3.append(a)# if stack is empty --> appending /
        print("stack",lst3)
      elif lst3[-1]== "*" or lst3[-1]== "+" or lst3[-1]== "-" :
        lst3.append(a)  #if previous char. is less priroty than current char. --> appending /
        print("stack",lst3)
      else:
        while lst3[-1]== "^":
            
            u=lst3.pop()   #if previous char. is greater priroty than current char. --> poping previous char 
                         #until previous char. is less priroty than current char.
            lst4.append(u)
        else:
          lst3.append(a) # appending operator here
          print("stack",lst3)
          print(lst4)
        
    elif a=="*":
      if lst3==[]:
        lst3.append(a)  # if stack is empty --> appending *
        print("stack",lst3)
      elif lst3[-1]== "+"  or lst3[-1]== "-" :
        lst3.append(a)  #if previous char. is less priroty than current char. --> appending *
        print("stack",lst3)
        
      else:
        while lst3[-1] == "/" or lst3[-1]== "^" :
        
            k=lst3.pop()   #if previous char. is greater priroty than current char. --> poping previous char
                         #until previous char. is less priroty than current char.
            lst4.append(k) # poped char. --> appending with operand
        else:
          lst3.append(a) # appending operator here
        print("stack",lst3)
        print(lst4)
                  
    elif a=="+":
       if lst3==[]:
        lst3.append(a)  # if stack is empty --> appending +
        print("stack",lst3)
       elif lst3[-1]== "-":
        lst3.append(a)  #if previous char. is less priroty than current char. --> appending + 
        print("stack",lst3)
       else :
         while lst3[-1] == "/" or lst3[-1]=="*" or lst3[-1]== "^":
             
             p=lst3.pop()   #if previous char. is greater priroty than current char. --> poping previous char 
                         #until previous char. is less priroty than current char. 
             lst4.append(p) # poped char. --> appending with operand
         else:
           lst3.append(a)  # appending operator here
           print("stack",lst3)
           print(lst4)
    elif a=="-":
      if lst3==[]:
        lst3.append(a)  # if stack is empty --> appending -
        print(lst4)
      else:
        while lst3[-1]== "/"  or lst3[-1]== "*" or lst3[-1]== "+" or lst3[-1]== "^" or lst3[-1]!= "(":
            
            g=lst3.pop()  #if previous char. is greater priroty than current char. --> poping previous char 
                         #until previous char. is less priroty than current char.
            lst4.append(g)  # poped char. --> appending with operand
        
        else:
            if lst3[-1]=="(" or lst3==[]:
               
              lst3.append(a)  # appending operator here
              print("stack",lst3)  
              print(lst4) 
for x in range (len(lst3)):
  s=lst3.pop()
  lst4.append(s)
print(lst4)

str2="".join(lst4)
print("Equation of infix -->",str1)
print("Equation of postfix -->",str2)
      
           

       
        

