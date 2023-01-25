#Program for an Email simualation using a class
#Email has certain attributes and functions including whether it's spam or has been read

class Email:
    def __init__(self, from_address, email_contents):       
        self.email_contents = email_contents
        self.from_address = from_address
        self.has_been_read = False
        self.is_spam = False 
        
    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

    def __str__(self):
        return self.from_address + ' ' + self.email_contents

    def get_is_spam(self):
        return self.is_spam


#inbox = [["email@yahoo.com","One email"], ["email2@yahoo.com","Two email"]]

#Functions to add an email, get number of emails, read the emails, mark them as spam or delete them
inbox = []

def add_email(email_contents, from_address):
    new_email = Email(email_contents, from_address)
    inbox.append(new_email)

#add_email("email@yahoo.com","One email")
#add_email("email2@yahoo.com","Two email")

def get_count():
    return len(inbox)

def get_email(i):
    inbox[i].mark_as_read()
    return inbox[i]

def get_unread_emails():
    unread = []
    for i in inbox:
        if i.has_been_read == False:
            unread.append(i)
    return unread

def get_spam_emails():
    spam = []
    for i in inbox:
        if i.is_spam == True:
            spam.append(i)
    return spam    

def delete(email):
    inbox.remove(email)

#User input to determine which function gets executed
#Choose a specific email based on a number from 0 to the total number of emails  minus 1

user_choice = input("What would you like to do - view/read/mark spam/send/delete/quit? ")

while user_choice != "quit":
    if user_choice == "view":
        total = get_count()
        print(f"There is a total of {total} emails in the inbox.")
        read_choice = input("Would you like to read unread or spam emails? Please type unread or spam: ")
        if read_choice == "unread":
            for i in get_unread_emails():
                print(i)
        elif read_choice == "spam":
            for i in get_spam_emails():
                print(i)
        else:
            print("Wrong choice.") 
    elif user_choice == "read":
        chosen_email = int(input(f"Please choose one email from the inbox to mark as read, from 0 to {get_count()-1}: "))
        print(get_email(chosen_email))   
    elif user_choice == "mark spam":
        chosen_spam = int(input(f"Please choose one email from the inbox to mark as spam, from 0 to {get_count()-1}: "))
        inbox[chosen_spam].mark_as_spam()
    elif user_choice == "send":
        from_email = input("Please type in the email address the email is from: ")
        content = input("Please type the content of the email : ")
        add_email(from_email,content)
    elif user_choice == "delete":
        chosen_delete = int(input(f"Please choose one email from the inbox to delete, from 0 to {get_count()-1}: "))
        print(delete(chosen_delete))           
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
    print('\n')
    user_choice = input("What would you like to do - view/read/mark spam/send/delete/quit? ")
