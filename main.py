import keygenerator as kg
import numpy as np
import cv2

img = cv2.imread("PATH")
cv2.imshow('Normal Image', img)
cv2.waitKey(0)
height = img.shape[0]
width = img.shape[1]
key = kg.keygen(0.01, 3.95, height*width)
print(key)

z = 0
en_img = np.zeros(shape=[height, width, 3], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        en_img[i, j] = img[i, j] ^ key[z]
        z += 1
cv2.imshow('Encrypted', en_img)
cv2.waitKey(0)
cv2.imwrite("Path to save the Encrypted Image", en_img)

z = 0
dec_img = np.zeros(shape=[height, width, 3], dtype=np.uint8)
for i in range(height):
    for j in range(width):
        dec_img[i, j] = en_img[i, j] ^ key[z]
        z += 1
cv2.imshow('Decrypted', dec_img)
cv2.waitKey(0)
cv2.imwrite("C:/Users/adroi/Downloads", dec_img)
