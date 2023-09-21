# Input: 3 points A, B, C
# Output: angle ABC
import numpy as np
def calculate_angle(a,b,c):
    a, b, c = np.array(a), np.array(b),  np.array(c)

    radians = np.arctan2(c[1]- b[1], c[0]-b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180/np.pi)
    if angle > 180:
        angle = 360 - 180
    return angle

# Dictionary of angle
def name_angle_fun():
    name_angle1 = {'right_elbow': 0, 'left_elbow': 1, 'right_shoulder': 2, 'left_shoulder': 3,
              'right_knee': 4, 'left_knee': 5, 'right_hip':6, 'left_hip': 7, 'right_ankle': 8,
              'left_ankle': 9, 'vertical': 10}
    return name_angle1

# Các điểm tính góc
def angle_dict_fun():
    angle_dict1 = {'right_elbow': [12,14,16], 'left_elbow': [11,13,15], 'right_shoulder': [14,12,24], 'left_shoulder': [13,11,23],
              'right_knee': [24,26,28], 'left_knee': [23,25,29], 'right_hip':[12,24,26], 'left_hip': [11,23,25], 'right_ankle': [26,28,32],
              'left_ankle': [25,27,31], 'vertical': [12,24,24]}
    return angle_dict1