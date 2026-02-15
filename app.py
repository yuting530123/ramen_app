import os
from flask import Flask, request, render_template
from order_service import calculate_total
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/order", methods=["POST"])
def order():
    # 口味（單選）
    flavor_choice = request.form.get("flavor")

    # 加料（可複選）
    topping_choices = request.form.getlist("toppings")
    topping_choices = [t for t in topping_choices if t]

    # 計算總金額
    total = calculate_total(flavor_choice, topping_choices)

    # ⭐ 先存進資料庫（一定要在 return 前）
    db.insert_order(flavor_choice, topping_choices, total)

    # 顯示用
    display_toppings = topping_choices if topping_choices else ["無"]

    return render_template(
        "order_success.html",
        flavor=flavor_choice,
        toppings=display_toppings,
        total=total
    )

if __name__ == "__main__":
    db.create_tables()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
