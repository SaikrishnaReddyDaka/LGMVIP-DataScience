"""
Daka Saikrishna Reddy
Data Science Internship at Let's Grow More
LGMVIP FEBRUARY 2022
Beginner Level Task - Image to Pencil sketch with python
"""
import cv2

# Using imread to read the original image
pic = cv2.imread('dubai.jpg', 330)
cv2.imshow('Original Image', pic)
cv2.waitKey(0)

# Reading black and white image
black_white_image = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
cv2.imshow("Black and White Image", black_white_image)
cv2.waitKey(0)

# Inverting the image- reversing the colours of the image
invert_image = 255 - black_white_image
cv2.imshow("Inverted Image", invert_image)
cv2.waitKey(0)

# Blurring the inverted image
blurred_image = cv2.GaussianBlur(invert_image, (21, 21), 0)
# Inverting the blurred image
inverted_blurred_image = 255 - blurred_image

# Creating Pencil Sketch
pencil_sketch = cv2.divide(black_white_image, inverted_blurred_image, scale=256.0)
cv2.imshow("Pencil Sketch Image", pencil_sketch)
cv2.waitKey(0)

# Displaying the original image
cv2.imshow('Original Image', pic)
# Displaying pencil sketch image
cv2.imshow('Pencil sketch Image', pencil_sketch)
cv2.waitKey(0)


"""
 Thank you for watching, Please share your valuable feedback
"""

