import numpy as np
from extract_vid import *

#Input: 2 matrix are represented for 2 videos
def distance_matrix(mat1, mat2):
    N = mat1.shape[0]
    M = mat2.shape[0]
    dist_mat = np.zeros((N,M))
    for i in range(N):
        for j in range(M):
            dist_mat[i, j] = np.linalg.norm(mat1[i, :] - mat2[j,:] )
    return dist_mat


    