import os
import random
from time import sleep



dead_char = " "
live_char = "O"
n_bits_width = os.get_terminal_size()[0] #40
n_bits_height = os.get_terminal_size()[1] #40
sleep_time = 0.5 #seconds

### INITIALISE GRID

# Randomised grid
grid = [[random.randint(0,1) for i in range(n_bits_width)] for j in range(n_bits_height)]

# Test grid 1
#grid = [[0 for i in range(n_bits_width)] for j in range(n_bits_height)]
#grid[5][5] = 1
#grid[5][6] = 1
#grid[6][5] = 1
#grid[6][6] = 1


def update_grid(grid):
    # Initialise neighbour map (each cell shows the number of neighbours it has)
    #neighbour_map = [0 for i in range(n_bits_width * n_bits_height)]

    new_grid = [[0 for i in range(n_bits_width)] for j in range(n_bits_height)]

    for row in range(0, n_bits_height):
        for col in range(0, n_bits_width):
            ### COUNT NEIGHBOURS
            n_neighbours = 0

            try: n_neighbours += grid[row][col-1] # Check left neighbour
            except: pass

            try: n_neighbours += grid[row-1][col-1] # Check left top neighbour
            except: pass
            
            try: n_neighbours += grid[row-1][col] # Check top neighbour
            except: pass

            try: n_neighbours += grid[row-1][col+1] # Check right top neighbour
            except: pass

            try: n_neighbours += grid[row][col+1] # Check right neighbour
            except: pass
            
            try: n_neighbours += grid[row+1][col+1] # Check right bottom neighbour
            except: pass

            try: n_neighbours += grid[row+1][col] # Check bottom neighbour
            except: pass
            
            try: n_neighbours += grid[row+1][col-1] # Check left bottom neighbour
            except: pass

            #print(n_neighbours)

            #neighbour_grid[row][col] = n_neighbours
            
            ### APPLY RULES
            if grid[row][col] == 0: # dead
                if n_neighbours == 3:
                    new_grid[row][col] = 1
            else: # alive
                if n_neighbours in [2,3]: # under or overpopulate
                    new_grid[row][col] = 1
                else:
                    new_grid[row][col] = 0

    return(new_grid)


def cls(n=0):
    if n == 0:
        os.system("cls")
        #print("\b"*n_bits_height*n_bits_width)
    else:
        print("\b" * (n_bits_width+1) * n_bits_height)
        print("\b" * 50) #? how many ?
    #https://stackoverflow.com/questions/34828142/cmd-console-game-reduction-of-blinking


### GAME OF LIFE LOOP
cls(0)
while True:
    # Draw grid
    sleep(sleep_time)
    #os.system("cls")
    cls()
    grid_string = ""
    for row in range(0, n_bits_height):
        for col in range(0, n_bits_width):
            #one_row += str(grid[row][col])
            grid_string += [dead_char, live_char][grid[row][col]]
        grid_string += "\n"
            
    print(grid_string)

    # Calculate and print percentage covered
    perc_covered = 100*sum(sum(x) if isinstance(x, list) else x for x in grid )/(n_bits_height * n_bits_width)
    print("Percentage covered:", round(perc_covered,1), "%")


    # Update grid (placeholder for now)
    #grid = [random.randint(0,1) for i in range(n_bits_width * n_bits_height)]
    #grid = [[random.randint(0,1) for i in range(n_bits_width)] for j in range(n_bits_height)]
    grid = update_grid(grid)



