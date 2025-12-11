import cv2
cap=cv2.VideoCapture(0);
while (True):
    ret,frame=cap.read()
    #for grayscale capture just do this -------
    '''
    gray=cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
    and chnage frame name in below line with 'gray'
    '''
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()