import cv2
import utils as ut
import numpy as np


def image_resize(image, h, w):
    return cv2.resize(image, (h, w), interpolation=cv2.INTER_AREA)


if __name__ == "__main__":
    arucoDict, arucoParams = ut.aruco_init()
    cap = cv2.VideoCapture(0)

    image_height = 720
    image_width = 1280
    image_center_x = image_width//2
    image_center_y = image_height//2
    safe_zone_sz_x = 100
    safe_zone_sz_y = 100

    centers = None

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, image = cap.read()
        # remove for jetcam - its native 720
        image = image_resize(image, 1280, 720)

        (corners, ids, rejected) = cv2.aruco.detectMarkers(
            image, arucoDict, parameters=arucoParams)

        if ids is not None:
            centers = ut.calc_centers(corners)
            image = ut.drawAruco(image, ids, corners, centers)

            # only the first Aruco detected will be followed
            # NOTE: need a method to handle multiple Aruco
            center_x, center_y = centers[0]

            (quad_coord_x, quad_coord_y) = ut.cam_coord_to_quadrant_coord(
                (center_x, center_y), (image_center_x, image_center_y))

            # print(center_x, center_y, ' | ', quad_coord_x, quad_coord_y)
            turn_direction = ''
            if quad_coord_x > safe_zone_sz_x:
                turn_direction = 'right'
            elif quad_coord_x < (-safe_zone_sz_x):
                turn_direction = 'left'
            else:
                turn_direction = 'STOP'
            print(center_x, ' | ', quad_coord_x, ' | ', turn_direction)

        cv2.imshow('Input', image)

        c = cv2.waitKey(1)
        if c == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
