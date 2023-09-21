from matplotlib.patches import ConnectionPatch
import matplotlib.pyplot as plt
import mediapipe as mp
import cv2
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
from calculate_angle import *
from distance_matrix import *
from extract_vid import *
from save_vid import *
from dynamic_time_warping_module import *

def visualize_dtw(inpath1, inpath2, outpath1, outpath2, path):
    cap1 = cv2.VideoCapture(inpath1)
    cap2 = cv2.VideoCapture(inpath2)
    output1 = save_video(inpath1, outpath1)
    output2 = save_video(inpath2, outpath2)
    stop = 0
    with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
        while cap1.isOpened() or cap2.isOpened():
            stop += 1
            if stop == 2:
                break
            for i in path:
                cap1.set(1,i[0])
                cap2.set(1, i[1])  # Where frame_no is the frame you want
                okay1  , frame1 = cap1.read()
                okay2 , frame2 = cap2.read()
                
                if okay1:
                    #hsv1 = cv2.cvtColor(frame1 , cv2.COLOR_BGR2HSV)
                    cv2.imshow('trainer' , frame1)
                    
                    output1.write(frame1)
        
                if okay2:
                    #hsv2 = cv2.cvtColor(frame2 , cv2.COLOR_BGR2HSV)
                    cv2.imshow('user' , frame2)
                    
                    output2.write(frame2)

                if not okay1 or not okay2:
                    print('Cant read the video , Exit!')
                    break

                k = cv2.waitKey(20)
                if k == ord('q'):
                    break 
                
                #cv2.waitKey(1)
            # if cv2.waitKey(1) and 0xFF == ord('q'):
            #     break
            cv2.waitKey(0)
    cap1.release()
    cap2.release()