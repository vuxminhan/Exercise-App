import cv2
import mediapipe as mp

def draw_bounding_box_around_body_parts(frame, body_parts_list):
    # Initialize pose and drawing utilities
    mp_pose = mp.solutions.pose
    # mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose()

    # Read the image
    frame = cv2.imread(frame)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image and get the pose landmarks
    results = pose.process(image_rgb)

    # Define body parts using landmark indices
    body_parts = {
   
                'right_elbow': [mp_pose.PoseLandmark.RIGHT_ELBOW.value],
                'left_elbow': [mp_pose.PoseLandmark.LEFT_ELBOW.value],
                'right_shoulder': [mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
                'left_shoulder': [mp_pose.PoseLandmark.LEFT_SHOULDER.value],
                'right_knee': [mp_pose.PoseLandmark.RIGHT_KNEE.value],
                'left_knee': [mp_pose.PoseLandmark.LEFT_KNEE.value],
                'right_hip': [mp_pose.PoseLandmark.RIGHT_HIP.value],
                'left_hip': [mp_pose.PoseLandmark.LEFT_HIP.value],
                'right_ankle': [mp_pose.PoseLandmark.RIGHT_ANKLE.value],
                'left_ankle': [mp_pose.PoseLandmark.LEFT_ANKLE.value]
                }

    try:
        if results.pose_landmarks:
            for body_part_name in body_parts_list:
                indices = body_parts.get(body_part_name)
                print(indices)
                if indices:
                    # body_part_coords = [(int(results.pose_landmarks.landmark[i].x * frame.shape[1]), 
                    #                     int(results.pose_landmarks.landmark[i].y * frame.shape[0])) for i in indices]
                    body_part_coords = [(results.pose_landmarks.landmark[i].x , 
                                        results.pose_landmarks.landmark[i].y) for i in indices]
                    
                    print(body_part_coords)
                    margin = 30
                    x_coords = [coord[0] for coord in body_part_coords]
                    y_coords = [coord[1] for coord in body_part_coords]
                    x_min, x_max = min(x_coords) - margin, max(x_coords) + margin
                    y_min, y_max = min(y_coords) - margin, max(y_coords) + margin

                    # Draw bounding box
                    left_color = (0, 0, 255)  # Red for left
                    right_color = (255, 0, 0)  # Blue for right

                    # Determine color based on body part name
                    if "left" in body_part_name:
                        color = left_color
                    elif "right" in body_part_name:
                        color = right_color
                    else:
                        color = (0, 255, 0)  # Default green color for other body parts

                    # Draw bounding box with the determined color
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), color, 4)
            return frame
    except:
        pass


    # Show the image
    # cv2.imshow('Body Part Bounding Box', frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# # Call the function with an image path, a point, and a list of body parts
draw_bounding_box_around_body_parts('./Sources/img.png', ['right_elbow', 'left_shoulder','left_hip'])
