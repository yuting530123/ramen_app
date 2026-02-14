# order_service.py

# 拉麵口味價格字典
FLAVOR_PRICE = {
    "豚骨": 180,
    "味噌": 170,
    "鹽味": 160
}

# 加料價格字典
TOPPING_PRICE = {
    "叉燒": 30,
    "溏心蛋": 15,
    "加麵": 20
}

def calculate_total(flavor_name, topping_names):
    """
    計算總金額
    :param flavor_name: 字串，拉麵口味名稱
    :param topping_names: list，勾選的加料名稱列表
    :return: int 總金額
    """
    total = FLAVOR_PRICE[flavor_name]
    for t in topping_names:
        total += TOPPING_PRICE[t]
    return total
