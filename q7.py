print ("upto which term do you want fibbonacci sequence ")
n=input ()
fibb=[0,1]
sum_=0
for i in range (0,int(n)+1):
   if i>=2:
      fibb. append (fibb[i-1]+fibb[i-2])
   print (fibb[i],end="\t")
   sum_+=int(fibb[i])
   if i==int(n):
      print (f"\naverage of all the terms= {sum_/(int(n)+1)}")
