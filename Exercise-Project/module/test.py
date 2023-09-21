import mediapipe as mp
import cv2
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

path = [1,1,2,2,2,3,4,5,6,7,8,8,8,8,8,8,9,9,10,11,12,13,14,15,16,17,18,19,20,20,21,21,21,21,22,23,24,25]
cap1 = cv2.VideoCapture("./Sources/viddtw1.mp4")
frame_height = int(cap1.get(4))
frame_width = int(cap1.get(3))
frame_size = (frame_width, frame_height)
fps = 20.0
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output1 = cv2.VideoWriter("./Sources/optest.mp4", fourcc, fps, frame_size)
with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
    while cap1.isOpened():
        for i in path:
            cap1.set(cv2.CAP_PROP_POS_MSEC,i)
            okay1, frame1 = cap1.read()
            
            if okay1:
                img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                img1.flags.writeable = False

                #Make detection
                result1 = pose.process(img1)

                # Back the original color channels
                img1.flags.writeable = True
                img1 = cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
                
                #print(landmarks) 
                # try:
                #     landmarks = result.pose_landmarks.landmark
                #   
                # except:
                #     pass

            
                #Render detection
                mp_drawing.draw_landmarks(img1, result1.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    ) 
                cv2.imshow('Mediapipe Vid', img1)             
                k = cv2.waitKey(20)
                if k == ord('q'):
                    break
                output1.write(img1)
