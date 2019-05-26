import cv2
import imageio
import numpy as np
from matplotlib import pyplot as plt

# inspired in the contents that can be found at
# these links:
#
# https://stackoverflow.com/questions/2938162/how-does-an-unsharp-mask-work
# https://en.wikipedia.org/wiki/Unsharp_masking
#
def unsharping_mask (image, weight, threshold):
    n,m = image.shape

    blurred_image = cv2.GaussianBlur(image,(7,7),0)
    mask = image - blurred_image

    # TODO Get another version of the image with
    # higher contrast to use in this operation
    for x in range(n):
        for y in range(m):
            new_value = weight * mask[x,y]

            if(abs(new_value) > threshold):
                image[x,y] = image[x,y] + new_value

    # Debugging
    #plt.imshow(blurred_image, cmap="gray")
    #plt.show()
    plt.imshow(mask, cmap="gray")
    plt.show()
    plt.imshow(image, cmap="gray")
    plt.show()

    return image

def test ():
    img = imageio.imread('test-image.tif')
    plt.imshow(img, cmap="gray")
    plt.show()
    unsharping_mask(img, 0.8, 190)
    return

test()