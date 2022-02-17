from pyzbar import pyzbar; from datetime import *; import time

import cv2

def time_date(frame):
    BCHScan = pyzbar.decode(frame)
    for info in BCHScan:
        a, b, c, d = info.rect
        TxtBCHFile = info.data.decode('utf-8')
        cv2.rectangle(frame, (a,b),(a+c, b+d),(0, 255, 0),3)
        TxtFont = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(frame, TxtBCHFile, (a + 10, b - 10), TxtFont, 1.0, (255 , 0 , 0), 2)

        localtime = datetime.now() 
        date = localtime.strftime("%B %d, %Y") 
        presentTime = time.localtime() 
        timearea = time.strftime("%H:%M", presentTime) 
        timeareaNum = int(time.strftime("%H", presentTime)) 
        timeareaDate = time.strftime("%M", presentTime) 
        hour_time = 12

        with open(information, "w") as update:
            if timeareaNum >= 0 and timeareaNum < hour_time:
                update.write(TxtBCHFile + (f"\nDate Recorded: {date}\nTime Recorded: {timearea} AM"))
            else:
                presentTime = (timeareaNum) - hour_time
                update.write(TxtBCHFile + (f"\nDate Recorded: {date}\nTime Recorded: {presentTime}:{timeareaDate} PM"))
    return frame; 

information = "contacttracing.txt"

def webcamExtract():
    aperture = cv2.VideoCapture(0) 
    unveil = cv2.QRCodeDetector() 
    while True: 
        _, frame = aperture.read() 
        info, cam, _ = unveil.detectAndDecode(frame)
        frame = time_date(cv2.resize(frame, None, fx=1.5, fy=1.5, interpolation = cv2.INTER_LINEAR_EXACT)) 
        cv2.imshow("ROSALES QR CODE DETECTOR", frame) 
        if cv2.waitKey(1) == ord('f'): 
            break 
    aperture.release() 
    cv2.destroyAllWindows() 

webcamExtract() 