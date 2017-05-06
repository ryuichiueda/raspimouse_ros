[![Build Status](https://travis-ci.org/ryuichiueda/raspimouse_ros.svg?branch=master)](https://travis-ci.org/ryuichiueda/raspimouse_ros)

こちらは書籍用に開発をストップして、新しいバージョンに移行します。

* 新しいバージョン: https://github.com/ryuichiueda/raspimouse_ros_2

# Raspberry Pi Mouse制御用基盤ROSパッケージ

## 使い方

1. Ubuntu Linux 14.04をインストール
  - 参考: https://wiki.ubuntu.com/ARM/RaspberryPi
1. ROSのインストールとセットアップ
  - https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu14.04_server
1. Raspberry Pi Mouseのドライバをセットアップ
  - 参考: https://github.com/rt-net/RaspberryPiMouse 
1. ワークスペースを作成と当リポジトリのclone

        $ mkdir -p catkin_ws/src
        $ cd ~/catkin_ws/src
        $ catkin_init_workspace
        $ git clone https://github.com/ryuichiueda/raspimouse_ros.git
        $ cd ..
        $ catkin_make

1. ~/.bashrcに以下の1行がない場合、追加し、ログアウト/ログイン

        source /home/ubuntu/catkin_ws/devel/setup.bash

1. ベースシステムの起動

        $ roscd raspimouse_ros/
        $ roslaunch raspimouse_ros raspimouse.launch 

1. チェックスクリプトの実行

        $ rosrun raspimouse_ros check_driver_io.py 



## 動作確認した環境

- Ubuntu Linux 14.04 server on Raspberry Pi 2
