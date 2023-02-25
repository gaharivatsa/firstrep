import cv2 as cv

capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)

def rescaleframe(frame,resize):
    width = int(frame.shape[1] * resize)
    height  = int(frame.shape[0] * resize)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    frame1 = rescaleframe(frame, 0.5)
    cv.imshow('video', frame1)

    key = cv.waitKeyEx(1)
    if key == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
