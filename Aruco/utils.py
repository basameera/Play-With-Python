import cv2
import numpy as np
import yaml


def bound(input_sig, min_val, max_val):
    if input_sig < min_val:
        return min_val
    elif input_sig > max_val:
        return max_val
    else:
        return input_sig

def calc_centers(corners):
    centers = list()
    for corner in corners:
        corners_sq = np.squeeze(corner)
        # center of aruco
        # center_x = (x1 + x3)//2
        # center_y = (y1 + y3)//2
        center_x = int((corners_sq[0, 0] + corners_sq[2, 0])/2)
        center_y = int((corners_sq[0, 1] + corners_sq[2, 1])/2)
        centers.append([center_x, center_y])
    return centers


def cam_coord_to_quadrant_coord(image_coord, center_coord):
    quad_coord_x = image_coord[0] - center_coord[0]
    quad_coord_y = center_coord[1] - image_coord[1]
    return (quad_coord_x, quad_coord_y)


def aruco_init():
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
    arucoParams = cv2.aruco.DetectorParameters_create()
    return arucoDict, arucoParams


def drawAruco(image, ids, corners, centers=None):
    color = (0, 0, 255)
    thickness = 2
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.6

    if len(ids) > 0:

        for n, value in enumerate(ids):
            corners_sq = np.squeeze(corners[n])
            image = cv2.line(image, tuple(corners_sq[0]), tuple(
                corners_sq[1]), color, thickness)
            image = cv2.line(image, tuple(corners_sq[1]), tuple(
                corners_sq[2]), color, thickness)
            image = cv2.line(image, tuple(corners_sq[2]), tuple(
                corners_sq[3]), color, thickness)
            image = cv2.line(image, tuple(corners_sq[3]), tuple(
                corners_sq[0]), color, thickness)

            area = PolygonArea(corners_sq)

            image = cv2.putText(image, str(value[0]) + ' [' + str(area) + ']', tuple(corners_sq[0]), font,
                                fontScale, (255, 0, 0), thickness, cv2.LINE_AA)

            if centers is not None:
                image = cv2.putText(image, str(centers[n]), tuple(centers[n]), font,
                                    fontScale, (0, 255, 0), thickness, cv2.LINE_AA)

    return image


def PolygonArea(corners):
    # https://stackoverflow.com/questions/24467972/calculate-area-of-polygon-given-x-y-coordinates
    n = len(corners)  # of corners
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area


def read_calibration_ros(fname="calibration_matrix.yaml"):
    with open(fname, "r") as f:
        calib_data = yaml.load(f, Loader=yaml.FullLoader)
    camera_matrix = np.asarray(
        calib_data['camera_matrix']['data'], dtype=np.float).reshape(3, 3)
    dist_coeff = np.asarray(
        calib_data['distortion_coefficients']['data'], dtype=np.float)
    return camera_matrix, dist_coeff


def resize_image_w_dim(img, dim=(320, 240), inter=cv2.INTER_AREA):
    '''
    dim = (width, height)
    '''
    return cv2.resize(img, dim, interpolation=inter)


def aspect_validate(w_aspect=16, h_aspect=9, w_val=16, h_val=9):
    target_aspect_ratio = h_aspect/w_aspect  # 9/16

    # try to choose the best side to crop out an image with target aspect ratio
    h_crop = 0
    w_crop = 0

    aspect_ratio = h_val/w_val
    if (aspect_ratio <= target_aspect_ratio):
        principle_axis = 'h'
        h_crop = h_val
        w_crop = (w_aspect * h_crop)/h_aspect
    elif (aspect_ratio > target_aspect_ratio):
        principle_axis = 'w'
        w_crop = w_val
        h_crop = (h_aspect * w_val)/w_aspect
    return int(w_crop), int(h_crop)


if __name__ == "__main__":
    pass
