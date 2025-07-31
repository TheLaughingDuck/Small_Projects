import Main_files.Windmodule as Windmodule

neighbours = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

def change_format(original_list):
    
    ret_list = []
    mini_list = []
    for i in range(5):
        for j in range(5):
            mini_list.append(original_list.pop(0))
        #print('mini_list: ', mini_list)
        ret_list.append(mini_list)
        mini_list = []
    print(ret_list)
    return(ret_list)


beta_list = [

]

for parent in range(0, len(beta_list)):
    beta_list[parent] = change_format(beta_list[parent])
    
    beta_canvas = Windmodule.Windclass(600, 600, 'Hell world')

    beta_canvas.Paint_cells(beta_list[parent], neighbours)

    beta_canvas.Loop()

























    