import cv2
import  mediapipe as mp 
import numpy as np    
from mediapipe.framework.formats import landmark_pb2
import time
import pyautogui


mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands  

video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8,min_tracking_confidence = 0.5  ) as hands:
    while video.isOpened():
        _,frame = video.read()
        image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        image = cv2.flip(image,1)
        
        image_height,image_width,_ = image.shape
        results = hands.process(image)
        image = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        if results.multi_hands_landmarks:
            for num,hand in enumerate(results.multi_hands_landmarks):
                mp_drawing.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS, mp_drawing.DrawingSpecs(color = (250,44,250),thickness = 2,circle_radius=2))
            
