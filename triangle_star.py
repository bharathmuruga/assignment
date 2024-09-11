n=int(input("enter the no:"))
m=1
for i in range(n):
  for j in range(n-1):
    print(" ",end=" ")
  for k in range(m):
    print("*",end=" ")
  n-=1
  m+=1
  print()

  