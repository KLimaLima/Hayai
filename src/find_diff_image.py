import cv2
import numpy as np

# Load two images
image1 = cv2.imread('result/frame406.jpg')
image2 = cv2.imread('result/frame348.jpg')
# Convert images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# Compute absolute difference between the two images
difference = cv2.absdiff(gray1, gray2)
# Apply thresholding to highlight the differences
_, thresholded = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)
# Find contours of the differences
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Draw rectangles around the differing regions
for contour in contours:
 x, y, w, h = cv2.boundingRect(contour)
 cv2.rectangle(image1, (x, y), (x + w, y + h), (0, 0, 255), 2)

#--- convert the result to integer type ---
res = difference.astype(np.uint8)

print("convert to int", np.count_nonzero(res))

#--- find percentage difference based on number of pixels that are not zero ---
percentage = (np.count_nonzero(res) * 100)/ res.size
print("percentage", percentage)

win_name = "result"
# Create a Named Window
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

# Move it to (X,Y)
cv2.moveWindow(win_name, 50, 50)
    
# Show the Image in the Window
cv2.imshow(win_name, image1)
    
# Resize the Window
cv2.resizeWindow(win_name, 960, 540)

# Display the result
# cv2.imshow('Difference', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()