# JSON 自動修正ツール (fixjson)

## 概要

これは、不正なエスケープシーケンスや特定の不要な文字列（``など）を含むJSONライクなテキストを、妥当なJSON形式に修正・整形するためのWebアプリケーションである。

修正されたJSONは、インデント付きで見やすく表示され、ワンクリックでクリップボードにコピーすることが可能だ。

## 主な機能

* **不正なエスケープの修正**: `\` が不適切に使用されている箇所（例: `\"` とすべきでない箇所での `\`）を自動的に修正する。
* **不要な文字列の削除**: `` などの特定の文字列をあらかじめ除去する。
* **JSON整形 (Pretty Print)**: 修正後のJSONをインデント（2スペース）付きで整形して表示する。
* **クリップボードコピー**: 整形後の結果をボタン一つでコピーできる。

## サイトURL

`https://fixjson.onrender.com/`

## 使用技術

* **バックエンド**: Python, Flask
* **WSGIサーバー**: Gunicorn (デプロイ時)
* **フロントエンド**: HTML, JavaScript (Clipboard API)

## ローカル環境での実行方法

1.  このリポジトリをクローンする。
    ```bash
    git clone (リポジトリのURL)
    cd fixjson
    ```

2.  (推奨) Pythonの仮想環境を作成し、有効化する。
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux の場合
    # venv\Scripts\activate   # Windows の場合
    ```

3.  必要なライブラリをインストールする。
    ```bash
    pip install -r requirements.txt
    ```

4.  Flaskアプリケーションを実行する。
    ```bash
    python fix_json_app.py
    ```

5.  ブラウザで `http://127.0.0.1:5000` にアクセスする。

## デプロイ

このアプリケーションは、`requirements.txt` と `gunicorn` を使用することで、Render.comのようなPaaS（Platform as a Service）に容易にデプロイ可能である。

* **Build Command**: `pip install -r requirements.txt`
* **Start Command**: `gunicorn fix_json_app:app`