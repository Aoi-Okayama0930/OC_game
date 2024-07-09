import cv2

def show_start_screen(cap, window_name):
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 画像を鏡像にし、テキストを描画
        frame = cv2.flip(frame, 1)
        cv2.putText(frame, 'Press "s" to Start', (100, 240), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3, cv2.LINE_AA)

        # 画像を表示
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1) & 0xFF

        # "s"キーが押されたらゲームを開始
        if key == ord('s'):
            return
