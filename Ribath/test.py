import cv2
from PIL import Image

property_id = int(cv2.CAP_PROP_FRAME_COUNT)

# cap1 = cv2.VideoCapture("vid1")
# length1 = int(cv2.VideoCapture.get(cap1, property_id))
# print( length1 )
#
# cap2 = cv2.VideoCapture("vid2")
# length2 = int(cv2.VideoCapture.get(cap2, property_id))
# print( length2 )
#
# success,image = cap1.read()
# count = 0;
# while success:
#     success,image = cap1.read()
#     cv2.imwrite("imgFromVid1/frame%d.jpg" % count, image)     # save frame as JPEG file
#     if cv2.waitKey(10) == 27:                     # exit if Escape is hit
#         break
#     if count == length1-2:
#         break
#     count += 1
#
# success,image = cap2.read()
# count = 0;
# while success:
#     success,image = cap2.read()
#     cv2.imwrite("imgFromVid2/frame%d.jpg" % count, image)     # save frame as JPEG file
#     if cv2.waitKey(10) == 27:                     # exit if Escape is hit
#         break
#     if count == length2-2:
#         break
#     count += 1

img = cv2.imread('imgFromVid2/frame12.jpg')
dimensions = img.shape
print(dimensions)

# im = Image.open('musk.jpg', 'r')
# width, height = im.size
# pixel_values = list(im.getdata())
# print(pixel_values[width])

im = Image.open('musk.jpg') # Can be many different formats.
pix = im.load()
print (im.size)  # Get the width and hight of the image for iterating over
countX = 0
countY = 0
# matrix = [[0]*640]*360
matrix = []
while countX<282:
    new = []
    while countY<500:
        if(countY%3==0):
            new.append(1)
        else:
            new.append(0)
        countY+=1
    matrix.append(new)
    countY=0
    countX+=1

# for z in range(192):
img = cv2.imread('imgFromVid1/frame12.jpg')
for x in range(282):
    for y in range(500):
        if(matrix[x][y]==1):
            # sdf = img[x, y]
            # print(sdf)
            img[x,y]=(0,0,0)

cv2.imwrite('Test.jpg', img)
