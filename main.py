import numpy as np
import cv2
import time

def draw_marker(i):
    tag = np.zeros((300, 300, 1), dtype="uint8")
    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
    cv2.aruco.drawMarker(arucoDict, i, 300, tag, 1)
    # cv2.imwrite(args["output"], tag)
    cv2.imshow("ArUCo Tag", tag)
    cv2.waitKey(0)

def detect_marker(image, arucoDict, arucoParams):
    (corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)
    print(corners)
    print(ids)
    points = corners[0].astype(np.int32)
    print(points)
    cv2.polylines(image, points, True, (0,255,0), thickness=2)
    cv2.imshow('window', image)
    cv2.waitKey(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # for i in range(50):
    #     draw_marker(i)

    arucoDict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_50)
    arucoParams = cv2.aruco.DetectorParameters_create()
    image = cv2.imread('test.jpg')

    start = time.time()

    detect_marker(image, arucoDict, arucoParams)

    done = time.time()
    print(f'done in {1/(done - start)}fps')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
