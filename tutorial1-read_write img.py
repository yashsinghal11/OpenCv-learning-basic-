import cv2

# Read the image
img = cv2.imread("testing.png",0)   # change 'testing.png' with the image name that you want to use

# Show the image (add a window name as first argument)
cv2.imshow("Image", img)
cv2.imwrite("img_copy.jpg",img)
# Wait until a key is pressed (0 means infinite wait)
cv2.waitKey(0)

# Destroy all OpenCV windows after key press
cv2.destroyAllWindows()
