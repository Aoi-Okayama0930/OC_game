import cv2
import mediapipe as mp
import numpy as np
import random
import Game.game as game

# MediaPipe Pose初期化
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

def draw_avatar(frame, landmarks):
    # 頭部の描画
    head_pos = (int(landmarks[mp_pose.PoseLandmark.NOSE].x * 640), int(landmarks[mp_pose.PoseLandmark.NOSE].y * 480))
    cv2.circle(frame, head_pos, 5, (0, 255, 0), -1)

    # 体の各部位を線でつなぐ
    connections = [
        (mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.RIGHT_SHOULDER),
        (mp_pose.PoseLandmark.LEFT_SHOULDER, mp_pose.PoseLandmark.LEFT_ELBOW),
        (mp_pose.PoseLandmark.LEFT_ELBOW, mp_pose.PoseLandmark.LEFT_WRIST),
        (mp_pose.PoseLandmark.RIGHT_SHOULDER, mp_pose.PoseLandmark.RIGHT_ELBOW),
        (mp_pose.PoseLandmark.RIGHT_ELBOW, mp_pose.PoseLandmark.RIGHT_WRIST),
        (mp_pose.PoseLandmark.LEFT_HIP, mp_pose.PoseLandmark.RIGHT_HIP),
        (mp_pose.PoseLandmark.LEFT_HIP, mp_pose.PoseLandmark.LEFT_KNEE),
        (mp_pose.PoseLandmark.LEFT_KNEE, mp_pose.PoseLandmark.LEFT_ANKLE),
        (mp_pose.PoseLandmark.RIGHT_HIP, mp_pose.PoseLandmark.RIGHT_KNEE),
        (mp_pose.PoseLandmark.RIGHT_KNEE, mp_pose.PoseLandmark.RIGHT_ANKLE)
    ]

    for connection in connections:
        point1 = (int(landmarks[connection[0]].x * 640), int(landmarks[connection[0]].y * 480))
        point2 = (int(landmarks[connection[1]].x * 640), int(landmarks[connection[1]].y * 480))
        cv2.line(frame, point1, point2, (255, 255, 255), 5)

