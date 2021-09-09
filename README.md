# SMB_downloader
SMBサーバからファイルをダウンロードする

## 使いみち
大きなデータ(画像や波形、ログファイルなど)は、Gitで管理するにはおもすぎる  
そのため、テラなどのファイルサーバにおいておき、必要なときに必要な人がダウンロードできるように
Gitとは別で管理するのが望ましい。 
このプログラムを使うと、接続先とダウンロードフォルダを指定するだけでファイルのダウンローダを作れる。　　

## 使用例

```python
# uname: SMBサーバのユーザ名
# upass: SMBサーバのパスワード
# hname: SMBサーバのルートフォルダ名 (e.g. share)
# ip: SMBサーバのIPアドレス
# src_folder: ダウンロード元のフォルダパス (hnameは除く)
# dst_folder: ダウンロード先のフォルダパス
with smb_client.smb_client(uname, upass, hname, ip) as c:
    c.get_files_by_folder(src_folder, dst_folder)
```