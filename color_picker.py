import cv2 as cv
import numpy as np

cap=cv.VideoCapture(0)

cap.set(3, 640) #sets the webcam frame width
cap.set(4, 480) #sets the webcam frame height
cap.set(10, 150) #sets the webcam brightness

def empty(a):
    pass

#creating our trackbar windows
cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", (640, 240))

cv.createTrackbar("Hue min", "Trackbars", 0, 179, empty)
cv.createTrackbar("Hue max", "Trackbars", 179, 179, empty)
cv.createTrackbar("Sat min", "Trackbars", 0, 255, empty)
cv.createTrackbar("Sat max", "Trackbars", 255, 255, empty)
cv.createTrackbar("Value min", "Trackbars", 0, 255, empty)
cv.createTrackbar("Value max", "Trackbars", 255, 255, empty)


while True:
    success, frame=cap.read()

    # frame_HSV=cv.cvtColor(frame, cv.COLOR_BGR2HLS)

    h_min=cv.getTrackbarPos("Hue min", "Trackbars")
    h_max=cv.getTrackbarPos("Hue max", "Trackbars")
    s_min=cv.getTrackbarPos("Sat min", "Trackbars")
    s_max=cv.getTrackbarPos("Sat max", "Trackbars")
    v_min=cv.getTrackbarPos("Value min", "Trackbars")
    v_max=cv.getTrackbarPos("Value max", "Trackbars")

    print(h_min, s_min, v_min, h_max, s_max, v_max)

    lower=np.array([h_min, s_min, v_min])
    upper=np.array([h_max, s_max, v_max])

    mask=cv.inRange(frame, lower, upper)
    # frame_res=cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("Live Video", frame)
    cv.imshow("Result", mask)

    if(cv.waitKey(1)==ord('x')):
        break