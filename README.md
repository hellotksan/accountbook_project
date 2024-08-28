# 家計簿アプリケーション

## 起動、使用順序

### FastAPI サーバを立ち上げる

```bash
uvicorn dbaccess:app --reload
```

### python ファイルでアプリケーションを実行する

### NextJS の web サーバを立ち上げる

- local の場合

```bash
npm run dev
```

- その他、AWS なら Amplify でデプロイ。サーバを使うと難しそう。

## フォルダ構成

```bash
├── accountbook/
│   ├── app/
│   │   ├── crud/
│   │   │   ├── accountbook.py  # 家計簿アプリケーションのメインファイル
│   │   │   ├── accountbook_register.py  # 家計簿アプリの登録モジュール
│   │   │   ├── ...
│   │   │   ├── input_utils.py  # 共通の入力処理を提供するモジュール群
│   │   ├── dbaccess.py  # FastAPIのエントリーポイント兼エンドポイント
│   │   ├── requirements.txt
│   ├── db/
│   │   ├── accountbook.dmp  # accountbookデータベースのdmpファイル
│   │   ├── db_schema.sql  # データベースのスキーマ定義SQLファイル
│   │   ├── dummydata.sql  # ダミーデータのSQLファイル
│   ├── docs/
│   │   ├── 2024-08-27 17-44-54.mkv  # 実際に使用している模擬動画
│   │   ├── 単体テスト項目書.xlsx  # 単体テスト項目書
│   ├── my-household-budget-app/  # 家計簿アプリのnextJsでデプロイしたwebアプリプロジェクト
│   │   ├── app/
│   │   │   ├── favicon.ico
│   │   │   ├── globals.css  # tailwindcssのCSSファイル
│   │   ├── components/
│   │   │   ├── piechart/  # 一か月の家計簿を円グラフにして表示するコンポーネント
│   │   │   │   ├── index.py
│   │   ├── lib/
│   │   │   ├── api.js  # apiのエンドポイントURLを格納しておくファイル
│   │   ├── pages/
│   │   │   ├── index.py  # ルートで表示するページ
│   │   │   ├── register/  # 登録する処理を表示するページ
│   │   │   │   ├── index.py
│   │   │   ├── ...
```

## おまけ: おそらく最適構成

```bash
├── accountbook/
│   ├── nextjs_frontend_app/
│   │   ├── ...
│   ├── fastapi_backend_project/
│   │   ├── ...
│   ├── docs/
│   │   ├── ...
│   ├── README.md
```

```bash
accountbook_fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py  # エントリーポイント
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py  # ユーザー関連のエンドポイント
│   │   │   │   ├── items.py  # アイテム関連のエンドポイント
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py  # 設定関連
│   │   ├── security.py  # セキュリティ関連（JWTやOAuth2）
│   ├── crud/
│   │   ├── __init__.py
│   │   ├── users.py  # ユーザー関連のCRUD操作
│   │   ├── items.py  # アイテム関連のCRUD操作
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py  # 全てのモデルのベースクラス
│   │   ├── session.py  # データベース接続設定
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py  # ユーザーモデル
│   │   ├── item.py  # アイテムモデル
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py  # ユーザー用Pydanticモデル
│   │   ├── item.py  # アイテム用Pydanticモデル
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_users.py  # ユーザー関連のテスト
│   │   ├── test_items.py  # アイテム関連のテスト
├── alembic/  # データベースマイグレーション用（Alembic使用時）
│   ├── versions/
│   └── env.py
├── .env  # 環境変数ファイル
├── requirements.txt  # 依存パッケージ
└── Dockerfile  # Docker設定ファイル
```
