print("1. Add task\n2. Remove\n3. Update\n4. Display\n5. Quit\n")
l1 = []
count = 0
while (True):
    ch = int(input("Enter choice : "))
    if(ch == 1):
        x = input("Enter the task : ")
        l1.append(x)
    elif(ch == 2):

        x = int(input("Enter task number to be removed : "))
        if(x>0 and x<=len(l1)):
            l1.remove(l1[x-1])
        else:
            print("Task number not found")
    elif(ch == 3):
        x = int(input("Enter task number to be updated : "))

        if(x>0 and x<=len(l1)):
            s = input("Enter the task : ")
            l1[x-1]= s
        else:
            print("Task number not found")
    elif(ch == 4):
        if(len(l1) > 0):
            print("Tasks are : ")
            count = 1
            for i in l1:
                print(str(count)+". "+i)
                count = count+1
        else:
            print("No tasks found\n")
    elif(ch == 5):
        print("Program terminated\n")
        break
    else:
        print("Invalid choice")