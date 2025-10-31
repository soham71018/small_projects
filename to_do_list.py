task=[] #i'll use this to store the user task data into this list

def showmenu():
    print("*****************TO DO LIST*****************")
    print("1.View Task")
    print("2.Add your task")
    print("3.Mark down your task completed")
    print("4.Delete your task")
    print("5. Exit")


def showtask(tasks):
    if not tasks:
        print("No tasks yet!")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        title = task.get("title", "<no title>")
        status = "✅" if task.get("done") else "❌"
        print(f"{i}. {title} - {status}")



def addtask():
    title = input("Enter you task :")
    task.append({"title":title})
    print("Task added ✅")


def markdone():
    showtask(task)
    try:
       tasknum = int(input("Enter you want to markdone :"))
       task[tasknum - 1]["done"]=True
       print("Task marked as done ✅")
    except:
        print("Invalid task number ! Sorry")

def deletetask():
    showtask(task)
    try:
        delete = int(input("Enter task num you want to delete :"))
        removed = task.pop(delete -1) 
        print(f"Deleted task: {removed['title']}") 
    except:
        print("Invalid number entered")

while True:
        showmenu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            showtask(task)
        elif choice == 2:
            addtask()
        elif choice == 3:
            markdone()
        elif choice == 4:
            deletetask()
        elif choice == 5:
            print("Exiting... Goodbye 👋")
            break
        else:
            print("Invalid choice! Try again.")
           

 





