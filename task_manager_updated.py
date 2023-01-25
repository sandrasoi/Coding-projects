#=====importing libraries===========
from datetime import date
import datetime
import re
import os

#====Login Section====

#username_input = "admin"
#password_input = "adm1n"

#Reading the usernames and passwords from a text file and splitting it into a list
user_file = open("user.txt", 'r+')
user_text2 = user_file.read()
user_text = user_text2.replace('\n', ', ')
userdetails = user_text.split(', ')
user_file.close()

#I am appending all usernames to one list and all passwords to one list
#They are separated on the basis that the usernames are in even positions, therefore when dividing their position by 2, it gives remainder 0
#Passwords are odd therefore have a remainder when dividing by 2

username = []
password = []

for i in range(len(userdetails)):
    if i%2 == 0:
        #print(i)
        username.append(userdetails[i])
    else:
        password.append(userdetails[i])

#print(username)
#print(password)

#Firstly I am checking whether entered username exists in the list
#If yes, I check the position that the username is in. This enables me to match the password to the username
#I check whether the password in the given position matches the password entered
username_input = input("Please enter your username: ")
password_input = input("Please enter your password: ") 

while True:
    if username_input in username:
        position_of_username = username.index(username_input)
        if password[position_of_username] == password_input:
            print("You may enter. \n")
            break
        else:
            #print("You have entered an incorrect password. Please try again.")
            password_input = input("You have entered an incorrect password. Please try again: ")        
    else:
        #print("You have entered an invalid username. Please try again.")
        username_input = input("You have entered an invalid username. Please try again: ")

#functions
def reg_user():
    if username_input == "admin":  
        while True:
            new_username = input("Please enter a new username: ")
            if new_username in username:
                print("You have entered a pre-existing username. Please try again.")
            else:
                break
        new_password = input("Please enter a new password: ") 
        new_password2 = input("Please confirm the password: ")
        if new_password == new_password2:
            new_user = open("user.txt", "a")
            new_user.write(new_username + ", " + new_password + "\n")
            new_user.close()
            print("Thank you, the new user has been registered.")
        else:
            print("The password doesn't match. Please try again.")
    else:
        print("Sorry, only an admin can register users.")

def add_task():
    username = input("Please enter the name of the person this task belongs to: ")
    title = input("Please enter the title of the task: ")
    description = input("Please enter a description of the task: ")
    duedate = input("Please enter the due date of the task: ")
    today = date.today()
    new_task = open("tasks.txt", "a")

    new_task.write(
            "\n\nTask:              "+ title + "\n" 
            "Assigned to:       "+ username + "\n" 
            "Date assigned:     " + str(today) + "\n" 
            "Due date:          "+ duedate + "\n" 
            "Task complete?     "+ "No" + "\n" 
            "Task description:  "+ description
            + "\n_____________________________________")  

    new_task.close()

def view_all():
    with open('tasks.txt', 'r+') as f:                   
        for line in f:
            list= line.strip()
            print(list)
    f.close()


def view_mine():
    alltasks = ""
    #read the file and create string called alltasks
    with open('tasks.txt', 'r+') as f:
        for line in f:
            alltasks += line

    #split based on tasks so by double line \n\n
    split_tasks = alltasks.split("\n\n")
    onetasklist = []
    for i in range(len(split_tasks)):
        onetasklist.append(split_tasks[i])

    #iterate through all tasks, and if that task contains the username, then print the task
    for i in range(len(onetasklist)):
        if username_input in onetasklist[i]:
            print('\n')
            print(i)
            print(onetasklist[i])
    f.close()

    #Request user to select a specific task so it can be edited.
    #User can edit the user assigned, the due date and mark it as completed
    #Make changes to the tasks.txt file according to the selected changes

    selected_task = int(input("Please select a task you would like to view. To return to main menu, please type -1: "))
    print(f"Thank you. You selected: \n")
    print(onetasklist[selected_task])
    if selected_task >= 0:
        edit_or_compelete = int(input("Would you like to edit the task or mark it as complete? Please choose 1 or 2: "))
        if edit_or_compelete == 1 and 'No' in onetasklist[selected_task]:
            print("You chose to edit your task. \n")
            assignedto = input("If you would like to change who the task is assigned to, type the new user or type No: ")
            if assignedto == 'No':
                pass
            else:
                onetasklist[selected_task] = onetasklist[selected_task].replace(username_input, assignedto)
                print('\n' + onetasklist[selected_task].replace(username_input, assignedto))
            newdate = input("If you would like to change the due date of the task, type the new date or type No: ")
            match = re.search('          (.*)\nTask complete?', onetasklist[selected_task])
            match_one = match.group(1)
            if newdate == "No":
                pass
            else:
                print('\n' + onetasklist[selected_task].replace(match_one, newdate))
                onetasklist[selected_task] = onetasklist[selected_task].replace(match_one, newdate)
            print("Thank you. Your changes have been made.")
                
            print(re.search('   (.*)Due date', onetasklist[selected_task]))
        elif edit_or_compelete == 2:
            print("You chose to mark your task as completed. \n")
            complete = input("If you would like to mark the task as complete, type Yes, otherwise type No. ")
            if complete == 'Yes':
                print('\n' + onetasklist[selected_task].replace('No', 'Yes'))
                onetasklist[selected_task] = onetasklist[selected_task].replace('No', 'Yes')
                print("Thank you. Your changes have been made.")
        else:
            print("This task is already completed or you made a wrong choice.")    
        
        with open('tasks.txt', 'w+') as f:
            for i in onetasklist:
                f.write(i +"\n\n")
    else:
        pass

#This function generates 2 reports, task_overview and user_overview

def gr():
    alltasks = ""
    with open('tasks.txt', 'r+') as f:
        for line in f:
            alltasks += line
    #split based on tasks so by double line \n\n
    split_tasks = alltasks.split("\n\n")
    f.close()

    #This loop iterates through each task and increases a count if the task is completed or uncompleted.
    count_completed = 0
    count_uncompleted = 0
    for i in range(len(split_tasks)):
        if 'Yes' in split_tasks[i]:
            count_completed += 1
        elif 'No' in split_tasks[i]:
            count_uncompleted += 1
    
    #This loop iterates through each task and increases a count if the task is overdue.
    #First I had to find strings that corresponded to the due date, then I compared the date due and the date assigned, if it was overdue, I increased the overdue count 
    overdue = 0
    for i in range(len(split_tasks)):
        date_assigned = (re.search('     (.*)\nDue date', split_tasks[i])).group(1)
        date_due = (re.search('          (.*)\nTask complete?', split_tasks[i])).group(1)
        
        d1 = datetime.datetime.strptime(date_assigned, "%Y-%m-%d").date()
        d2 = datetime.datetime.strptime(date_due, "%Y-%m-%d").date()
        if d1 > d2:
            overdue += 1

    #Assigning variables for each stat neccessary
    num_tasks = str(len(split_tasks))
    completed_tasks = str(count_completed)
    uncompleted_tasks = str(count_uncompleted)
    overdue_tasks = str(overdue)
    percentage_incomplete = str(round((count_uncompleted/len(split_tasks))*100, 2)) + " %"
    percentage_overdue = str(round((overdue/len(split_tasks))*100,2)) + " %"

    #Writing all the stats to a file
    with open('task_overview.txt', 'w+') as f:
        f.write(f'''Number of tasks is:                 {num_tasks}
Number of completed tasks is:       {completed_tasks}
Number of uncompleted tasks is:     {uncompleted_tasks}
Number of overdue tasks is:         {overdue_tasks}
Percetage of incomplete tasks is:   {percentage_incomplete}
Percentage of overdue tasks is:     {percentage_overdue}.''')

    f.close()

#This section creates a file user_overview to show the number of tasks and users, and what tasks each user has and what is completed and what is not
#I looped through each user and then looped through each task to get the relevant information
    full_report = f'''The total number of users is:                                                  {str(len(username))}
The total number of tasks is:                                                  {num_tasks}\n\n'''

    for name in username:
        totaltasks = 0
        completedtasks = 0
        uncompletedtasks = 0
        overdue = 0
        for task in range(len(split_tasks)):
            date_assigned = (re.search('     (.*)\nDue date', split_tasks[task])).group(1)
            date_due = (re.search('          (.*)\nTask complete?', split_tasks[task])).group(1)
            d1 = datetime.datetime.strptime(date_assigned, "%Y-%m-%d").date()
            d2 = datetime.datetime.strptime(date_due, "%Y-%m-%d").date()
            if d1 > d2 and 'No' in split_tasks[task] and name in split_tasks[task]:
                overdue += 1
            if name in split_tasks[task]:
                totaltasks += 1
            if 'Yes' in split_tasks[task] and name in split_tasks[task]:
                completedtasks += 1
            if 'No' in split_tasks[task] and name in split_tasks[task]:
                uncompletedtasks += 1

        full_report += f'''
Total number of tasks assigned to {name} is:                                    {str(totaltasks)}
Percentage of tasks assigned to {name} is:                                      {str(round(totaltasks/len(split_tasks)*100,2))} %
Percentage of tasks assigned to {name} that have been completed is:             {str(round(completedtasks/totaltasks*100,2))} %
Percentage of tasks assigned to {name} that have not been completed is:         {str(round(uncompletedtasks/totaltasks*100,2))} %
Percentage of tasks assigned to {name} that are not completed and overdue is:   {str(round(overdue/totaltasks*100,2))} %\n\n'''

    with open('user_overview.txt', 'w+') as f:
            f.write(full_report)
    f.close()

#This function reads the file user_overview, puts it into a string and prints it out
def generatestats():
    overview_users = ""
    #read the file and create string called overview_users
    with open('user_overview.txt', 'r+') as f:
        for line in f:
            overview_users += line

    #split based on paragraphs so by double line \n\n
    split_overview_users = overview_users.split("\n\n")

    for task in split_overview_users:
        print(task)
    f.close()

#This function reads the file task_overview, puts it into a string and prints it out
def generatestats2():
    displaystats = ""
    #read the file and create string called displaystats
    with open('task_overview.txt', 'r+') as f:
        for line in f:
            displaystats += line

    #split based on each line so by double line \n
    split_displaystats = displaystats.split("\n")

    for task in split_displaystats:
        print(task)
    print("\n")
while True:
#presenting the menu to the user and 
# making sure that the user input is coneverted to lower case.
#if the user is admin, also display 'stats' option
    if username_input == "admin":
        menu = input('''Select one of the following Options below:
r -  Registering a user
a -  Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics
e -  Exit
: ''').lower()
    else:
        menu = input('''Select one of the following Options below:
r -  Registering a user
a -  Adding a task
va - View all tasks
vm - view my task
e -  Exit
: ''').lower()
    if menu == 'r':
        reg_user()
        
    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm': 
        view_mine()          

    elif menu == 'gr' and username_input == "admin":
        gr() 

    elif menu == 'ds' and username_input == "admin":
        path = 'user_overview.txt'
        isFile = os.path.exists(path)
        if isFile == False:
            gr()
            generatestats()
            generatestats2()
        else:
            generatestats()
            generatestats2()
            
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


    

