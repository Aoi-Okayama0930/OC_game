import cv2
from start import show_start_screen
from game import game_loop, initialize_game, get_score
from score import save_score, display_score_screen
import finish_scene

# ウィンドウの設定
window_name = 'Pose Game'
cv2.namedWindow(window_name)
cv2.moveWindow(window_name, 100, 100)  # ウィンドウの位置を調整

# カメラの設定
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # スタート画面の表示
    show_start_screen(cap, window_name)

    # ゲームの初期化
    initialize_game()

    # ゲームループの実行
    game_loop(cap, window_name)

    # 結果表示(PC)
    score = get_score()
    print(f'Final Score: {score}')

    # ゲーム終了アニメーションを表示
    finish_scene.finish_scene(cap,window_name)

    # スコアの保存
    save_score(score)

    # スコア表示画面の表示
    action = display_score_screen(cap, window_name)

    # ユーザーの選択に応じて処理を分岐
    if action == 'quit':
        break  # プログラムを終了
    elif action == 'restart':
        continue  # ループの先頭に戻り、ゲームを再スタート

cap.release()
cv2.destroyAllWindows()
