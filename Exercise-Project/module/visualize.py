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
from visualize import *
from save_vid import *

def visualize_dtw(inpath1, inpath2, outpath1, outpath2):
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
                message = ''
                if dist_mat[i[0],i[1]] <= 90:
                    for key in name_angle.keys():
                        j = name_angle[key]
                        if mat1[i[0],j] != mat2[i[1],j]:
                            wrong_angle = key
                            message += f'Your {key} is different from trainer + "\n" ' 
                    print(message)    
                    cap1.set(1,i[0])
                    cap2.set(1, i[1])  # Where frame_no is the frame you want
                    okay1  , frame1 = cap1.read()
                    okay2 , frame2 = cap2.read()
                    
                    if okay1:
                        # Change from BGR to RGB
                        img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                        img1.flags.writeable = False

                        #Make detection
                        result1 = pose.process(img1)

                        # Back the original color channels
                        img1.flags.writeable = True
                        img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)

                        #Extract landmarks 
                        try:
                            landmarks = result1.pose_landmarks.landmark
                            #print(landmarks)
                        except:
                            pass
                    
                        #Render detection
                        mp_drawing.draw_landmarks(img1, result1.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                                ) 
                        cv2.imshow('trainer' , img1)
                        
                        output1.write(img1)
            
                    if okay2:
                        # Change from BGR to RGB
                        img2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
                        img2.flags.writeable = False

                        #Make detection
                        result2 = pose.process(img2)

                        # Back the original color channels
                        img2.flags.writeable = True
                        img2 = cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)

                        #Extract landmarks 
                        try:
                            landmarks = result2.pose_landmarks.landmark
                            #print(landmarks)
                        except:
                            pass
                    
                        #Render detection
                        mp_drawing.draw_landmarks(img2, result2.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                                mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                                mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                                ) 
                        cv2.rectangle(img2, (0,0), (130, 70), (80,30,20), -1)
                        cv2.putText(img2, message, (20,25),2, 0.25, (250,250,250),1, lineType = cv2.LINE_AA )
                        cv2.imshow('user' , img2)
                        
                        output1.write(img2)

                    if not okay1 or not okay2:
                        print('Cant read the video , Exit!')
                        break

                    k = cv2.waitKey(20)
                    if k == ord('q'):
                        break 
                    cv2.waitKey(0)
                    #cv2.waitKey(1)
                # if cv2.waitKey(1) and 0xFF == ord('q'):
                #     break
                else:
                    pass
                cv2.waitKey(0)
            
    cap1.release()
    cap2.release()

    cv2.destroyAllWindows()