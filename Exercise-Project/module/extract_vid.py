import numpy as np
from calculate_angle import * 
import mediapipe as mp
import cv2
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

name_angle = name_angle_fun()
angle_dict = angle_dict_fun()
def extract_vid(vid_path):
    cap = cv2.VideoCapture(vid_path)
    N = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    matrix = []
    count = 0
    with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
        while(cap.isOpened()):
            try:
                ret, frame = cap.read()
                count += 1
                #Change from BGR to RGB
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
                img.flags.writeable = False

                #Make detection
                result = pose.process(img)

                # Back the original color channels
                img.flags.writeable = True
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

                #Extract landmarks 
                try:
                    landmarks = result.pose_landmarks.landmark
                    #print(landmarks)
                except:
                    pass
                #Landmarks: là 1 list chứa tọa độ 33 điểm trên cơ thể
                #Render detection
                # mp_drawing.draw_landmarks(img, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                #                 mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                #                 mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                #                 ) 
                # cv2.imshow('Mediapipe Vid', img)             
                # k = cv2.waitKey(20)
                # if k == ord('q'):
                #     break

                theta = []
        
                # calculate angle
                for key in angle_dict.keys():                  
                    if key != "vertical": 
                        val = angle_dict[key]
                        a = [landmarks[val[0]].x, landmarks[val[0]].y]
                        b = [landmarks[val[1]].x, landmarks[val[1]].y]
                        c = [landmarks[val[2]].x, landmarks[val[2]].y]
                    else:
                        val = angle_dict[key]
                        a = [landmarks[val[0]].x, landmarks[val[0]].y]
                        b = [landmarks[val[1]].x, landmarks[val[1]].y]
                        c = [landmarks[val[1]].x, 0]
                    angle = calculate_angle(a, b, c)
                    theta.append(angle)               
                matrix.append(theta)

            except:
                pass
            if count == N:
                break
        
        return np.array(matrix)

