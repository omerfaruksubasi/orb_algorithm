import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
 
# Load the training image (grayscale)
img1 = cv.imread('bayrak.jpg', cv.IMREAD_GRAYSCALE)  # training image
# Load the target image (grayscale)
img2 = cv.imread('bayraklar.jpg', cv.IMREAD_GRAYSCALE)  # general image with multiple objects
 
# Initialize the ORB detector
orb = cv.ORB_create()
 
# Find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Create a BFMatcher object with Hamming distance metric and cross-check enabled
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
 
# Match descriptors between the two images
matches = bf.match(des1, des2)
 
# Sort matches by their distance (lower distance is better)
matches = sorted(matches, key=lambda x: x.distance)
 
# Draw the top 20 matches
img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:20], None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
 
# Show the result using matplotlib
plt.imshow(img3), plt.show()
