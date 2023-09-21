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
                cap2.set(1, i[1])
                # cap1.set(cv2.CAP_PROP_POS_MSEC,i[0])
                # cap2.set(cv2.CAP_PROP_POS_MSEC, i[1])  # Where frame_no is the frame you want
                okay1  , frame1 = cap1.read()
                okay2 , frame2 = cap2.read()
                
                if okay1:
                    # img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                    # img1.flags.writeable = False

                    # #Make detection
                    # result1 = pose.process(img1)

                    # # Back the original color channels
                    # img1.flags.writeable = True
                    # img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
                    
                    # #print(landmarks) 
                    # # try:
                    # #     landmarks = result.pose_landmarks.landmark
                    # #   
                    # # except:
                    # #     pass

                
                    # #Render detection
                    # mp_drawing.draw_landmarks(img1, result1.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    #             mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                    #             mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                    #             ) 
                    cv2.imshow('trainer' , frame1)
                    
                    output1.write(frame1)
        
                if okay2:

                    img2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                    img2.flags.writeable = False

                    #Make detection
                    result2 = pose.process(img2)

                    # Back the original color channels
                    img2.flags.writeable = True
                    img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
                
                    #Render detection
                    mp_drawing.draw_landmarks(img2, result2.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                            mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                            mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                            ) 
                    cv2.imshow('user' , img2)
                    
                    output2.write(img2)

                if not okay1 or not okay2:
                    print('Cant read the video , Exit!')
                    break

                k = cv2.waitKey(5)
                if k == ord('q'):
                    break 
                
                #cv2.waitKey(1)
            # if cv2.waitKey(1) and 0xFF == ord('q'):
            #     break
            cv2.waitKey(0)
    cap1.release()
    cap2.release()