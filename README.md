# 勤怠管理用 Entrance and Exit Control Management

Felica CardからIDm を読み込み、Cram Webサービスに送信


## 前準備

* 日本語フォントのインストール
* qt4のインストール
* 必要ライブラリのインストール

```
$ sudo apt-get install ttf-kochi-gothic xfonts-intl-japanese xfonts-intl-japanese-big xfonts-kaname
$ sudo apt-get install python-qt4
$ pip install -r requirements.txt
```

## サービス登録

```
$ sudo ln -s (this repository top) /opt/eaecm
$ vi /etc/eaecm.conf
```

/etc/eaecm.conf

```
CRAM_HOST=XXXX
CRAM_PORT=XXXX
CRAM_TOKEN=XXXX
```
ここで指定するTOKENを、cram側に登録してください。

```
$ sudo cp eaecm.service /etc/systemd/system
```

## サービス起動

```
$ sudo systemctl start eaecm
$ sudo systemctl enable eaecm
```
