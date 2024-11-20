# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 22:33:04 2024

@author: Aldzz
"""

import numpy as np
import cv2

#Rekam Video
cam = cv2.VideoCapture("c:\\Users\\Asus\\Pictures\\part2.mp4", 0 )

#Upload Video
#cam = cv2.VideoCapture(cv2.CAP_DSHOW)

#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 120)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)

#konvolusi manual
def konvolusi(image, kernel):
    row,col= image.shape
    mrow,mcol=kernel.shape
    h =int(mrow/2)

    canvas = np.zeros((row,col),np.uint8)
    for i in range(0,row):
        for j in range(0,col):
            if i==0 or i==row-1 or j==col-1:
                canvas.itemset((i,j),0)
            else:
                imgsum=0
                for k in range (-h, mrow-h):
                    for l in range (-h, mcol-h):
                        res=image[i+k,j+l] * kernel[h+k,h+l]
                        imgsum+=res
                    canvas.itemset((i,j), imgsum)
    return canvas
 
def kernel1(image):
    kernel = np.array([[-1/9, -1/9, -1/9],[-1/9, 8/9, -1/9],[-1/9, -1/9, -1/9]],np.float32)
    canvas = konvolusi(image, kernel)
    return canvas

def kernel2(image):
    kernel = np.array([[0, 1/8, 0],[1/8, 1/2, 1/8],[0, 1/8, 0]],np.float32)
    canvas2 = konvolusi(image, kernel)
    return canvas2

while True: 
    #mengubah masing masing citra sesuai dengan perintahnya
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    test1=kernel1(gray)
    cv2.imshow("gambar1",gray)
    cv2.imshow("High pass",test1)

    test2=kernel2(gray)
    cv2.imshow("gambar2",gray)
    cv2.imshow("low pass",test2)

    print(" gamabr1 ", gray)    
    print(" gambar2 ", gray)
    print(" gambar1 ", gray.shape)
    print(" gambar2 ", gray.shape) 
    print(" high filter image1 ", test1.shape)
    print(" lowpass image1", test1.shape)
    print(" high filter image2 ", test2.shape)
    print(" lowpass image2", test2.shape)
    
    if cv2.waitKey(1)==ord('1'):
        break
cv2.destroyAllWindows()

"""

System Model: ASUS EXPERTBOOK L1400CDAY_L1400CDA
                     BIOS: L1400CDAY.304 (type: UEFI)
                Processor: AMD Ryzen 3 3250U with Radeon Graphics          (4 CPUs), ~2.6GHz
Card name: AMD Radeon(TM) Vega 3 Graphics
        Manufacturer: Advanced Micro Devices, Inc.
           Chip type: AMD Radeon Graphics Processor (0x15D8)
RAM = 8 GB
          
         """