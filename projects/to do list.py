to_do_list=[]
def add_task(task):
   return to_do_list.append(task)

def view_the_task():
  if len(to_do_list)==0:
     print("to do list  is empty")
  for item in range (len(to_do_list)):
     print(item+1,to_do_list[item])
     
     

def delete_task(delete_item):
   dele= to_do_list.pop(delete_item-1)
   print(f"{dele} task is delete")
   

def display():
   print("1:add")
   print("2:view")
   print("3:delete")
   print("4:exit")

while True:
  display()

  user=input("enter(1/2/3/4): ")
  if user=="4":
       print("exiting the application")
       break
  elif user=="1":
    while True: 
     task=input("enter the task (1:back):")
     if task=="1":
        break
     add_task(task)
  elif user=="2":
     view_the_task()
  elif user=="3":
     delete_item=int(input("enter the item: to be delete: "))
     if len(to_do_list)==0:
        print("to do list is EMPTY")
        break
     delete_task(delete_item)
   
