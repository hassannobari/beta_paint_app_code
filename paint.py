import cv2 
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((800,800,3),np.uint8)
cv2.namedWindow("image")

def nothing(x):
    pass
cv2.createTrackbar("R","image",0,255,nothing)
cv2.createTrackbar("G","image",0,255,nothing)
cv2.createTrackbar("B","image",0,255,nothing)
flu = "thickness"
cv2.createTrackbar(flu,"image",0,5,nothing)

draw = False
ix = 0 
iy = 0
r,g,b,s = 255,255,255,5
history = []
def draww(event,x,y,flags,param):
    global draw,ix,iy,r,g,b,s,img
    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        ix = x
        iy = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw:
            cv2.line(img,(ix,iy),(x,y),color=(b,g,r),thickness=s)
            ix , iy = x,y
    elif event == cv2.EVENT_LBUTTONUP:
        draw =False
        history.append(img.copy())

cv2.setMouseCallback("image",draww)

while True:
     cv2.imshow("image",img)
     key =cv2.waitKey(1) & 0xFF
     if key == 27:
        break
     elif key == ord('c'):
        img [:] = 0
        history.clear()
     elif key == ord('z'):
         if len(history) >0:
             img = history.pop()
         
     r = cv2.getTrackbarPos("R","image")
     g = cv2.getTrackbarPos("G","image") 
     b = cv2.getTrackbarPos("B","image")
     s = cv2.getTrackbarPos(flu,"image")
     if s == 0:
        s = 1
        
cv2.destroyAllWindows()
