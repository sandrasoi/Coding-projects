#Mine sweeper program
#This program takes an input containing the location of bombs and outputs the location of bombs and the number of bombs that are directly next to a certain position

#First create an empty 5 by 5 grid that will be populated
number_of_rows = 5
number_of_columns = 5
mine_output = [[None] * number_of_columns for _ in range(number_of_rows)]

mine_input = []
mine_input5 = []
mine_input6 = []

print('''You will be asked to create a mine sweeper grid.
This will be a 5 by 5 grid. You will be asked to input each line of the grid invidually.
Bomb is presented as # and no bomb as -.
Please seperate your input using only a comma, e.g. "-,-,-,#,#". ''')

mine_input1 = (input("Please input the first line of a 5 by 5 grid containing bombs and -: ")).split(",")
mine_input2 = (input("Please input the second line of a 5 by 5 grid containing bombs and -: ")).split(",")
mine_input3 = (input("Please input the third line of a 5 by 5 grid containing bombs and -: ")).split(",")
mine_input4 = (input("Please input the fourth line of a 5 by 5 grid containing bombs and -: ")).split(",")
mine_input5 = (input("Please input the fifth line of a 5 by 5 grid containing bombs and -: ")).split(",")


mine_input = [mine_input1, mine_input2, mine_input3, mine_input4, mine_input5]

'''mine_input = [["-","-","-","#","#"],
            ["-", "#","-","-","-"],
            ["-","-","#","-","-"],
            ["-","#","#","-","-"],
            ["-","-","-","-","-"]]'''


#For loop checks each position and the 8 surrounding positions
#If the position is out of bound, there is no check
#Otherwise, it checks if there is a bomb in that position and it creates the number of mines counter
for position, row in enumerate(mine_input, start=0):
    print()
    for count, col in enumerate(row, start=0):
        number_of_mines = 0        
        if mine_input[position][count] == "#":
            mine_output[position][count] = "#"
        else:
            if (position-1>=0 and position-1 <=4) and (count-1>=0 and count-1 <=4):
                if mine_input[position-1][count-1] == "#":
                    number_of_mines += 1
            #N
            if (position-1>=0 and position-1 <=4) and (count>=0 and count <=4):
                if mine_input[position-1][count] == "#":
                    number_of_mines += 1
            #NE
            if (position-1>=0 and position-1 <=4) and (count+1>=0 and count+1 <=4):
                if mine_input[position-1][count+1] == "#":
                    number_of_mines += 1
            #W
            if (position>=0 and position <=4) and (count-1>=0 and count-1 <=4):
                if mine_input[position][count-1] == "#":
                    number_of_mines += 1
            #E
            if (position>=0 and position <=4) and (count+1>=0 and count+1 <=4):
                if mine_input[position][count+1] == "#":
                    number_of_mines += 1
            #SW
            if (position+1>=0 and position+1 <=4) and (count-1>=0 and count-1 <=4):
                if mine_input[position+1][count-1] == "#":
                    number_of_mines += 1
            #S
            if (position+1>=0 and position+1 <=4) and (count>=0 and count <=4):
                if mine_input[position+1][count] == "#":
                    number_of_mines += 1
            #SE
            if (position+1>=0 and position+1 <=4) and (count+1>=0 and count+1 <=4):
                if mine_input[position+1][count+1] == "#":
                    number_of_mines += 1                

            mine_output[position][count] = str(number_of_mines)
     
print(mine_output)

