def factorial(number):
  if number<0:
      return None
  if number==1 or number==0:
    return 1
  else:
    return number*factorial(number-1)
    

def out_put(number):
    fact_result=factorial(number)
    if fact_result is not None:
       print(f"factorial of {number} is ",fact_result)
    else:
       print(f"{number} is a negative number")
       


number=int(input("enter the number: "))
out_put(number)
