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