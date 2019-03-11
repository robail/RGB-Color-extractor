
from PIL import Image
import cv2
import numpy as np

width = 480
height = 360
files = glob("/home/pszry/usr/local/MASK/color_mask/*.jpg")


i= len(files)
print i

for x in range(0, i):
    fn = files[x] 
    img=cv2.imread(fn)
    

    ######################################## 
    a = os.path.basename(fn)
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

     
    lower_black = np.array([0,0,0])
    upper_black = np.array([70,70,70])
    black_mask = cv2.inRange(hsv, lower_black, upper_black)
    black_mask[np.where((black_mask == [0]))] = [0]     # for black
    print np.unique(black_mask)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    blue_mask = cv2.inRange(hsv, lower_blue, lower_blue)
    blue_mask[np.where((blue_mask == [0]))] = [0]     # for blue
    print np.unique(blue_mask)

    ########################################
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    red_mask = cv2.inRange(hsv, lower_red, upper_red) 
    red_mask[np.where((red_mask == [0]))] = [1]     # for red
    print np.unique(red_mask)
    #############################
    
    lower_green = np.array([0, 100, 100])
    upper_green = np.array([20, 255, 255])
    green_mask = cv2.inRange(hsv, lower_green, upper_green) 
    green_mask[np.where((green_mask == [0]))] = [2]      # for green 
    print np.unique(green_mask)



    # Add ALL
    mask = green_mask +  red_mask + black_mask + blue_mask
    print np.unique(mask)



    cv2.imwrite('/home/pszry/usr/local/MASK/root_mask/'+a, mask)



