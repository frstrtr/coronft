import cv2

_image = cv2.imread('images/coronavirus-png-68_2_without_alpha.png')

scale_percent = 40 # percent of original size
width = int(_image.shape[1] * scale_percent / 100)
height = int(_image.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(_image,dim, interpolation=cv2.INTER_AREA)
img_gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)

# apply binary thresholding
ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
# visualize the binary image
# cv2.imshow('Binary image', thresh)
# cv2.waitKey(0)
# cv2.imwrite('image_thres1.jpg', thresh)
# cv2.destroyAllWindows()

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_LIST , method=cv2.CHAIN_APPROX_NONE)
print(hierarchy)                                     
# draw contours on the original image
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=[contours[0]], contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)

for i in range(len(contours)):
    _contour = contours[i]#cv2.convexHull(contours[i])
    print("Contours:")
    print('len={0}'.format(len(_contour)))
    print('Area={0}\n'.format(cv2.contourArea(_contour)))
    #print(_contour)
    # print(contours)
    
#see the results
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()

f = open('contour2.txt', 'w')
i = 0
for x in contours[0]:
    i += 1
    for _x, _y in x:
    # f.write()
        if i < 10:
            break
        i = 0
        res = "{0} {1} 0\n".format(_x, _y)
        # print(res)
        f.write(res)

# for x in contours[0]:
#     f.write(str(x))
f.close()
contours[0].tofile("contour.txt", sep = ",", format = "%s")