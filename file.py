import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import pyautogui as pag                 
pag.FAILSAFE= True 
# if FAILSAFE is enabled then if anything wrong goes with the program, it can be aborted if the mouse is dragged to any four corners of the monitor. Though FAILSAFE is enabled by default but if it is set to 'False' then it will not raise any exception

detector = HandDetector(detectionCon=0.8, maxHands=1)

time.sleep(4.0)

# In cv2.VideoCapture the argument 0 implies that we are using the webcam of the current device
# Alternatively camera of other devices can be used too. In that case the IP address of the camera needs to be passsed as an argument
video = cv2.VideoCapture(0)


while True:
    ret, frame=video.read()
    hands, img=detector.findHands(frame)
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (300, 425), (50, 50, 255), -2)
    if hands:
        lmlst=hands[0]
        fingerUp=detector.fingersUp(lmlst)
        print(fingerUp)
        # if the configuration of the hands is a closed fist -> no fingers are up then it is not going to press any key
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'Finger Count: 0', (20, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'RUN', (420, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)   

        # if fingers count detected by cvzone is -> 1 <= fingerUp < 5   then it  presses 'space' key                       
        if fingerUp == [0, 1, 0, 0, 0]:
            cv2.putText(frame, 'Finger Count: 1', (20, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'JUMP', (420, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)  
            pag.press('space')                                               
        if fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, 'Finger Count: 2', (20, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'JUMP', (420, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)     
            pag.press('space')                                            
        if fingerUp == [0, 1, 1, 1, 0]:
            cv2.putText(frame, 'Finger Count: 3', (20, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'JUMP', (420, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
            pag.press('space')                                                 
        if fingerUp == [0, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger Count: 4', (20, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'JUMP', (420, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)  
            pag.press('space')      

         # if all fingers are up then pyautogui presses 'down' key and then it is going to release the 'down' key                                             
        if fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger Count: 5', (20, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
            cv2.putText(frame, 'DUCK', (420, 460), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1, cv2.LINE_AA)
            pag.keyDown('down')
            pag.keyUp('down')
            

    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    # If q key is presssed then the camera closes

video.release()
cv2.destroyAllWindows()
