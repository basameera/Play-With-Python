import cv2
import utils as ut


if __name__ == "__main__":
    arucoDict, arucoParams = ut.aruco_init()
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, image = cap.read()

        (corners, ids, rejected) = cv2.aruco.detectMarkers(
            image, arucoDict, parameters=arucoParams)

        if ids is not None:
            image = ut.drawAruco(image, ids, corners)

        cv2.imshow('Input', image)

        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
