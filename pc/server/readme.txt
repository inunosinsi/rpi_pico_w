PCの方で使用する。
Raspberry Pi 400を想定

このファイル(readme.txt)があるディレクトリまで移動して下記のコマンドを実行する
$ python3 -m http.server 8000
実行後にブラウザでhttp://localhost:8000にアクセスする

他の端末のクライアントからアクセスする時、下記コマンドで自身のIPアドレスを調べておく
$ hostname -I
