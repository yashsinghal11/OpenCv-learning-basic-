import cv2
img=cv2.imread("testing.png",1) #read image for operations
img=cv2.circle(img,(250,250),180,(147,96,44),10) #given parameters to draw circle on image
'''
for rectangle:cv2.rectangle(image, pt1, pt2, color, thickness)
for diffrent :cv2.polylines(img, [points], isClosed=True, color=(0,255,255), thickness=2)
'''

cv2.imwrite("circle_image.png",img) # saved the image as circled_image

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

