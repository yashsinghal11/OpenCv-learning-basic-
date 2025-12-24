import cv2
import numpy as np

def nothing(x):
    pass

# Read image once
frame = cv2.imread("smarties.jpeg")
if frame is None:
    print("Image not found!")
    exit()

# Create a window
cv2.namedWindow("Trackbars")

# Create trackbars for lower HSV
cv2.createTrackbar("LH", "Trackbars", 0, 179, nothing)   # Hue: 0-179
cv2.createTrackbar("LS", "Trackbars", 0, 255, nothing)   # Saturation: 0-255
cv2.createTrackbar("LV", "Trackbars", 0, 255, nothing)   # Value: 0-255

# Create trackbars for upper HSV
cv2.createTrackbar("UH", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("US", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("UV", "Trackbars", 255, 255, nothing)

while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar positions
    lh = cv2.getTrackbarPos("LH", "Trackbars")
    ls = cv2.getTrackbarPos("LS", "Trackbars")
    lv = cv2.getTrackbarPos("LV", "Trackbars")

    uh = cv2.getTrackbarPos("UH", "Trackbars")
    us = cv2.getTrackbarPos("US", "Trackbars")
    uv = cv2.getTrackbarPos("UV", "Trackbars")

    # Define lower and upper range
    lower_bound = np.array([lh, ls, lv])
    upper_bound = np.array([uh, us, uv])

    # Mask and result
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Show results
    cv2.imshow("Original", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", res)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key
        break

cv2.destroyAllWindows()
