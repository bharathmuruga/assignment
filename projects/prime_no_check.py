def prime_no_checker(number):
  if number<=1:
    return False
  else:
    for i in range(2,number):
        if number%i==0:
           return False
    else:
       return True
        
number=int(input("enter the number: "))  
if prime_no_checker(number):
   print(f"{number} is prime")
else:
   print(f"{number} is not prime")
  