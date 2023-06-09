# src

base用API

## 概要

base用API の AWS Chalice アプリケーション。

## ローカル環境

### 前提

- Python3.9系 をインストール ... [Python DL](https://www.python.org/downloads/)
- フレームワークは [AWS Chalice](https://aws.github.io/chalice/) を利用。
- Pythonの開発は仮想環境(venv)を利用。以下手順はvenvを利用する。
- ローカルのDBはDocker Composeを利用。

### ローカルDB作成

dockerエンジン及びdocker composeをインストールし以下のコマンドでローカル環境用のDBコンテナを作成する。
MySQL & phpMyAdminの環境を作成

```
> cd docker\db
> docker-compose up --build　... コンテナ作成＆起動＆アタッチ
```

DBコンテナ起動/停止

```
> cd docker\db
> docker-compose up　　　　... DBのコンテナを起動＆アタッチ
  起動中に「Ctrl+C」　　　 ... DBのコンテナを停止
```

phpMyAdminへアクセス

http://localhost:8081/index.php


### Python開発環境作成

python仮想環境作成

```
> cd src
> python -m venv venv          ... 仮想環境作成
> .\venv\Scripts\activate      ... 仮想環境に入る
※Trường hợp lỗi "...cannot be loaded because running scripts is disabled on this system" thì mở PS và chạy lệnh sau:
> Get-ExecutionPolicy
> Set-ExecutionPolicy RemoteSigned
(venv) > pip install -r requirements.txt ... 必要なパッケージをインストール
```

Chaliceローカル起動/停止

```
> cd src
> .\venv\Scripts\activate   ... 仮想環境に入る
(venv) > chalice local --stage local --port 8000   ... ローカルでAPIを起動。適宜ポート番号を変更してください。
　　　　 起動中に「Ctrl+C」        　　　　　　 　　... APIを停止。
(venv) > deactivate         ... 仮想環境から出る
```

- chalice localで起動したサーバは「Ctrl-C」で停止できるが、「Ctrl-C」の後にサービスディレクトリ内のいずれかのファイルを更新しないと停止されない。サービスディレクトリ内のファイルが更新された時のリロードで「Ctrl-C」を検知している模様。


## デプロイ

以下のコマンドでデプロイします。

```sh
$ cd src
$ . venv/bin/activate
$ pip install -r requirements.txt　　※既にインストール済であれば不要。
$ chalice deploy --stage {各環境名}　　※環境名は "dev":開発環境、 "stg":ステージング環境、 "prd":本番環境
```

初回のデプロイ後、API Gatewayのオーソライザーは一度「編集」で何も変更せずに「保存」をしないと機能しないので注意！

デフォルト以外の AWS_PROFILE で実行する場合は以下のように環境変数を指定して `chalice deploy` を実行します。

```sh
$ AWS_PROFILE=myawsaccount chalice deploy --stage dev
```

## 参考

- chalice　https://aws.github.io/chalice/
- Docker Compose コマンドリファレンス　https://docs.docker.jp/compose/reference/toc.html
- phpMyAdmin https://www.dbonline.jp/phpmyadmin/

## Coding convention

http://10.32.4.160:3080/ThinhBV/python_chalice_base/-/blob/master/CodingRule/Coding_Convention.xlsx
