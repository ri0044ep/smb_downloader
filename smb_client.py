# -*- coding: utf-8 -*-
'''
Terastationからファイルをダウンロードしてくる
'''

# import pip install pysmb
from smb.SMBConnection import SMBConnection
import platform
import os

class smb_client:
    def __init__(self, username, password, remote_name, ip):
        self.conn = SMBConnection(username, password, platform.node(), remote_name)
        self.ip = ip
    
    def __enter__(self):
        self.conn.connect(self.ip, 139)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()
    
    def get_file(self, src_folder, dst_folder, file_name):
        '''
        <src_folder>内にある<file_name>を<dst_folder>にダウンロード
        '''
        with open(os.path.join(dst_folder, file_name), 'wb') as f:
            print('downloading : {}'.format(os.path.join(src_folder, file_name)))
            self.conn.retrieveFile('share', os.path.join(src_folder, file_name), f)
    
    def get_file_list(self, src_folder, pattern='*'):
        '''
        <src_folder>内にある<pattern>に合致するファイル一覧を取得
        ※returnはSharedFileオブジェクトのリスト
        '''
        return self.conn.listPath('share', '/'+src_folder, pattern=pattern)[2:]
    
    def get_files_by_folder(self, src_folder, dst_folder, pattern='*'):
        '''
        <src_folder>内にある<pattern>に合致するファイルをすべて<dst_folder>にダウンロード
        フォルダ構造を保って再帰的に行う
        '''
        files = self.get_file_list(src_folder, pattern=pattern)
        for f in files:
            if f.isDirectory:
                os.makedirs(os.path.join(dst_folder, f.filename), exist_ok=True)
                self.get_files_by_folder(os.path.join(src_folder, f.filename), os.path.join(dst_folder, f.filename))
            else:
                self.get_file(src_folder, dst_folder, f.filename)


if __name__ == "__main__":
    ip = '172.24.162.203'
    uname = 'share'
    upass = 'fujinolab'
    hname = 'share'
    
    src_folder = os.path.join('個人用', '13期', '吉田', 'CAN_Data')
    dst_folder = './data'
    
    os.makedirs(dst_folder, exist_ok=True)
    
    with smb_client(uname, upass, hname, ip) as c:
        c.get_files_by_folder(src_folder, './')