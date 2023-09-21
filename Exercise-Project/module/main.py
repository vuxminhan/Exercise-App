from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt
import numpy as np
import mediapipe as mp
import cv2
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
from calculate_angle import *
from distance_matrix import *
from extract_vid import *
from visualize_dtw import *
from save_vid import *
from dynamic_time_warping_module import *

path1 = "./Sources/viddtw1.mp4"
path2 = "./Sources/viddtw2.mp4"

mat1 = extract_vid(path1)
mat2 = extract_vid(path2)
dist_mat = distance_matrix(mat1, mat2)

path = dtw(dist_mat)

output1 = './Sources/odtw1.mp4'
output2 =  './Sources/odtw.mp4'
stop = 0

visual = visualize_dtw(path1, path2, output1, output2, path)
print(visual)