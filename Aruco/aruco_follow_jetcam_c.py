# with Robot + undistortion - CV window
import setup_path
import cv2
from jetcam.csi_camera import CSICamera
import utils as ut
from jetbot_fs import Robot
import time
import os

image_height = 720
image_width = 1280

# image_height = 360
# image_width = 640


safe_zone_sz_x = 50
safe_zone_sz_y = 50

centers = None

path_dir = 'config'
file_calib = 'cam_calib_csi.yml'


# get settings
mtx, dist = ut.read_calibration_ros(os.path.join(path_dir, file_calib))

# calculate new camera matrix
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(
    mtx, dist, (image_width, image_height), 1, (image_width, image_height))

# map
mapx, mapy = cv2.initUndistortRectifyMap(
    mtx, dist, None, newcameramtx, (image_width, image_height), 5)

x, y, w_roi, h_roi = roi
w_crop, h_crop = ut.aspect_validate(16, 9, w_roi, h_roi)
w_crop_half, h_crop_half = int(w_crop//2), int(h_crop//2)
image_center_x = int(image_width/2)
image_center_y = int(image_height/2)
aspect_roi_x = image_center_x - w_crop_half
aspect_roi_y = image_center_y - h_crop_half

robot_turn_speed = 0.1

if __name__ == "__main__":

    # init aruco settings
    arucoDict, arucoParams = ut.aruco_init()

    # init robot
    robot = Robot()
    robot.stop()

    # init camera
    camera = CSICamera(width=image_width, height=image_height, capture_width=1280,
                       capture_height=720, capture_fps=30, flip_mode=2)

    try:
        while True:
            tm = time.time()
            image = camera.read()

            # undistort image - 90ms
            image = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

            # crop roi with aspect ration
            image = image[aspect_roi_y:aspect_roi_y +
                        h_crop, aspect_roi_x:aspect_roi_x+w_crop]

            # resize image - 100ms
            image = ut.resize_image_w_dim(image, dim=(640, 360))

            # et = time.time()-tm

            (corners, ids, rejected) = cv2.aruco.detectMarkers(
                image, arucoDict, parameters=arucoParams)

            if ids is not None:
                h_rz,  w_rz = image.shape[:2]
                rz_center_x = int(w_rz//2)
                rz_center_y = int(h_rz//2)
                centers = ut.calc_centers(corners)
                image = ut.drawAruco(image, ids, corners, centers)

                # only the first Aruco detected will be followed
                # NOTE: need a method to handle multiple Aruco
                center_x, center_y = centers[0]
                # print(center_x, center_y)
                (quad_coord_x, quad_coord_y) = ut.cam_coord_to_quadrant_coord(
                    (center_x, center_y), (rz_center_x, rz_center_y))

                # print(center_x, center_y, ' | ', quad_coord_x, quad_coord_y)
                turn_direction = ''
                if quad_coord_x > safe_zone_sz_x:
                    turn_direction = 'right'
                    robot.right(robot_turn_speed)
                elif quad_coord_x < (-safe_zone_sz_x):
                    turn_direction = 'left'
                    robot.left(robot_turn_speed)
                else:
                    turn_direction = 'STOP'
                    robot.stop()
                print(w_rz, h_rz, ' - ', center_x, ' | ',
                    quad_coord_x, ' | ', turn_direction, end=' | ')

            else:
                robot.stop()

            et = time.time()-tm

            print('   Time:', et)
            
    except KeyboardInterrupt:
        print("\nBye!")

    robot.stop()
