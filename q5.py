x = "ABCDEFGHIJK"
m = 0
n = 0
p = " "
while len(x)>= 1:
    y = x[ :-m]
    print(n*p, y)
    m = m+2
    n = n+1
    if y == "A":
        break
