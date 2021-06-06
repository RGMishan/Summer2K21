import cv2
import numpy as np

image = np.zeros((800,800,3), dtype="uint8",)

#the face
image = cv2.circle(image, (400,400), 350, (0,255,255), -1 )

#left eye white part
image = cv2.circle(image, (270,270), 75, (255,255,255), -1)
#left eye white part
image = cv2.circle(image, (275,290), 30, (0,0,0,0), -1)
#right eye white part
image = cv2.circle(image, (550,270), 75, (255,255,255), -1)
#right eye white part
image = cv2.circle(image, (550,290), 30, (0,0,0,0), -1)

#nose part
p1 = (410, 360)
p2 = (380, 420)
p3 = (440, 420)

cv2.line(image, p1, p2, (0, 0, 255), 3)
cv2.line(image, p2, p3, (0, 0, 255), 3)
cv2.line(image, p1, p3, (0, 0, 255), 3)

#moustace part
image = cv2.ellipse(image, (415,450), (100,50), 0, 0, 90, (0,0,0), -1)
image = cv2.ellipse(image, (410,450), (100,50), 0, 90, 180, (0,0,0), -1)

#text in mouth
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1.5
image = cv2.putText(image, 'SMILEE', (340,550), font, fontScale, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow("face" , image)
cv2.waitKey()
cv2.destroyAllWindows()