import cv2

# ウィンドウの設定
window_name = 'Pose Game'
cv2.namedWindow(window_name)
cv2.moveWindow(window_name, 100, 100)  # ウィンドウの位置を調整

# カメラの設定
width = 640
height = 480
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# game設定
point_radius = 10 # playerの判定範囲