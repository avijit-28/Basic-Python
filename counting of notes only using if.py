total_amt=int(input("Enter any amount: "))
note=0
money=0
if total_amt > 0:
  a=total_amt//2000
  note +=a
  total_amt=total_amt%2000
  money+=2000*a
  print('2000\t x\t',a,'\t=\t',2000*a)
  a=total_amt//500
  note +=a
  total_amt=total_amt%500
  money+=500*a
  print('500\t x\t',a,'\t=\t',500*a)
  a=total_amt//200
  note +=a
  total_amt=total_amt%200
  money+=200*a
  print('200\t x\t',a,'\t=\t',200*a)
  a=total_amt//100
  note +=a
  total_amt=total_amt%100
  money+=100*a
  print('100\t x\t',a,'\t=\t',100*a)
  a=total_amt//50
  note +=a
  total_amt=total_amt%50
  money+=50*a
  print('50\t x\t',a,'\t=\t',50*a)
  a=total_amt//20
  note +=a
  total_amt=total_amt%20
  money+=20*a
  print('20\t x\t',a,'\t=\t',20*a)
  a=total_amt//10
  note +=a
  total_amt=total_amt%10
  money+=10*a
  print('10\t x\t',a,'\t=\t',10*a)
  a=total_amt//5
  note +=a
  total_amt=total_amt%5
  money+=5*a
  print('5\t x\t',a,'\t=\t',5*a)
  a=total_amt//2
  note +=a
  total_amt=total_amt%2
  money+=2*a
  print('2\t x\t',a,'\t=\t',2*a)
  a=total_amt//1
  note +=a
  total_amt=total_amt%1
  money+=1*a
  print('1\t x\t',a,'\t=\t',1*a)
  print("--------------------------------------")
  print('\t  Total',note,'notes of --> ',money)
else:
  print("Please !!! enter vamild amount...")







  
  
  
