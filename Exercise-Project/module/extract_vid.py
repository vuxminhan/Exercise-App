import numpy as np
from calculate_angle import * 


name_angle = name_angle_fun()
angle_dict = angle_dict_fun()
def extract_vid(array):
    matrix = []
    for i in range(array.shape[0]):  # calculate angle
        theta = []
        for key in angle_dict.keys():                  
            if key != "vertical": 
                val = angle_dict[key]
                a = array[i][val[0]]
                b = array[i][val[1]]
                c = array[i][val[2]]
            else:
                val = angle_dict[key]
                a = array[i][val[0]]
                b = array[i][val[1]]
                c = [0,0,1]
            angle = calculate_angle(a, b, c)
            theta.append(angle)               
        matrix.append(theta)    
    return np.array(matrix)

