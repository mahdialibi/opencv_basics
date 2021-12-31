

import cv2 as cv
ddepth = cv.CV_16S
kernel_size = 3
window_name = "Laplace Demo"
# [variables]
# [load]
imageName = 'data/text.jpg'
src = cv.imread(imageName, cv.IMREAD_COLOR) # Load an image
# [reduce_noise]
# Remove noise by blurring with a Gaussian filter
src = cv.GaussianBlur(src, (3, 3), 0)

# [convert_to_gray]
# Convert the image to grayscale
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
# converting back to uint8
abs_dst = cv.convertScaleAbs(dst)
#[display]
cv.imshow('Laplacian', abs_dst)

sobelx_dst=cv.Sobel(src_gray,cv.CV_64F,1,0)
sobely_dst=cv.Sobel(src_gray,cv.CV_64F,1,0)
sobelxy_dst = cv.bitwise_or(sobelx_dst,sobely_dst)
cv.imshow('sobel', sobelxy_dst)
cv.waitKey(0)
