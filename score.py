import cv2
import os

# スコアを保存するファイルのパス
SCORE_FILE = 'scores.txt'

def save_score(score):
    with open(SCORE_FILE, 'a') as file:
        file.write(f'{score}\n')

def get_high_scores():
    if not os.path.exists(SCORE_FILE):
        return []
    with open(SCORE_FILE, 'r') as file:
        scores = file.readlines()
    scores = [int(score.strip()) for score in scores]
    scores.sort(reverse=True)
    return scores

def get_last_scores():
    with open(SCORE_FILE, 'r') as file:
        scores = file.readlines()
    last_score = scores[-1].strip()
    return last_score

def display_score_screen(cap, window_name):
    high_scores = get_high_scores()
    last_score = get_last_scores()
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 画像を鏡像にし、スコアを描画
        frame = cv2.flip(frame, 1)
        cv2.putText(frame, 'High Scores:', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, 'Your Scores:', (350, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, f'{last_score}', (350, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        for i, score in enumerate(high_scores[:5], start=1):
            cv2.putText(frame, f'{i}. {score}', (100, 50 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.putText(frame, 'Press "q" to Quit or "r" to Restart', (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # 画像を表示
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            return 'quit'  # 終了
        elif key == ord('r'):
            return 'restart'  # 再スタート
