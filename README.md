# Docker + Flask のボイラープレート

## Usage(使い方)
#### 1. このテンプレートrepoから自分のリポジトリを作成
![img](https://i.imgur.com/AlA5ZcQ.png)

#### 2. `.env.sample`を参考に`.env`ファイルを`.env.sample`と同じ場所に作成

#### 3. Dockerを使ってビルド => アップ
__Dockerが入ってないと動きません__  

```bash
$ make build_up
```

これでサーバーがたちます
`http://localhost:8000`
にアクセスすればみれます  


## 基礎フォルダ構造の解説
```text
.
├── Dockerfile              // アプリケーション自体のDockerfile
├── Makefile                // `make XXX`みたいなコマンドでいろんなコマンドを簡略化するためのファいうr
├── README.md               // まず読みましょうというもの
├── .docker                 // アプリケーション以外のdockerで立ち上げるものたち
│   ├── db
│   │   ├── initializers/01_createdb.sql    // サーバー立ち上げた時にこの内容によってデフォルトのROLEとDBができる         
│   │   └── data/           // 実際のデータベースのデータが同期される
│   ├── nginx
│   │   ├── app.conf        // Nginxの設定         
│   │   └── Dockerfile
│   └── redis               // 非同期ジョブ実行の際に使われる揮発性DB
├── app                     // アプリケーションのソースコードが入るフォルダ *1
│   ├── __init__.py
│   ├── application.py      // アプリケーションに様々なパッケージを適用して初期化する
│   ├── config.py           // アプリケーションの設定
│   ├── database.py         // データベースの初期化
│   ├── jobs                // 非同期などで実行したいジョブを入れる
│   │   └── __init__.py
│   ├── lib                 // アプリ内で使う独自ライブラリなどを配置
│   │   └── __init__.py
│   ├── models              // モデルを入れる
│   │   └── __init__.py
│   ├── static              // 画像やスタイルシートを入れる
│   │   ├── img
│   │   ├── javascript
│   │   └── stylesheet
│   ├── tasks.py            // celeryに渡したいジョブやライブラリなどをimport
│   ├── templates           // テンプレートが入る
│   ├── tests               // pytestによって実行したいテストを入れる
│   │   └── __init__.py
│   └── views               // viewが入る => views.pyのように1つのファイルにしてもいい
│       └── __init__.py
├── docker-compose.yml      
├── guniconf.py             // gunicornの設定
├── run.py                  // 起動用ファイル
└── tmp                     // プログラムによって一時的に生成されるファイルなどを格納する用のフォルダ
    └── sockets             // ソケットファイルがはいる

```
`*1` => 独自のプロジェクト名・アプリ名に変えてもいいが、ソースコード内のパッケージ名も変える必要がある