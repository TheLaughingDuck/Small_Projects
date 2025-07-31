'''
Module dedicated to manipulating the field. This includes eliminating
debree before it interacts and interfers with other patterns.

Should perhaps also include creating the field etc? And the ruleset?
'''
from random import randint

def Create_random_field(length):
    field = Initiate_blank(length)
    for x_pos in range(0, len(field)):
        for y_pos in range(0, len(field)):
            if (randint(1,2) == 1):
                field[x_pos][y_pos] = 1
    return field

def Initiate_blank(length):
    return [[0]*length for i in range(length)]

def Tick(field, neighbour_list):
    New_field = Initiate_blank(len(field))
    for x_pos in range(1, len(field)-1):
        for y_pos in range(1, len(field)-1):
            
            '''Count neighbours'''
            neighbours = 0
            for y in range(y_pos+1, y_pos-2, -1):
                for x in range(x_pos-1, x_pos+2, 1):
                    if ((field[x][y] == 1) and not ((x == x_pos) and (y == y_pos))):
                        neighbours += 1
                        
            '''Rules'''
            if(neighbours < 2 and field[x_pos][y_pos] == 1): #Underpopulation
                New_field[x_pos][y_pos] = 0
                #print('Under-Killed ' + '(' + str(x_pos) + ',' + str(y_pos) + ')')
            if((neighbours == 2 or neighbours == 3) and field[x_pos][y_pos] == 1): #Survivors!
                New_field[x_pos][y_pos] = 1
                #print('Survived ' + '(' + str(x_pos) + ',' + str(y_pos) + ')')
            if(neighbours == 3 and field[x_pos][y_pos] == 0): #Reproduction
                New_field[x_pos][y_pos] = 1
                #print('Birthed ' + '(' + str(x_pos) + ',' + str(y_pos) + ')')
            if(neighbours > 3): #Overpopulation
                New_field[x_pos][y_pos] = 0
                #print('Over-Killed ' + '(' + str(x_pos) + ',' + str(y_pos) + ')')
    
    '''Counting neighbours :('''
    for x_pos in range(1, len(New_field)-1):
        for y_pos in range(1, len(New_field)-1):
            neighbours = 0
            for y in range(y_pos+1, y_pos-2, -1):
                for x in range(x_pos-1, x_pos+2, 1):
                    if ((New_field[x][y] == 1) and not ((x == x_pos) and (y == y_pos))):
                        neighbours += 1
                    neighbour_list[x_pos][y_pos] = neighbours
    
    return New_field, neighbour_list

def Trimming(field):
    '''
    This function is used to call the trimming-functions I select.
    '''
    field, paint_list1 = Clear_square(field)
    field, paint_list2 = Clear_Beehive(field)
    
    paint_list1 += paint_list2
    return field, paint_list1

def Clear_square(field):
    '''
    Looks for 2x2-squares with a two-level garden and removes them.
    Currently doesn´t notice 2x2-squares on the edge or one dead cell from the
    edge. Should maybe be fixed?
    Perhaps draw something red where we the square was removed? To clarify for the
    user.
    Litar ganska mycket på att den fungerar.
    '''
    paint_list = []
    #Cycle through field
    for x_pos in range(2, len(field)-3):
        for y_pos in range(2, len(field)-3):
            #Cycle through the surrounding of what could be a square
            neighbour_list = []
            for check_x in range(x_pos-2, x_pos+4):
                for check_y in range(y_pos-2, y_pos+4):
                    neighbour_list.append(field[check_x][check_y])
            if (neighbour_list == [0,0,0,0,0,0, 0,0,0,0,0,0, 0,0,1,1,0,0, 0,0,1,1,0,0, 0,0,0,0,0,0, 0,0,0,0,0,0]):
                print('Found square on (' + str(x_pos) + ',' + str(y_pos) + ')')                
                field[x_pos][y_pos] = 0
                field[x_pos][y_pos+1] = 0
                field[x_pos+1][y_pos] = 0
                field[x_pos+1][y_pos+1] = 0
                
                paint_list.append((x_pos,y_pos))
                paint_list.append((x_pos,y_pos+1))
                paint_list.append((x_pos+1,y_pos))
                paint_list.append((x_pos+1,y_pos+1))
    return field, paint_list

def Clear_Beehive(field):
    '''
    Looks for Beehives with a two-level garden and kills them!
    Mind the rotation tho...!!!! Not fixed yet!
    Litar ganska mycket på att den fungerar.
    '''
    paint_list = []
    #Cycle through field
    for x_pos in range(2, len(field)-4):
        for y_pos in range(2, len(field)-5):
            #Cycle through the surrounding of what could be a standing Beehive
            neighbour_list = []
            for check_x in range(x_pos-2, x_pos+5):
                for check_y in range(y_pos-2, y_pos+6):
                    neighbour_list.append(field[check_x][check_y])
            if (neighbour_list == [0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,  0,0,0,1,1,0,0,0,  0,0,1,0,0,1,0,0,  0,0,0,1,1,0,0,0,  0,0,0,0,0,0,0,0,  0,0,0,0,0,0,0,0,]):
                print('Found Beehive on (' + str(x_pos) + ',' + str(y_pos) + ')')
                field[x_pos][y_pos+1] = 0
                field[x_pos][y_pos+2] = 0
                paint_list.append((x_pos,y_pos+1))
                paint_list.append((x_pos,y_pos+2))
                
                field[x_pos+1][y_pos] = 0
                field[x_pos+1][y_pos+3] = 0
                paint_list.append((x_pos+1,y_pos))
                paint_list.append((x_pos+1,y_pos+3))
                
                field[x_pos+2][y_pos+1] = 0
                field[x_pos+2][y_pos+2] = 0
                paint_list.append((x_pos+2,y_pos+1))
                paint_list.append((x_pos+2,y_pos+2))
                
    #Check for fallen beehives
    for x_pos in range(2, len(field)-5):
        for y_pos in range(2, len(field)-4):
            #Cycle through the surrounding of what could be a fallen Beehive
            neighbour_list = []
            for check_x in range(x_pos-2, x_pos+6):
                for check_y in range(y_pos-2, y_pos+5):
                    neighbour_list.append(field[check_x][check_y])
            #print(len(neighbour_list))
            if (neighbour_list == [0,0,0,0,0,0,0,  0,0,0,0,0,0,0,  0,0,0,1,0,0,0,  0,0,1,0,1,0,0,  0,0,1,0,1,0,0,  0,0,0,1,0,0,0,  0,0,0,0,0,0,0,  0,0,0,0,0,0,0]):
                print('Found fallen Beehive on (' + str(x_pos) + ',' + str(y_pos) + ')')
                field[x_pos+1][y_pos+2] = 0
                field[x_pos+2][y_pos+2] = 0
                paint_list.append((x_pos+1,y_pos+2))
                paint_list.append((x_pos+2,y_pos+2))
                
                field[x_pos][y_pos+1] = 0
                field[x_pos+3][y_pos+1] = 0
                paint_list.append((x_pos,y_pos+1))
                paint_list.append((x_pos+3,y_pos+1))
                
                field[x_pos+1][y_pos] = 0
                field[x_pos+2][y_pos] = 0
                paint_list.append((x_pos+1,y_pos))
                paint_list.append((x_pos+2,y_pos))
            
    return field, paint_list

def Clear_Boat(field):
    '''
    Looks for boats with a two-level garden and kills them!
    Mind the rotation tho...
    '''
