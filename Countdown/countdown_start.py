import cv2
import time
import numpy as np

def countdown_start(cap, window_name):
    start_time = time.time()
    animation_duration = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 画像を鏡像にし、スコアを描画
        frame = cv2.flip(frame, 1)

        elapsed_time = time.time() - start_time

        if elapsed_time > animation_duration:
            break

        # アニメーションの内容を描画
        alpha = elapsed_time / animation_duration
        overlay = frame.copy()
        cv2.putText(overlay, 'START', (150, 240), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0), 10, cv2.LINE_AA)
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
