# app.py

from flask import Flask, request, render_template
from order_service import calculate_total
import db
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # 你的表單頁面

@app.route("/order", methods=["POST"])
def order():
    # 口味（單選）
    flavor_choice = request.form.get("flavor")  # 例如 "豚骨"

    # 加料（可複選）
    topping_choices = request.form.getlist("toppings")  # 例如 ["叉燒", "加麵"]

    # 過濾掉空值（處理「無加料」的情況）
    topping_choices = [t for t in topping_choices if t]

    # 計算總金額
    total = calculate_total(flavor_choice, topping_choices)

    # 成功頁顯示加料，如果沒有勾選就顯示「無」
    display_toppings = topping_choices if topping_choices else ["無"]

    return render_template(
        "order_success.html",
        flavor=flavor_choice,
        toppings=display_toppings,
        total=total
    )

    # ⭐ 存進資料庫
    db.insert_order(flavor_choice, topping_choices, total)

    display_toppings = topping_choices if topping_choices else ["無"]

    return render_template(
        "order_success.html",
        flavor=flavor_choice,
        toppings=display_toppings,
        total=total
    )

if __name__ == "__main__":
    db.create_tables()  # ⭐ 啟動時確保 table 存在
    app.run(debug=True)
