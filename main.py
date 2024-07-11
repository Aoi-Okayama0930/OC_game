import cv2
from start import show_start_screen
from Game.game import game_loop, initialize_game, get_score
from score import save_score, display_score_screen
import finish_scene
import Music.bgm as bgm
import Countdown.countdown_main as down

# BGMファイルのパス
BGM_MENUE = 'c:/Users/81908/Desktop/研究室/OpenCanpus/OC_game/Music/free2.mp3'
BGM_GAME = 'c:/Users/81908/Desktop/研究室/OpenCanpus/OC_game/Music/free1.mp3'
SOUND_EFFECT_FINISH = 'c:/Users/81908/Desktop/研究室/OpenCanpus/OC_game/Music/Finish_SE.mp3'
SOUND_EFFECT_TRANSITION = 'c:/Users/81908/Desktop/研究室/OpenCanpus/OC_game/Music/SE1.mp3'
SOUND_EFFECT_TRANSITION2 = 'c:/Users/81908/Desktop/研究室/OpenCanpus/OC_game/Music/SE2.mp3'


# ウィンドウの設定
window_name = 'Pose Game'
cv2.namedWindow(window_name)
cv2.moveWindow(window_name, 100, 100)  # ウィンドウの位置を調整

# カメラの設定
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# BGMの初期化
bgm.initialize_bgm()

while True:
    # スタート画面の表示
    bgm.play_bgm(BGM_MENUE)
    show_start_screen(cap, window_name)
    bgm.play_sound_effect(SOUND_EFFECT_TRANSITION)

    # Countdown画面の表示
    bgm.stop_bgm()
    down.countdown_main(cap,window_name)

    # ゲームの初期化
    initialize_game()

    # ゲームループの実行
    bgm.play_bgm(BGM_GAME)
    game_loop(cap, window_name)

    # 結果表示(PC)
    score = get_score()
    print(f'Final Score: {score}')

    # ゲーム終了アニメーションを表示
    bgm.stop_bgm()
    bgm.play_sound_effect(SOUND_EFFECT_FINISH)
    finish_scene.finish_scene(cap,window_name)

    # スコアの保存
    save_score(score)

    # スコア表示画面の表示
    bgm.play_bgm(BGM_MENUE)
    action = display_score_screen(cap, window_name)

    # ユーザーの選択に応じて処理を分岐
    if action == 'quit':
        break  # プログラムを終了
    elif action == 'restart':
        bgm.play_sound_effect(SOUND_EFFECT_TRANSITION2)
        continue  # ループの先頭に戻り、ゲームを再スタート

cap.release()
cv2.destroyAllWindows()
