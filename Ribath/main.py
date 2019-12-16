import cv2

property_id = int(cv2.CAP_PROP_FRAME_COUNT)

cap1 = cv2.VideoCapture("vid1")
length1 = int(cv2.VideoCapture.get(cap1, property_id))
print( length1 )

cap2 = cv2.VideoCapture("vid2")
length2 = int(cv2.VideoCapture.get(cap2, property_id))
print( length2 )

success,image = cap1.read()
count = 0;
while success:
    success,image = cap1.read()

    resized_image = cv2.resize(image,(640, 360),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)   #resize image
    cv2.imwrite("imgFromVid1/frame%d.jpg" % count, resized_image)     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    if count == length1-2:
        break
    count += 1

success,image = cap2.read()
count = 0;
while success:
    success,image = cap2.read()
    resized_image = cv2.resize(image,(640, 360),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)   #resize image
    cv2.imwrite("imgFromVid2/frame%d.jpg" % count, resized_image)     # save frame as JPEG file
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
        break
    if count == length2-2:
        break
    count += 1

countX = 0
countY = 0
matrix = []
while countX<360:
    new = []
    while countY<640:
        if(countY%2==0):
            new.append(1)
        else:
            new.append(0)
        countY+=1
    matrix.append(new)
    countY=0
    countX+=1

for z in range(133):
    img1 = cv2.imread('imgFromVid1/frame%d.jpg'%z)
    img2 = cv2.imread('imgFromVid2/frame%d.jpg'%z)
    for x in range(360):
        for y in range(640):
            if(matrix[x][y]==1):
                color = img2[x,y]
                img1[x,y]=(color[0],color[1],color[2])
    cv2.imwrite('processedImg/frame%d.jpg'%z, img1)


img_array = []
for i in range(132):
    img = cv2.imread("processedImg/frame%d.jpg"%i)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

for i in range(132):
    out.write(img_array[i])
out.release()