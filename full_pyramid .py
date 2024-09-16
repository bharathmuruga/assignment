n=int(input("enter the number: "))
for i in range(n):
  for x in range(1,n):
    print("",end=" ")
  for y in range(i+1,):
    print("*",end=" ")
  
  n-=1
  print()