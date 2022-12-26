#=====importing libraries===========
from datetime import date

#====Login Section====

username_input = input("Please enter your username: ")
password_input = input("Please enter your password: ")
#username_input = "admin4"
#password_input = "adm1n4"

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


while True:
    if username_input in username:
    #print("Username matches")
    position_of_username = username.index(username_input)
    if password[position_of_username] == password_input:
        print("You may enter")
#print(username)
#print(password)

#Firstly I am checking whether entered username exists in the list
#If yes, I check the position that the username is in. This enables me to match the password to the username
#I check whether the password in the given position matches the password entered
if username_input in username:
    #print("Username matches")
    position_of_username = username.index(username_input)
    if password[position_of_username] == password_input:
        print("You may enter")
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
s -  Stats
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
                #if statement added that only admin can register a user
                if username_input == "admin":                    
                    new_username = input("Please enter a new username: ")
                    new_password = input("Please enter a new password: ") 
                    new_password2 = input("Please confirm the password: ")
                    if new_password == new_password2:
                        new_user = open("user.txt", "a")
                        new_user.write(new_username + ", " + new_password + "\n")
                        new_user.close()
                    else:
                        print("The password doesn't match. Please try again.")
                else:
                    print("Sorry, only an admin can register users.")


            elif menu == 'a':
                pass
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


            elif menu == 'va':
                with open('tasks.txt', 'r+') as f:                   
                    for line in f:
                        list= line.strip()
                        #list2 = list.split(", ") #after split, I get brackets and quotation marks, how do I get rid of those? Why does that happen?
                        print(list)
                        #taskdetails = line.split(",")
                f.close()

            elif menu == 'vm':           
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
                        print(onetasklist[i])

                f.close()

            elif menu == 's' and username_input == "admin":  
                alltasks = ""
                #read the file and create string called alltasks
                with open('tasks.txt', 'r+') as f:
                    for line in f:
                        alltasks += line

                #split based on tasks so by double line \n\n
                split_tasks = alltasks.split("\n\n")
                print("There are " + str(len(split_tasks)) + " tasks.\n")
                print("There are " + str(len(username)-1) + " users.\n")

                f.close()

            elif menu == 'e':
                print('Goodbye!!!')
                exit()

            else:
                print("You have made a wrong choice, Please Try again")


    else:
        print("You have entered an incorrect password. Please try again.")
else:
    print("You have entered an invalid username. Please try again.")
    

