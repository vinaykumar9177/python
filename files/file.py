import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow("Trackbars")

cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    #red colour
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
    #blue colour
    lower_blue= np.array([94, 80, 2])
    upper_blue= np.array([126, 255, 255])
    blue_mask= cv2.inRange(hsv_frame, lower_blue, upper_blue)
    blue = cv2.bitwise_and(frame, frame,mask=blue_mask)
    #yellow colour
    lower_yellow= np.array([25, 52, 72])
    upper_yellow= np.array([102, 255,255])
    yellow_mask=cv2.inRange(hsv_frame, lower_yellow, upper_yellow)
    yellow=cv2.bitwise_and(frame, frame, mask=yellow_mask)
    cv2.imshow("frame", frame)
    cv2.imshow("result", blue)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()