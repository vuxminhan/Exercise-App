import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
from calculate_angle import *
from distance_matrix import *
from extract_vid import *
from visualize_dtw import *
from save_vid import *
from dynamic_time_warping_module import *
from highlight_angle import *
from get_path import *
from get_array_coordinates import *
from highlight_angle_box import *
from highlight_angle_circle import *

path1 = "./coordinates_file/trainer_X3D.npy"
path2 = "./coordinates_file/learner_X3D.npy"

array_t = get_array(path1)
array_l = get_array(path2)

inpath1 = "./Sources/row1.mp4"
inpath2 = "./Sources/row2.mp4"

mat1 = extract_vid(array_t)
mat2 = extract_vid(array_l)
dist_mat = distance_matrix(mat1, mat2)
path = dtw(dist_mat)

path_dtw = get_path1(path)

output1 = './Sources/odtw13Dbox.mp4'
output2 =  './Sources/odtw23Dbox.mp4'
stop = 0

#visual = visualize_dtw(inpath1, inpath2, path_n)
visual = highlight_angle_circle(inpath1, inpath2,path_dtw, mat1, mat2, output1, output2, array_l)
#visual = highlight_angle_box(inpath1, inpath2,path_dtw, mat1, mat2, output1, output2)