import cv2

cap=cv2.VideoCapture(1)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('check',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    else:
        break

cap.release()
cv2.destroyAllWindows()