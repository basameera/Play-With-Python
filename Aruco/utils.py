import cv2
import numpy as np


def aruco_init():
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
    arucoParams = cv2.aruco.DetectorParameters_create()
    return arucoDict, arucoParams


def drawAruco(image, ids, corners):
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

            image = cv2.putText(image, str(value[0]), tuple(corners_sq[0]), font,
                                fontScale, (255, 0, 0), thickness, cv2.LINE_AA)

    return image


if __name__ == "__main__":
    pass
