import cv2
from get_array_coordinates import *
def highlight_body_part_with_circle(frame, keypoints, body_part, circle_radius=10, color=(255, 255, 255)):
    """
    Highlight the specified body part using circles around the keypoints.
    """
    # Define the keypoints indices for various body parts
    angle_dict = {
        'right_elbow': [14, 15, 16],
        'left_elbow': [11, 12, 13],
        'right_shoulder': [8, 14, 15],
        'left_shoulder': [8, 11, 12],
        'right_knee': [1, 2, 3],
        'left_knee': [4, 5, 6],
        'right_hip': [0, 1, 2],
        'left_hip': [0, 4, 5],
        'vertical': [8, 0, 0]
            }
 
    # Extract keypoints for the specified body part
    body_keypoints = [keypoints[idx][:2] for idx in angle_dict[body_part]]
    #print(body_keypoints)

    # Highlight keypoints with circles
    for kp in body_keypoints:
        #print(kp)

        x = -int(kp[0] *  (frame.shape[1]))
        y = -int(kp[1] *  (frame.shape[0]))
        print(x,y)
        frame = cv2.circle(frame, (x, y), circle_radius, color, -1)
        # cv2.imshow('a', frame)
        # k = cv2.waitKey(20)
        # if k == ord('q'):
        #     break                    
        # cv2.destroyAllWindows()

    return frame
#test
path2 = "./coordinates_file/learner_X3D.npy"
array_l = get_array(path2)
inpath1 = "./Sources/row2.mp4"
cap = cv2.VideoCapture(inpath1)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = highlight_body_part_with_circle(frame, array_l[0], 'right_elbow', circle_radius=15, color=(0, 0, 255))
        cv2.imshow('trainer' , frame)
        k = cv2.waitKey(20)
        if k == ord('q'):
            break                    
        cv2.waitKey(0)
        break

def draw_boxes_around_points(image, keypoints,body_part, box_size=(20, 20), color=(0, 255, 0), thickness=2):
    angle_dict = {
        'right_elbow': [14, 15, 16],
        'left_elbow': [11, 12, 13],
        'right_shoulder': [8, 14, 15],
        'left_shoulder': [8, 11, 12],
        'right_knee': [1, 2, 3],
        'left_knee': [4, 5, 6],
        'right_hip': [0, 1, 2],
        'left_hip': [0, 4, 5],
        'vertical': [8, 0, 0]
            }
 
    # Extract keypoints for the specified body part
    body_keypoints = [keypoints[idx][:2] for idx in angle_dict[body_part]]

    # Highlight keypoints with circles
    for kp in body_keypoints:
        x, y = int(kp[0]), int(kp[1])
        half_width, half_height = box_size[0] // 2, box_size[1] // 2
        top_left = (x - half_width, y - half_height)
        bottom_right = (x + half_width, y + half_height)
        
        cv2.rectangle(image, top_left, bottom_right, color, thickness)
    return image
