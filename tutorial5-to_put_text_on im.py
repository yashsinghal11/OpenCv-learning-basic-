import cv2
img=cv2.imread("testing.png",1) #read image for operations
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,'OPENCV',(10,500),font,4,(0,255,255),10,cv2.LINE_AA)
cv2.imwrite('text_img.png',img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

