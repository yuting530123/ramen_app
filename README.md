<<<<<<< HEAD
拉麵點餐機 Web App

這是一個使用 Python Flask 開發的簡易拉麵點餐系統，
使用者可以透過網頁介面選擇拉麵品項並送出訂單，
後端會將訂單資料儲存至 PostgreSQL 資料庫。

本專案同時支援：

本機端開發（Local）

Render 雲端部署（Production）

🔧 使用技術

Python 3

Flask

PostgreSQL

HTML / CSS / JavaScript

Render（雲端部署）

Git / GitHub（版本控制）

📂 專案結構
ramen-ordering-system/
├── app.py                  # Flask 主程式
├── requirements.txt        # Python 套件清單
├── Procfile                # Render 部署設定
├── templates/
│   ├── index.html          # 點餐頁面
│   └── order_success.html  # 訂單成功頁
├── static/
│   ├── style.css
│   └── scripts.js
└── README.md

⚙️ 功能介紹

使用者可在網頁上選擇拉麵品項

送出訂單後，資料會寫入 PostgreSQL

訂單成功後顯示成功畫面

支援本機與雲端資料庫環境切換

🧠 環境設定說明
本機端（Local）

建立虛擬環境

python -m venv venv


啟動虛擬環境
（Windows）

venv\Scripts\activate


安裝套件

pip install -r requirements.txt


設定環境變數（資料庫連線）

DATABASE_URL=postgresql://user:password@localhost:5432/dbname


啟動伺服器

python app.py

☁️ Render 雲端部署

使用 Render 提供的 PostgreSQL Database

資料庫連線字串透過 Render 的 Environment Variables 設定

app.py 會根據 DATABASE_URL 自動連線至正確的資料庫

📝 備註

本機 PostgreSQL 與 Render PostgreSQL 為 不同資料庫

本專案已避免將虛擬環境（venv）上傳至 GitHub

專案目的為展示 Flask + PostgreSQL 的基本 Web 開發與部署流程
=======
# ramen-ordering-system
拉麵點餐系統
>>>>>>> a1c16142bb68f00d0104c517f326bcd729081870
