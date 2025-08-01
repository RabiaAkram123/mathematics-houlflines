##############houlfline probublistic######


import cv2
import numpy as np
img=cv2.imread("sudoko.png")
resize_img=cv2.resize(img,(800,600))
gray=cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,150,apertureSize=3)
#cv2.imshow("canny_image",edges)
lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
     x1,y1,x2,y2 =line[0]
     cv2.line(resize_img,(x1,y1),(x2,y2),(0,0,255),2)
    
cv2.imshow("imag",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows
    
    
