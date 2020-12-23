# https://docs.opencv.org/3.4.0/d5/dae/tutorial_aruco_detection.html
# https://docs.opencv.org/3.4.3/dc/dbb/tutorial_py_calibration.html
# https://docs.opencv.org/3.1.0/d5/dae/tutorial_aruco_detection.html

import cv2
import utils as ut


if __name__ == "__main__":

    arucoDict, arucoParams = ut.aruco_init()

    image_file = '20201223_173642.jpg'
    image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    image_copy = image.copy()

    (corners, ids, rejected) = cv2.aruco.detectMarkers(
        image, arucoDict, parameters=arucoParams)

    image = ut.drawAruco(image, ids, corners)

    cv2.imshow("image", image)
    cv2.waitKey(0)
