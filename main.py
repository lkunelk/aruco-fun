import numpy as np
import cv2
import time

def draw_marker():
    tag = np.zeros((300, 300, 1), dtype="uint8")
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
    cv2.aruco.drawMarker(arucoDict, 1, 300, tag, 1)
    # cv2.imwrite(args["output"], tag)
    cv2.imshow("ArUCo Tag", tag)
    cv2.waitKey(0)

def detect_marker():
    image = cv2.imread('marker.jpg')
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
    arucoParams = cv2.aruco.DetectorParameters_create()

    start = time.time()
    (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)
    done = time.time()
    print(f'done in {1/(done - start)}fps')
    print(ids)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # draw_marker()
    detect_marker()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
