import os
tasks=[]
#load function 
def load_task(tasks):
  
    if os.path.exists("task.txt"):
        with open ("task.txt", "r") as file:
            tasks=file.readlines()
        return [task.strip() for task in tasks()]
    return []

#save function 
def save_task(tasks):
    with open ("task.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n") 
        
#add function 
def add_task(tasks):
    task=input ("Enter the task : ")
    tasks.append(task)
    save_task(tasks) 
    print ("Task added Successfully")


#view function 
def view_task(tasks):
        if not tasks :
            print("no tasks")
        else:
            for idx, task in enumerate(tasks):
                print(f"{idx+1}. {task}") 
                  
# del function 
def delete_task(tasks):
    view_task(tasks)
    try:
        no_of_task=int(input("Enter the no of task to delete : "))
        if 1<= no_of_task<= len(tasks):
            deleted_task=tasks.pop(no_of_task -1)
            print (f"The {deleted_task} Deleted successfully ")
        else:
            print ("invalid task num")
    except:
        print ("Enter Valid Input ")     

#main function 
def main():
   
   
    while True:
        print ("1.Add task")           
        print ("2.View task") 
        print ("3.Delete task") 
        print ("4.Exit")      
        user_input= int(input("Enter Choice(1/2/3/4)"))             
        
        if user_input == 1:
            add_task(tasks)
        elif user_input == 2:
            view_task(tasks)
        elif user_input == 3:
            delete_task(tasks)
        elif user_input == 4:
            print ("Exiting App -   Thanks")
            break
        else:
            print ("Enter valid input")        
    load_task()
# calling main
if __name__ == "__main__" :
    main()                      
