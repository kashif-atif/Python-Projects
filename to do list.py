tasks = []

while True :
  print (" TO-DO-LIST ")

  print ("1 - add a task")
  print ("2 - view a task")
  print ("3 - remove a task")

  choice =  int (input("enter the choice"))

  if choice == 1:
    task = input("add a task :")
    tasks.append(task)
    print ("task added succcessfully")

  elif choice == 2:
    print (task)  
    
  elif choice == 3:
    task = input("enter task to remove")
    tasks.remove(task)

  else:
    break