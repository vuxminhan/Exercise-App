from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt
import numpy as np
#import scipy.spatial.distance as dist
import mediapipe as mp
import cv2
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# Input: a distance matrix in which each element is distance of 2 vectors represented for 2 frames
# Output: list contains pairs of frame indexes of 2 videos
def dtw(dist_mat):
    N, M = dist_mat.shape
    cost_mat = np.zeros((N + 1, M + 1))
    for i in range(1,N+1):
        cost_mat[i, 0]  = np.inf
    for j in range(1, M+1):
        cost_mat[0, j] = np.inf
    traceback_mat = np.zeros((N,M))
    for i in range(N):
        for j in range(M):
            min_list = [cost_mat[i, j], # match = 0
                        cost_mat[i, j+1],   #insert = 1
                        cost_mat[i+1, j]]   # deletion = 2
            index_min = np.argmin(min_list)
            cost_mat[i+1,j+1] = dist_mat[i, j] + min_list[index_min]
            traceback_mat[i,j] = index_min 
    i = N-1
    j = M -1
    path = [(i,j)]
    while i > 0 or j > 0:
        tb_type = traceback_mat[i,j]
        if tb_type == 0: # đi chéo
            i = i-1
            j = j-1
        elif tb_type == 1: # đi xuống
            i = i - 1
        elif tb_type == 2: # đi ngang
            j = j - 1
    
        path.append((i,j))
    cost_mat = cost_mat[1:, 1:]
    return path[::-1]
