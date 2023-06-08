import cv2
import numpy as np

farm_img = cv2.imread('C:/Users/Karim/Desktop/Python/ImageRecognition/farm.png', cv2.IMREAD_UNCHANGED)
wheat_img = cv2.imread('C:/Users/Karim/Desktop/Python/ImageRecognition/needle.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('Farm', farm_img)
cv2.waitKey()
cv2.destroyAllWindows

cv2.imshow('Needle', wheat_img)
cv2.waitKey()
cv2.destroyAllWindows

result = cv2.matchTemplate(farm_img, wheat_img, cv2.TM_CCOEFF_NORMED)

cv2.imshow('Result', result)
cv2.waitKey()
cv2.destroyAllWindows

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print(max_loc)
print(max_val)

w = wheat_img.shape[1]
h = wheat_img.shape[0]

print(cv2.rectangle(farm_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2))

cv2.imshow('Farm', farm_img)
cv2.waitKey()
cv2.destroyAllWindows

threshold = .60
yloc, xloc = np.where(result >= threshold)
 
print(len(xloc))

for (x, y) in zip(xloc, yloc):
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (0,255,255), 2)
    
cv2.imshow('Farm', farm_img)
cv2.waitKey()
cv2.destroyAllWindows()

# What is a rectangle?
# x, y, w, h
rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(w), int(h)])
    rectangles.append([int(x), int(y), int(w), int(h)])
    
print(len(rectangles))

rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
print(rectangles)

print(len(rectangles))

cv2.imshow('Farm', farm_img)
cv2.waitKey()
cv2.destroyAllWindows()