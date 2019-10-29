import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def otsu_thresh(src):
    Vb_max = 0.0          # Variance bw classes
    #find threshold_value
    src = cv2.GaussianBlur(src, (3,3), 0)
    histogram = cv2.calcHist([src], [0], None, [256], [0, 256])
    cum_sum = np.cumsum(histogram.ravel())
    index = np.arange(0,256)
    multiply = np.multiply(histogram.ravel(), index)
    cumsum_mul = np.cumsum(multiply)
    for i in range(256):
        if (i==0):
            continue
        else:
            w1= cum_sum[i-1]/cum_sum[255]
            w2= (cum_sum[255] - cum_sum[i-1])/cum_sum[255]
            mean1 = cumsum_mul[i-1]/cum_sum[i-1]
            mean2 = (cumsum_mul[255]-cumsum_mul[i-1])/(cum_sum[255]-cum_sum[i-1])
            Vb = w1*w2*np.square(mean1 - mean2)
            if (Vb > Vb_max):
                Vb_max = Vb
                threshold = i
    #thresholding
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if (img[i,j]< threshold):
                img[i,j] =0
            else: img[i,j] = 255
    return threshold, img

# Test function
img = cv2.imread('egg2.jpg', 0)

ret, thr = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

th, result = otsu_thresh(img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])

fig = plt.figure()

# show original image
fig.add_subplot(121)
plt.title('OpenCV threshold:'+str(ret))
plt.xticks([])
plt.yticks([])
plt.set_cmap('gray')
plt.imshow(result)

fig.add_subplot(122)
plt.title('Our threshold: '+str(th))
plt.xticks([])
plt.yticks([])
plt.imshow(thr)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()