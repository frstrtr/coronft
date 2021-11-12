import cv2

image = cv2.imread('images/coronavirus-png-68_2_without_alpha.png')
img_gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)

# apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# visualize the binary image
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)
cv2.imwrite('image_thres1.jpg', thresh)
cv2.destroyAllWindows()

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_LIST , method=cv2.CHAIN_APPROX_NONE)
                                     
# draw contours on the original image
image_copy = image.copy()
for contour in contours:
    convexHull = cv2.convexHull(contour)
    cv2.drawContours(image=image_copy, contours=[convexHull], contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(len(contours)):
    _contour = cv2.convexHull(contours[i])
    print("Contours:")
    print('len={0}'.format(len(_contour)))
    print(_contour)
    
# see the results
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()
