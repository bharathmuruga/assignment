def box_pattern(n):
  for i in range(n):
   for x in range(n):
    print("*",end=" ")
   print()


def triangle_pattern(n):
 r=1
 for i in range(n):
  for x in range(r):
   print("*",end=" ")
  r+=1
  print()

def left_half_pyramid(n):
 m=1
 for i in range(n):
   for x in range(n-i-1):
    print(" ",end=" ")
   for y in range(m):
     print("*",end=" ")
   m+=1
   print()


def user_choice():
 print("choose 1 for box pattern")
 print("choose 2 for triangle pattern")
 print("choose 3 for left half pyramid")

 choice=int(input("enter the choice from (1-3): "))
 n=int(input("enter the number of time : "))

 if choice==1:
  box_pattern(n)
 elif choice==2:
  triangle_pattern(n)
 elif choice==3:
   left_half_pyramid(n)
 else:
  print("invalid choice")


user_choice()


