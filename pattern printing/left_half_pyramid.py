n=int(input("enter the no:"))
m=1
for i in range(n):
  for j in range(n):
    print(" ",end=" ")
  for k in range(m):
   print("*",end=" ")
  m+=1
  n-=1
  print()