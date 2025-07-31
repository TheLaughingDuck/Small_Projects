import tkinter

class Windclass(): #Window-Canvas-Something-Something
    def __init__(self, Width, Height, Title):
        self.root = tkinter.Tk()
        self.width = Width
        self.height = Height
        self.w_canvas = tkinter.Canvas(self.root, width=Width, height=Height)
        self.w_canvas.pack()
        self.w_canvas.winfo_toplevel().title(Title)
        print('Initiated canvas.')
        
    def Paint_cells(self, field, neighbour_list):
        n = int(self.width / len(field))
        self.w_canvas.delete("all")
        
        '''Paint grid-lines '''
        for x in range(0, self.width, n):
            self.w_canvas.create_line(x, 0, x, self.height, fill="#476042", width=0.1)
            pass
        for y in range(0, self.height, n):
            self.w_canvas.create_line(0, y, self.width, y, fill="#476042", width=0.1)
            pass
        
        '''Paint cells'''
        for x_pos in range(0, len(field)):
            for y_pos in range(0, len(field)):
                a = x_pos * n
                b = self.height - n - y_pos * n
                #w_canvas.create_text(a + 15, b + 15,text= '(' + str(x_pos) + ',' + str(y_pos) + ')')
                if (field[x_pos][y_pos] == 1):
                    self.w_canvas.create_rectangle(a, b, a+n, b+n, fill="green") #green
                    
                dis = 10

                if (neighbour_list[x_pos][y_pos] == 8):
                    self.w_canvas.create_text(a + dis, b + dis,text= '8', fill='gray')
                if (neighbour_list[x_pos][y_pos] == 7):
                    self.w_canvas.create_text(a + dis, b + dis,text= '7', fill='black')
                if (neighbour_list[x_pos][y_pos] == 6):
                    self.w_canvas.create_text(a + dis, b + dis,text= '6', fill='turquoise')
                if (neighbour_list[x_pos][y_pos] == 5):
                    self.w_canvas.create_text(a + dis, b + dis,text= '5', fill='maroon')
                if (neighbour_list[x_pos][y_pos] == 4):
                    self.w_canvas.create_text(a + dis, b + dis,text= '4', fill='purple')
                if (neighbour_list[x_pos][y_pos] == 3):
                    self.w_canvas.create_text(a + dis, b + dis,text= '3', fill='red')
                if (neighbour_list[x_pos][y_pos] == 2):
                    self.w_canvas.create_text(a + dis, b + dis,text= '2', fill='green')
                if (neighbour_list[x_pos][y_pos] == 1):
                    self.w_canvas.create_text(a + dis, b + dis,text= '1', fill='blue')
                
                    #self.w_canvas.create_rectangle(65, 35, 135, 65, fill="yellow") #obsolete
        #print('Just painted')
    
    def Paint_Blood(self, field, point_list):
        n = int(self.width / len(field))
        for point in point_list:
            a = point[0] * n
            b = self.height - n - point[1] * n
            self.w_canvas.create_rectangle(a, b, a+n, b+n, fill="red")
    def Loop(self):
        self.root.mainloop()
        


