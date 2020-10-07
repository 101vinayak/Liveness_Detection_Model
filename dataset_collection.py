import numpy as np
import cv2

def dataset():

    cap = cv2.VideoCapture(0)
    count = 0

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        gray = frame

        if count<1000:
            cv2.imwrite('img-not-live/' +str(count) + ".jpg", frame)
        else:
            break

        count += 1

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    count = 0
    '''
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if count<1000:
            cv2.imwrite('img-live/' +str(count) + ".jpg", frame)
        else:
            break

        count += 1

        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    '''