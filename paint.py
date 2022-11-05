from platform import architecture
import cv2 as cv
import numpy as np

colours=[[37, 41, 167, 90, 82, 255], #orange
    [0 ,111, 0, 179, 255, 77], #green
    [136, 78, 190, 163, 114, 255]] #pink

dotColors=[[38, 169, 235],#orange
           [90, 237, 95], #green        
           [182, 104, 237]] #pink

myPoints=[] #x, y, dotColorsID --> draw points in a loop-- gives a line-- for a particular DotColorID at that point x, y

def findColor(frame, colours, dotColors):
    count=0
    newPoint=[]
    for color in colours:
        lower=np.array(color[0:3])
        upper=np.array(color[3:6])
        mask=cv.inRange(frame, lower, upper)
        x, y=getContour(mask)
        cv.circle(imgRes, (x,y), 10, dotColors[count], -1)
        if(x!=0 and y!=0):
            newPoint.append([x,y,count])
        count+=1
        #cv.imshow(str(color[4]), mask)
    return newPoint

FrameWidth = 640
FrameHeight = 480

cap=cv.VideoCapture(0)

cap.set(3, FrameWidth) #sets the webcam frame width
cap.set(4, FrameHeight) #sets the webcam frame height
cap.set(10, 150) #sets the webcam brightness

def getContour(img):
    contours, hierarchy=cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv.contourArea(cnt)
        if(area>500):
            #cv.drawContours(imgRes, cnt, -1, (0,255,0), 3)
            perimeter=cv.arcLength(cnt, True)
            approx=cv.approxPolyDP(cnt, 0.02*perimeter, True)
            x, y, w, h=cv.boundingRect(approx)
    return x+w//2, y    


def DrawonCanvas(myPoints, dotColors):
    
    for point in myPoints:
        cv.circle(imgRes, (point[0], point[1]), 20, dotColors[point[2]], -1)


while True:

    success, frame=cap.read()
    # frame_HSV=cv.cvtColor(frame, cv.COLOR_BGR2HLS)
    imgRes=frame.copy()
    newPoint=findColor(frame, colours, dotColors)

    if(len(newPoint)!=0):
        for newP in newPoint:
            myPoints.append(newP)
    if(len(myPoints)!=0):    
        DrawonCanvas(myPoints, dotColors)    
    cv.imshow("Result", imgRes)

    #cv.imshow("Live Feed", frame)
    

    if(cv.waitKey(1)==ord('x')):
        break


