import setup_path
import cv2
from jetcam.csi_camera import CSICamera
import utils as ut
from jetbot_fs import Robot
import time

image_height = 720
image_width = 1280

image_height = 360
image_width = 640

image_center_x = image_width//2
image_center_y = image_height//2
safe_zone_sz_x = 100
safe_zone_sz_y = 100

centers = None

if __name__ == "__main__":

    # init aruco settings
    arucoDict, arucoParams = ut.aruco_init()

    # init robot
    robot = Robot()

    # init camera
    camera = CSICamera(width=image_width, height=image_height, capture_width=1280,
                       capture_height=720, capture_fps=30, flip_mode=2)

    while True:
        image = camera.read()
        st = time.time()
        (corners, ids, rejected) = cv2.aruco.detectMarkers(
            image, arucoDict, parameters=arucoParams)
        elapsed_tm = int((time.time()-st)*1000)
        print(elapsed_tm, "ms", end=' | ')
        if ids is not None:
            centers = ut.calc_centers(corners)
            image = ut.drawAruco(image, ids, corners, centers)

            # only the first Aruco detected will be followed
            # NOTE: need a method to handle multiple Aruco
            center_x, center_y = centers[0]
            # print(center_x, center_y)
            (quad_coord_x, quad_coord_y) = ut.cam_coord_to_quadrant_coord(
                (center_x, center_y), (image_center_x, image_center_y))

            # print(center_x, center_y, ' | ', quad_coord_x, quad_coord_y)
            turn_direction = ''
            if quad_coord_x > safe_zone_sz_x:
                turn_direction = 'right'
                robot.right(0.3)
            elif quad_coord_x < (-safe_zone_sz_x):
                turn_direction = 'left'
                robot.left(0.3)
            else:
                turn_direction = 'STOP'
                robot.stop()
            print(center_x, ' | ', quad_coord_x, ' | ', turn_direction, end=' | ')

        else:
            robot.stop()

        print()

        cv2.imshow('Input', image)

        c = cv2.waitKey(1)
        if c == 27:
            break

    cv2.destroyAllWindows()
    robot.stop()
