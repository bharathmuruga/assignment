#numbers_increament_pattern
n=int(input("enter the no: "))
k=1
for i in range(n):
  for j in range(1,k+1):
    print(j, end=" ")
  k+=1
  print()
