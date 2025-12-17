import cv2

# Read the image
img = cv2.imread("messi.jpeg")   # change 'testing.png' with the image name that you want to use

# Show the image (add a window name as first argument)
cv2.imshow("Image", img)
print(img.size)
print(img.shape)
print(img.dtype)

b, g, r = cv2.split(img)          # Split into channels
img = cv2.merge((b, g, r))        # Merge back
# Crop ball (y:0→26 , x:76→87)
ball = img[0:26, 76:87]   # shape (26, 11, 3)

# Paste ball at new location (must also be 26×11 region)
img[50:76, 200:211] = ball

# Wait until a key is pressed (0 means infinite wait)
cv2.waitKey(0)

# Destroy all OpenCV windows after key press
cv2.destroyAllWindows()
