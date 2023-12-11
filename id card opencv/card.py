import cv2 as cv
cam = cv.VideoCapture(0)
detect = cv.CascadeClassifier("content\haarcascade_frontalface_default.xml")
Id= int(input("Enter the search"))
samplenum = 0
while True:
    ret, img2 = cam.read()
    gray = cv.cvtColor(img2, cv.COLOR_BAYER_BG2BGR)
    faces = detect.detectMultiScale(gray, 1.3,5)
    for (x ,y,w,h) in faces:
        cv.rectangle(img2, (x,y),(x+w,y+h),(255,0,0),2)
        samplenum = samplenum + 1
        cv.imwrite("content\photos" +Id + '.' +str(samplenum) +".jpg",gray[y:y +h,x:x+w])
        cv.imshow('frame' , img2)
    #wait for 100 miliseconds
    if cv.waitKey(100) & 0xFF == ord('q'):
        break
    elif samplenum>1:
        break
cam.release()
cv.destroyAllWindows()