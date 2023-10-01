import cv2

def save_video(vid_path, name_output):
    vid = cv2.VideoCapture(vid_path)
    frame_height = int(vid.get(4))
    frame_width = int(vid.get(3))
    frame_size = (frame_width, frame_height)
    fps = 2.0
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output = cv2.VideoWriter(name_output, fourcc, fps, frame_size)
    return output