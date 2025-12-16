import cv2
import datetime
cap=cv2.VideoCapture(0);
while (True):
    ret,frame=cap.read()
    #for grayscale capture just do this -------
    '''q
    gray=cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
    and chnage frame name in below line with 'gray'
    '''
    #to print date and time we use this 
    datet=str(datetime.datetime.now())
    cv2.putText(frame, datet, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()