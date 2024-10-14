＜フォルダの説明＞
Music:音楽ファイル(mp3)等を置いている．音楽を鳴らすのはpygameを使用
Game:ゲームモードの内容．
Countdown:MenueモードからGameモードへ切り替える際のカウントダウン部分の記載．

＜ファイルの説明＞
main.py:各ファイルを呼び出したりしている．ゲームの流れの記載．
start.py:スタート画面の構成．
game.py:ゲームの当たり判定やプレイヤー，タッチポイントの描画．
score.py:スコア画面の構成．
score.txt:スコアのデータの保存．
finish_scene.py:終了画面の構成．



__pycache__:pythonを実行したキャッシュが残されたファイルです．消しても問題ありませんが，実行時間が少し短くなるかも．．．

＜環境構築注意点＞
pythonを利用しているのでインストールが必須．（例：version:python 3.11.3）
opencvを利用しているのでインストールが必須．
mediapipeを利用しているのでインストールが必須．
main.pyにてカメラの設定を行っているのだが，cap = cv2.VideoCapture(1)でカメラの設定を行っている．Captureする数字は機種によって変更されるため，注意されたい．
aaa
