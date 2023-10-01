from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt
import mediapipe as mp
import cv2

from calculate_angle import *
from distance_matrix import *
from extract_vid import *
from save_vid import *
from dynamic_time_warping_module import *

def visualize_dtw(inpath1, inpath2, path):
    cap1 = cv2.VideoCapture(inpath1)
    cap2 = cv2.VideoCapture(inpath2)
    stop = 0
   
    while cap1.isOpened() or cap2.isOpened():
        stop += 1
        if stop == 2:
            break
        for i in path:
            cap1.set(1,i[0])
            cap2.set(1, i[1])
            okay1  , frame1 = cap1.read()
            okay2 , frame2 = cap2.read()
            
            if okay1:
                cv2.imshow('trainer' , frame1)
    
            if okay2:
                cv2.imshow('user' , frame2)
                
            if not okay1 or not okay2:
                print('Cant read the video , Exit!')
                break

            k = cv2.waitKey(5)
            if k == ord('q'):
                break 

        cv2.waitKey(0)
    cap1.release()
    cap2.release()