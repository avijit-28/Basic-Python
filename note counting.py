total_amt=int(input("Enter any amount: "))
note=0
money=0
while total_amt > 0 :
  if total_amt > 0:
    if total_amt >= 2000:
      a=total_amt//2000
      note +=a
      total_amt=total_amt%2000
      money+=2000*a
      print('2000   x\t',a,'\t=\t',2000*a)
    else:
      print('2000   x\t',0,'\t=\t',2000*0)
  if total_amt > 0:
    if total_amt >= 500:
      a=total_amt//500
      note +=a
      total_amt=total_amt%500
      money+=500*a
      print('500    x\t',a,'\t=\t',500*a)
    else:
      print('500    x\t',0,'\t=\t',500*0)
  if total_amt > 0:
    if total_amt >= 200:
      a=total_amt//200
      note +=a
      total_amt=total_amt%200
      money+=200*a
      print('200    x\t',a,'\t=\t',200*a)
    else:
      print('200    x\t',0,'\t=\t',200*0)
  if total_amt > 0:
    if total_amt >=100:
      a=total_amt//100
      note +=a
      total_amt=total_amt%100
      money+=100*a
      print('100    x\t',a,'\t=\t',  100*a)
    else:
      print('100    x\t',0,'\t=\t',100*0)
  if total_amt > 0:
    if total_amt >=50:
      a=total_amt//50
      note +=a
      total_amt=total_amt%50
      money+=50*a
      print('50     x\t',a,'\t=\t',50*a)
    else:
      print('50     x\t',0,'\t=\t',50*0)
  if total_amt > 0:
    if total_amt >=20:
      a=total_amt//20
      note +=a
      total_amt=total_amt%20
      money+=20*a
      print('20     x\t',a,'\t=\t',20*a)
    else:
      print('20     x\t',0,'\t=\t',20*0)
  if total_amt > 0:
    if total_amt >=10:
      a=total_amt//10
      note +=a
      total_amt=total_amt%10
      money+=10*a
      print('10     x\t',a,'\t=\t',10*a)
    else:
      print('10     x\t',0,'\t=\t',10*0)
  if total_amt > 0:
    if total_amt >=5:
      a=total_amt//5
      note +=a
      total_amt=total_amt%5
      money+=5*a
      print('5      x\t',a,'\t=\t',5*a)
    else:
      print('5      x\t',0,'\t=\t',5*0)
  if total_amt > 0:
    if total_amt >=2:
      a=total_amt//2
      note +=a
      total_amt=total_amt%2
      money+=2*a
      print('2      x\t',a,'\t=\t',2*a)
    else:
      print('2      x\t',0,'\t=\t',2*0)
  if total_amt > 0:
    if total_amt >=1:
      a=total_amt//1
      note +=a
      total_amt=total_amt%1
      money+=1*a
      print('1      x\t',a,'\t=\t',1*a)
    else:
      print('1      x\t',0,'\t=\t',1*0)
print("--------------------------------------")
print('\t  Total',note,'notes of --> ',money)
    
