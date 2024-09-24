n=int(input("enter the number: "))
m=1
for i in range(n):
  for x in range(n-i-1):
    print(" ",end=" ")
  for k in range(m):
    print("*",end=" ")
  m+=1
  print()
  