#A program to keep count of shoe stock, add to the stock, find the lowest and highest quantity of a specific shoe and more.

#Setting up the Shoe class
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_code(self):
        return self.code

    def get_quantity(self):
        return self.quantity
    
    def __str__(self):
        string = (f"There are {self.quantity} {self.product}. Country: {self.country} Code: {self.code}  Cost: {self.cost} ")
        return string

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

#Function to read details of shoes from a file and add them to a list, with an error message if can't read the file or can't add to a list.
def read_shoes_data():
    try:
        with open("inventory.txt", "r+") as f:
            next(f)
            for line1 in f:
                line = line1.replace('\n', '')
                country = line.split(",")[0]
                code = line.split(",")[1]
                product = line.split(",")[2]
                cost = int(line.split(",")[3])
                quantity = int(line.split(",")[4])
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)
    except Exception:
        print("You made an error.")

#Function to allow a user to add a shoe object
def capture_shoes():
    country = input("What is the country? ")
    code = input("What is the code? ")
    product = input("What is the product? ")
    cost = input("What is the cost? ")
    quantity = input("What is the quantity? ")
    product = Shoe(country, code, product, cost, quantity)
    shoe_list.append(product)

#Fucntion to see all the shoes in the list in a friendly to read format.
#It iterates over the shoes list and prints the details of the shoes.
def view_all():
    for i in shoe_list:
        print(i.__str__())

#Function to work out the shoe with the lowest quantity and update this in the file (restocking)
def re_stock():
    smallest = min(shoe_list, key=lambda shoe: shoe.quantity)
    user =input(f"There are only {smallest.quantity} {smallest.product}s. Do you want to add this quantity of shoes? (y/n) ")
    if user == 'y':
        increased = int(input("How much do you want to increase the quantity of shoe by? "))
        current_quantity = smallest.get_quantity()
        smallest.quantity = current_quantity + increased
    with open('inventory.txt', 'w+') as f:
        f.write('Country,Code,Product,Cost,Quantity\n')
        for i in shoe_list:
            f.write(f"{i.product},{i.code},{i.product},{i.cost},{i.quantity}\n")

#Function to search for a shoe in a list based on its code and return the relevant object
def search_shoe():
    shoe_code_input = input("Please enter the code of the shoe you are looking for: ")
    for i in shoe_list:
        if shoe_code_input == i.code:
            return i

#Function to work out the value of each shoe in the list by multiplying the cost and quantity of each shoe.
def value_per_item():
    for i in shoe_list:
        value = i.quantity * i.cost
        print(f"The value of {i.product} is {value}.")

#Function to search for the shoe with the highest quantity and putting it on sale.
def highest_qty():
    high_qty = max(shoe_list, key=lambda shoe: shoe.quantity)
    print(f"{high_qty.product} is for sale.")

read_shoes_data()

'''
#==========Main Menu=============

Menu to let user interact with the program.
'''
while True:
    menu = input('''Select one of the following Options below:
    a -  Add a shoe
    va - View all shoes
    re - Restock
    se - Search for a shoe
    v -  Value per item
    sa - Sale
    e -  Exit
    : ''').lower()

    if menu == 'a':
        capture_shoes()

    elif menu == 'va':
        view_all()

    elif menu == 're':
        re_stock()

    elif menu == 'se':
        print(search_shoe())

    elif menu == 'v':
        value_per_item()

    elif menu == 'sa':
        highest_qty()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")