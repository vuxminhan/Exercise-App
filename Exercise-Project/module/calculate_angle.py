# Input: 3 points A, B, C
# Output: angle ABC
import numpy as np

def calculate_angle(point1, point2, point3):
    vector1 = np.array(point1) - np.array(point2)
    vector3 = np.array(point3) - np.array(point2)

    dot_product = np.dot(vector1, vector3)
    norm_product = np.linalg.norm(vector1) * np.linalg.norm(vector3)

    cosine_angle = dot_product / norm_product
    angle = np.arccos(cosine_angle)

    return np.degrees(angle)

# Dictionary of angle
def name_angle_fun():
    name_angle1 = {'right_elbow': 0, 'left_elbow': 1, 'right_shoulder': 2, 'left_shoulder': 3,
              'right_knee': 4, 'left_knee': 5, 'right_hip':6, 'left_hip': 7, 'vertical': 8}
    return name_angle1

# Các điểm tính góc
def angle_dict_fun():
    angle_dict1 = {'right_elbow': [14,15,16], 'left_elbow': [11,12,13], 'right_shoulder': [8,14,15], 'left_shoulder': [8,11,12],
              'right_knee': [1,2,3], 'left_knee': [4,5,6], 'right_hip':[0,1,2], 'left_hip': [0,4,5],  'vertical': [8,0,0]}
    return angle_dict1