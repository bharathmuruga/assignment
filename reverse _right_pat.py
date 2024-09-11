#reverse_right_pattern
n=int(input("enter the no: "))
for i in range(n):
  for j in range(n):
    print("*",end=" ")
  n-=1
  print()