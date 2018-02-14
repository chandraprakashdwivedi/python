import cv2, time

first_frame=None
video=cv2.VideoCapture(0)


#we are using while loop to continously capturing video from camera or not just a single frame
while True:
     check, frame = video.read()

     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     gray=cv2.GaussianBlur(gray,(21,21),0) #we are using gaussianblur to blur out the gray image 21,21 height & widhth of gaussian kernel and 0 is a recommnede value

     if first_frame is None:
         first_frame=gray
         continue

     delta_frame=cv2.absdiff(first_frame,gray) #here we are comparing first frame with current frame

# where 30= is the threhold limit 255=value applied to those whose threshold is 30
     thresh_frame=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
     thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

     (_,cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

     for countour in cnts:
         if cv2.contourArea(contour) < 1000:
             continue
          (x,y,w,h)=cv2.boundingRect(contour)
          cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

     

     cv2.imshow("gray frame",gray)
     cv2.imshow("delta frame",delta_frame)
     cv2.imshow("thresh frame",thresh_frame)
     cv2.imshow("color frame",frame)

    

     key=cv2.waitKey(1)
     print(gray)
     print(delta_frame)

     if key==ord('q'):
         break


video.release()
cv2.destroyAllWindows()
