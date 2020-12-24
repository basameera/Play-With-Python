import setup_path
import cv2
from jetcam.csi_camera import CSICamera
import utils as ut


if __name__ == "__main__":
    arucoDict, arucoParams = ut.aruco_init()

    width=1280
    height=720
    camera = CSICamera(width=width, height=height, capture_width=1280,
                    capture_height=720, capture_fps=30, flip_mode=2)

    while True:
        image = camera.read()

        (corners, ids, rejected) = cv2.aruco.detectMarkers(
            image, arucoDict, parameters=arucoParams)

        if ids is not None:
            image = ut.drawAruco(image, ids, corners)

        cv2.imshow('Input', image)

        c = cv2.waitKey(1)
        if c == 27:
            break

    cv2.destroyAllWindows()
