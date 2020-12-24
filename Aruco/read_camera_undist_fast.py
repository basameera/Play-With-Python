import setup_path
import os
from jetcam.csi_camera import CSICamera
import cv2
from utils import read_calibration_ros, resize_image_w_dim, aspect_validate
import time

path_dir = 'config'
file_calib = 'cam_calib_csi.yml'
w_og,  h_og = 1280, 720

# get settings
mtx, dist = read_calibration_ros(os.path.join(path_dir, file_calib))

# calculate new camera matrix
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(
    mtx, dist, (w_og, h_og), 1, (w_og, h_og))

# map
mapx, mapy = cv2.initUndistortRectifyMap(
    mtx, dist, None, newcameramtx, (w_og, h_og), 5)

camera = CSICamera(width=w_og, height=h_og, capture_width=1280,
                   capture_height=720, capture_fps=30, flip_mode=2)

x, y, w_roi, h_roi = roi
w_crop, h_crop = aspect_validate(16, 9, w_roi, h_roi)
w_crop_half, h_crop_half = int(w_crop//2), int(h_crop//2)
cx = int(w_og/2)
cy = int(h_og/2)
aspect_roi_x = cx-w_crop_half
aspect_roi_y = cy-h_crop_half

while True:
    tm = time.time()
    # read image - 33ms
    image = camera.read()

    # undistort image - 90ms
    image = cv2.remap(image, mapx, mapy, cv2.INTER_LINEAR)

    # crop roi with aspect ration
    image = image[aspect_roi_y:aspect_roi_y + h_crop, aspect_roi_x:aspect_roi_x+w_crop]

    # resize image - 100ms
    image = resize_image_w_dim(image, dim=(640, 360))

    # show image
    cv2.imshow('JetCam', image)
    key = cv2.waitKey(1)

    if key == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
        print('Done')
        break

    et = time.time()-tm

    print('   Time:', et, end='\r')
