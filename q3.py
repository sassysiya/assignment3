a = int(input("Enter number of terms you want in list: "))
x = []
for i in range(0,a):
    d = int(input(f"Enter {i+1} th item of list: " ))
    x.append(d)
x.sort()
y = []
for j in range(0,a):
    g = x[j]**2
    y.append(g)

list_tuple = list(zip(x,y))
print(list_tuple)
