import cv2, time
imgW = 320
imgH = 240

#cv2.namedWindow("Window!", cv2.WINDOW_AUTOSIZE)
camera_index = 0

cap = cv2.VideoCapture(0)
a = 0
#cv2.VideoCapture.set(capture, cv2.CV_CAP_PROP_FRAME_WIDTH, imgW);
#cv2.VideoCapture.set(cv2.CV_CAP_PROP_FRAME_HEIGHT, imgH);
cap.set(cv2.CAP_PROP_FRAME_WIDTH, imgW);
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, imgH)

while True:
    a = a + 1
    #frame = cv2.QueryFrame(cap)
    ret, frame = cap.read()
    print(ret)
    print(frame)
   # cv2.imshow("window1", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    cv2.imshow("Capturing", gray)
    command = cv2.waitKey(1)
    if command == ord('q'):
        print("Ending program")
        break
    #elif command == ord('s'):
     #   print("saving image")
      #  cv2.SaveImage("test.jpg", frame)
    print(a)
cap.release()
cv2.destroyAllWindows()