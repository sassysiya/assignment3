a = input("Enter a word : ")
b = len(a)
p = ' '.join(a.split())
r = len(p)
unique = []
if " " not in p:
   for i in range(0, r):
       de =  f"The number of occurence of {p[i]} is {p.count(p[i])}"
       if de in unique :
           continue
       else:
           unique.append(de)

   for item in unique :
        print(item)


else :
   x = a.split()
   y = len(x)
   for j in range(0,y):
       l = f"The number of occurence of {x[j]} is {x.count(x[j])}"

       if l in unique:
           continue
       else:
           unique.append(l)

   for items in unique:
        print(items)


