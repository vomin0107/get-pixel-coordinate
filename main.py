import numpy as np
from math import pi, sin, cos, tan

if __name__ == '__main__':
    ## 주어진 월드좌표계의 단위를 mm로 상정하고 진행
    # 주어진 점의 월드좌표
    X = 100
    Y = 100
    Z = 0

    # 주어진 카메라의 월드 좌표
    Xcam = -1000
    Ycam = 0
    Zcam = 1000

    # 주어진 카메라 좌표계와 월드 좌표계를 비교했을 때 카메라의 pan, tilt 각도
    p = -pi / 2
    t = -pi / 4

    # 초점 거리 - 임의의 값 대입
    f = 3

    # 카메라 센서 사이즈 가로/세로 사이즈 - 임의의 값 대입
    ws = 3.674
    hs = 2.760

    # 영상 해상도 - 임의의 값 대입
    wi = 640
    hi = 480

    # 주점, 영상의 중심이라고 가정
    cx = wi / 2
    cy = hi / 2

    # 주어진 점의 월드 좌표를 카메라 좌표계로 변환
    cam_coordinate_p = np.dot(np.array([[cos(p), sin(p), 0],
                                        [-sin(p)*sin(t), cos(p)*sin(t), -cos(t)],
                                        [-sin(p)*cos(t), cos(p)*cos(t), sin(t)]]),
                              (np.array([[X], [Y], [Z]]) - np.array([[Xcam],[Ycam],[Zcam]])))

    # 주어진 점을 카메라 좌표계계로 변환하여 구한 좌표
    Xc = cam_coordinate_p[0]
    Yc = cam_coordinate_p[1]
    Zc = cam_coordinate_p[2]

    # 카메라 센서상에 주어진 점의 상이 맺히는 위치
    xs = f * Xc / Zc
    ys = f * Yc / Zc

    # 영상 내에 주어진 점의 픽셀 좌표
    x = xs * wi / ws + cx
    y = ys * hi / hs + cy

    print('x:', x,'y:', y)