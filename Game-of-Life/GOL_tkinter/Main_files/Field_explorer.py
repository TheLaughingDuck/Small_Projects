import random
import sys
'''
Everything related to exploring the field.

Will be able to backtrack(sort of) and find chains and cycles etc. In my
dreams at least.

Works, sort of, has found about 13 parents to the ring. Most of them not very
interesting, but a few are!

Next step;

1) search for ring-parents again, but with a 2-level garden!

2) Search for parents to the ring-parents!


'''

ring_parent_catalogue = [
   
]




                   
def Find_ring(field, parent): #Works! #But what do we do when we´re done    
    for x_pos in range(2, len(field)-2):
        for y_pos in range(2, len(field)-2):
            #Now cycle through the surrounding of what could be a ring
            neighbour_list = []
            for check_x in range(x_pos-2, x_pos+3):
                for check_y in range(y_pos-2, y_pos+3):
                    neighbour_list.append(field[check_x][check_y])
            if (neighbour_list == [0,0,0,0,0, 0,1,1,1,0, 0,1,0,1,0, 0,1,1,1,0, 0,0,0,0,0]):
                print('found RING on (' + str(x_pos) + ',' + str(y_pos) + ')')
                
                '''Finds the local parent in the same area that the ring we found occupies'''
                local_parent = []
                for check_x in range(x_pos-2, x_pos+3):
                    for check_y in range(y_pos-2, y_pos+3):
                        if (parent[check_x][check_y] == 1):
                            local_parent.append(1)
                        if (parent[check_x][check_y] == 0):
                            local_parent.append(0)
                            
                            
                if (local_parent in ring_parent_catalogue):
                    pass
                    #print('found uninteresting ring-parent')
                else:
                    print('found INTERESTING ring-parent')
                    with open ('ring_parent.txt', 'a') as file:
                        file.write('found RING on (' + str(x_pos) + ',' + str(y_pos) + ') \n')
                        file.write(str(local_parent) + '\n \n')



                