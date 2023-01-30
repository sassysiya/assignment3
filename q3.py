l = int(input("Enter lower limit: "))
u = int(input("Enter upper limit: "))
a = [(x,x**2) for x in range(l,u+1)]
print (a)
