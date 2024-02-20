x = int(input("Enter a number: "))
y = int(input("Enter a number: "))
f1 = []
for i in range(x,0,-1):
    if x % i == 0:
        f1.append(i)
f2 = []
for i in range(y,0,-1):
    if y % i == 0:
        f2.append(i)
i = 0
while f1[i] not in f2:
    i = i + 1
print("The GFC of",x,"and",y,"is",f1[i])
