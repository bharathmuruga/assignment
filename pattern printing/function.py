
#function with key word arguments
def my_function(food2,food3,food1):
  print("your fav food is "+" "+food1)
my_function(food1="fruits",food2="non_veg",food3="veg")

#function with *args
def my_food(*food):
  print("my fav food"+" "+food[1])
my_food("veg","non-veg","fruits")

#function with **kargs
def my_sports(**game):
  print("my fav game is"+ " " +game["game2"])
my_sports(game1="football",game2="cricket",game3="hockey")

#default parameter value
def my_function(country ="norway"):
  print("I am from " + country)
my_function("sweden")
my_function("india")
my_function()
my_function("brazil")

#passing list as args
def my_function(food):
  for x in food:
    print(x)
fruits=["apple","banana","cherry","orange"]
my_function(fruits)

#function for return a value
def my_function(x):
  return 5*x
print(my_function(3))
print(my_function(4))

#pass statement
def myfunctio():
  pass

#postional only args
def my_function(x,/):
  print(x)
my_function(3)

#key word only args
def my_function(*,x):
  print(x)
my_function(x=3)

#combine postional and key args
def my_function(a,b,/,*,c,d):
  print(a+b+c+d)
my_function(2,3,c=5,d=4)
