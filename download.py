# -*- coding: utf-8 -*-
'''
TerastationからCANのログデータをダウンロードする
'''
# ライブラリ
import os

# 自作ライブラリ
import smb_client

# Terastationの設定
ip = '172.24.162.203'
uname = 'share'
upass = 'fujinolab'
hname = 'share'

# CANデータのダウンロード
src_folder = os.path.join('個人用', '13期', '吉田', 'CAN_Data')
dst_folder = './data'

# ダウンロード先フォルダを作る
os.makedirs(dst_folder, exist_ok=True)

# ダウンロードの実行
with smb_client.smb_client(uname, upass, hname, ip) as c:
    c.get_files_by_folder(src_folder, dst_folder)