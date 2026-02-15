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
    try:
        flavor_choice = request.form.get("flavor")
        topping_choices = request.form.getlist("toppings")
        topping_choices = [t for t in topping_choices if t]

        total = calculate_total(flavor_choice, topping_choices)

        # ⭐ 資料庫存檔
        db.insert_order(flavor_choice, topping_choices, total)

        display_toppings = topping_choices if topping_choices else ["無"]

        return render_template(
            "order_success.html",
            flavor=flavor_choice,
            toppings=display_toppings,
            total=total
        )
    except Exception as e:
        # 將錯誤直接印在頁面上，方便 Debug
        return f"Error: {e}"


if __name__ == "__main__":
    db.create_tables()
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


@app.route("/orders")
def orders():
    orders = db.get_orders()
    return render_template("orders.html", orders=orders)
