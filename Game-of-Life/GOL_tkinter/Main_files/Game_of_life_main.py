import Field_operator as Field_operator
import Field_explorer as Field_explorer
import Windmodule as Windmodule

import time
import sys


def U_Interface_V3():
    '''
    Intended to be an even more updated version of the original UI function.

    Current BUGS:
    The built-in forced exits will not work immediately, but will instead send the user
    onwards down to the next setting (when doing manual settings). This means the user
    will AT MOST have to press the ENTER key 7 times before the program exits. 
    '''
    
    ## Time Keeping for entire program
    global start_time
    start_time = time.time()

    ## UI Keeping track of stuff
    trials = 3 #User has 3 trials for each input-step
    completed = False
    consecutive_inputs = 0

    ## START of UI
    print("Program Initiating.")
    print("Please follow the simple setup procedure below :)")

    print('-----')
    print('Choose settings: "default" or "manual". (Recommended: "default").')
    while trials != 0 and completed == False:
        setup = input(">>")
        if(setup == "default" or setup == "def" or setup == ""):
            print("-----")
            print('Default settings selected.')
            Width = 600
            Height = 600
            length = 30
            Trimming = False

            completed = True #Exit outer while loop
        elif(setup == "manual" or setup == "man"):
            print("-----")
            print("Manual settings selected.")
            
            ## Width and Height
            trials = 3
            while trials != 0 and completed == False:
                print('-----')
                print('Please Input Width and Height. (Recommended: 600)')
                try:
                    Width = input(">>")
                    Height = Width

                    # Exit program
                    if(Width == ""):
                        consecutive_inputs += 1
                        if(consecutive_inputs >= 3):
                            print('-----')
                            print('Forced program exit')
                            print("(3 consecutive empty inputs)")
                            sys.exit("(3 consecutive empty inputs)")
                    else:
                        consecutive_inputs = 0

                        Width = int(Width)
                        Height = Width
                    
                    # Check Width input
                    if(Width < 0):
                        raise Exception()
                    
                    completed = True
                except:
                    print("An input-error occurred. Please try again.")
                    trials -= 1
            
            if(trials == 0):
                Width = 600
                Height = 600
                print("Number of trials (3) exceeded. \nDefault width and height (600) selected.")
            

            ## Square length
            trials = 3
            completed = False
            while trials != 0 and completed == False:
                print('-----')
                print('Input number of squares per side. (Recommended: 30).')
                try:
                    length = input(">>")

                    # Exit program
                    if(length == ""):
                        consecutive_inputs += 1
                        if(consecutive_inputs >= 3):
                            print('-----')
                            print('Forced program exit')
                            print("(3 consecutive empty inputs)")
                            sys.exit("(3 consecutive empty inputs)")
                    else:
                        consecutive_inputs = 0

                        length = int(length)
                    
                    # Check length input
                    if(length < 0):
                        raise Exception()
                    
                    completed = True
                except:
                    print("An input-error occurred. Please try again.")
                    trials -= 1
            
            if(trials == 0):
                length = 30
                print("Number of trials (3) exceeded. \nDefault number of squares (30) selected.")
            

            ## Trimming
            trials = 3
            completed = False
            while trials != 0 and completed == False:
                print('-----')
                print('Input trimming setting: "yes" or "no". (Recommended: "no")')
                Trimming = input(">>")

                # Exit program
                if(Trimming == ""):
                    consecutive_inputs += 1
                    if(consecutive_inputs >= 3):
                        print('-----')
                        print('Forced program exit')
                        print("(3 consecutive empty inputs)")
                        sys.exit("(3 consecutive empty inputs)")
                else:
                    consecutive_inputs = 0
                
                # Check Trimming input
                if(Trimming == "yes" or Trimming == "Trim"):
                    Trimming = True
                    completed = True
                elif(Trimming == "no" or Trimming == "notrim"):
                    Trimming == False
                    completed = True
                else:
                    print("An input-error occurred. Please try again.")
                    trials -= 1
            
            if(trials == 0):
                Trimming = False
                print('Number of trials (3) exceeded. \nDefault trimming setting ("no") filled in.')


            completed = True #Exit outer while loop
        else:
            print("An input-error occurred. Please try again.")
            trials -= 1
    
    if(trials == 0):
        print("Number of trials (3) exceeded. \nDefault settings selected.")
        

    print('-----')
    print("Setup completed!")
    ## END of UI: Perform various outputs
    main_sheet = Field_operator.Create_random_field(length)
    Windcan = Windmodule.Windclass(Width, Height, "Simply: life")
    return main_sheet, Windcan, Trimming


main_sheet, Windcan, Trimming = U_Interface_V3()
neighbour_list = Field_operator.Initiate_blank(30)
parent = main_sheet


            
def move():
    global parent
    global main_sheet
    global neighbour_list
    global start_time
    
    Windcan.Paint_cells(main_sheet, neighbour_list) #I don't wanna paint the cells!!!
    
    if Trimming == True:
        smain_sheet, paint_list = Field_operator.Trimming(main_sheet)
        Windcan.Paint_Blood(main_sheet, paint_list)
        
    #Field_explorer.Find_ring(main_sheet, parent)
    
    parent = main_sheet
    
    end_time = time.time()
    
    if (end_time - start_time >= 10):
        start_time = time.time()
        main_sheet = Field_operator.Create_random_field(30)
    
    #Last thing -->
    main_sheet, neighbour_list = Field_operator.Tick(main_sheet, neighbour_list)
    Windcan.w_canvas.after(1, move)

move()
Windcan.root.mainloop()


'''IDEAS
1) Build another module for editing the canvas using the mouse. The module
    should have a next-button that ticks the program forwards and the program
    should show 1,2 or 3 windows of what will happen to the pattern in the
    coming generations.
2) 

'''
