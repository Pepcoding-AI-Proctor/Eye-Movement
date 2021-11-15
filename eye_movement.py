import cv2
from gaze_tracking import GazeTracking

gaze = GazeTracking()

def tract_movement(frame,movement_list):
    
    gaze.refresh(frame)
    
    ll = []
    
    new_frame = gaze.annotated_frame()
    text = ""

    if(f_count % 100 == 0):
        r_true = 0

#     while(r_true < fps*5):
    if gaze.is_right():
        count1 += 1
        text = "Eye Looking right"
        ll.append(text)
    elif gaze.is_left():
        count1 += 1
        text = "Eye Looking left"
        ll.append(text)
    elif gaze.is_center():
        count1 += 1
        text = "Eye Looking center"
        ll.append(text)
    if gaze.is_upward():
        count1 += 1
        text1 = "Eye Looking Upward"
        ll.append(text1)
    elif gaze.is_downward():
        count1 += 1
        text1 = "Eye Looking Downward"
        ll.append(text1)
    else:
        count1 += 1
        text1 = "Eye Looking Straight"
        ll.append(text)
        
    movement_list.append(ll)