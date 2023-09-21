
import mediapipe as mp
import cv2
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
from calculate_angle import *
from distance_matrix import *
from extract_vid import *
from save_vid import *
from dynamic_time_warping_module import *

def highlight_angle_fun(inpath1, inpath2, path, dist_mat, mat1, mat2):
    cap1 = cv2.VideoCapture(inpath1)
    cap2 = cv2.VideoCapture(inpath2)

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
                        wrong_angle = mat2[i[1],j] - mat1[i[0],j]
                        if wrong_angle >= 20:
                            message += f'{key}: {wrong_angle}' 
                        
                    cap1.set(1,i[0])
                    cap2.set(1, i[1])  # Where frame_no is the frame you want
                    okay1  , frame1 = cap1.read()
                    okay2 , frame2 = cap2.read()
                    
                    if okay1:
                        cv2.imshow('trainer' , frame1)
                                
                    if okay2:
                        cv2.rectangle(frame2, (0,0), (130, 70), (80,30,20), -1)
                        cv2.putText(frame2, message, (20,25),2, 0.25, (250,250,250),1, lineType = cv2.LINE_AA )
                        cv2.imshow('user', frame2)
                    if not okay1 or not okay2:
                        print('Cant read the video , Exit!')
                        break

                    k = cv2.waitKey(5)
                    if k == ord('q'):
                        break 
                    
                else:
                    pass
                cv2.waitKey(0)
            
    cap1.release()
    cap2.release()

    cv2.destroyAllWindows()