'''class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age

p1=person("bharath","john")
print(p1.name,p1.age)'''

'''class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  
  def __str__(self):
    return (f"{self.name},{self.age}")

p1=person("john",23)
print(p1)'''

class person:
  def __init__(self,firstname,lastname):
    self.firstname=firstname
    self.lastname=lastname

  def fun(self):
    print(self.firstname,self.lastname)



'''class student(person):
  def __init__(self,firstname,lastname):
    person.__init__(self,firstname,lastname)'''

class student(person):
  def __init__(self,firstname,lastname,year):
   super().__init__(firstname,lastname)
   self.graduation=year
   
  def welcome(self):
    print("hi welcome",self.firstname,self.lastname,"to",self.graduation)

x= student("mike","joe",2019)
x.welcome()

class user:
  users=0
  def __init__(self,user_name,pwd):
    self.user_name=user_name #instance variable
    self.pwd=pwd
    user.users+=1
  def register(self):
    print("registering.." + self.user_name)
  
  def login(self):
    print("logging..."+self.user_name)
    return self
  
user1=user("bharath","abc123")
user2=user("kiran","345jg")
user3=user("john","lkk56")

user1.login().register() #chained

from abc import ABC, abstractmethod
#abstract
class vehicle(ABC):# abstract class
  @abstractmethod # decotrator
  def start(self):
    pass
  def stop(self):
    pass


class bike(vehicle):
  def start(self):
    print("you are riding a bike...")

class car(vehicle):
  def start(self):
    print("riding car...")

car1=car()
car1.start()




