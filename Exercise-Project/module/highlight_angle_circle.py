
import mediapipe as mp
import cv2
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
from calculate_angle import *
from distance_matrix import *
from extract_vid import *
from save_vid import *
from dynamic_time_warping_module import *
from bound_box import *
from highlight_point import *

def highlight_angle_circle(inpath1, inpath2, path, mat1, mat2, outpath1, outpath2, array_l):
    cap1 = cv2.VideoCapture(inpath1)
    cap2 = cv2.VideoCapture(inpath2)
    # outpath1 = input(str('Enter your output path:'))
    # outpath2 = input(str('Enter your output path:'))
    output1 = save_video(inpath1, outpath1)
    output2 = save_video(inpath2, outpath2)
    stop = 0

    while cap1.isOpened() or cap2.isOpened():
        stop += 1
        if stop == 2:
            break
        for i in path:
            wrong_angle_list = []
            message = ''
            for key in name_angle.keys():
                j = name_angle[key]
                wrong_ang = abs(mat2[i[1],j] - mat1[i[0],j])
                
                if wrong_ang >= 20:
                    wrong_angle_list.append(key)
                    message += f"{key}: {wrong_ang:.2f}\n"
           
                
            cap1.set(1,i[0])
            cap2.set(1, i[1])  # Where frame_no is the frame you want
            okay1  , frame1 = cap1.read()
            okay2 , frame2 = cap2.read()
            
            if okay1:
                cv2.imshow('trainer' , frame1)
                output1.write(frame1)  

            if okay2: 
                # keypoint = array_l[i[1]]
                # for key in wrong_angle_list:
                #     frame2 = highlight_body_part_with_circle(frame2,keypoint,key)
                cv2.rectangle(frame2, (0,0), (120, 200), (80,30,20), -1)
                y0, dy = 20, 20
                for i, line in enumerate(message.split('\n')):
                    y = y0 + i*dy
                    cv2.putText(frame2, line, (10, y ),2, 0.3, (250,250,250),1, lineType = cv2.LINE_AA )     

                cv2.imshow('user', frame2)
                output2.write(frame2)
            if not okay1 or not okay2:
                print('Cant read the video , Exit!')
                break
            k = cv2.waitKey(1)
            if k == ord('q'):
                break 
                     
        cv2.waitKey(0)
            
    cap1.release()
    cap2.release()

    cv2.destroyAllWindows()