# Todo List

lst = []

def readTodoList():
    for task in lst:
        print(f"{task[0]} is {if(task[1]!=None):task[1]else:print("not Completed",end="")}")
    
def AddTask():
    task = input("Enter the task: ")
    lst.append([task,None])

def MarkCompleted():
    count = 1
    for i in lst:
        print(f"{count}. {i[0]}")
        count += 1
    user_input = int(input(":"))
    if user_input>=len(lst):
        lst[user_input][1] = "Done"
    else:
        print("Wrong input")

def ClearList():
    lst.clear()

while True:
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark a Task as completed.")
    print("4. Clear Todo List")

    user_input = int(input(":"))

    if user_input==1:
        AddTask()

    if user_input==2:
        readTodoList()
    
    if user_input==3:
        MarkCompleted()

    if user_input==4:
        ClearList()