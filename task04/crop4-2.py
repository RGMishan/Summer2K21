import cv2
import numpy as np

#getting image 1
emptyface = cv2.imread("emptyface.jpg")
cv2.imshow("Empty Face" , emptyface)

#cropping faceout
cropemp = emptyface[26:26+455, 57:57+374]
cv2.imshow("Cropped Empty Face", cropemp)

#getting image 2
manface = cv2.imread("face.jpg")
cv2.imshow("Man Face" , manface)

# cropping faceout
manface = cv2.imread("face.jpg")
cropman = manface[26:26+455, 57:57+374]
cv2.imshow("Cropped Man Face", cropman)

#swapping 1
emptyface = cv2.imread("emptyface.jpg")
emptyface[26:26+455, 57:57+374] = cropman
cv2.imshow("Swap Face 1", emptyface)

# swapping 2
manface[26:26+455, 57:57+374] = cropemp
cv2.imshow("Swap Face 2", manface)
cv2.waitKey()
cv2.destroyAllWindows()