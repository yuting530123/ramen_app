import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from order_service import calculate_total


#  正常情境
def test_normal_order():
    result = calculate_total("豚骨", ["溏心蛋", "叉燒"])
    assert result == 180 + 15 + 30


# 沒有加料
def test_no_toppings():
    result = calculate_total("豚骨", [])
    assert result == 180


# 錯誤口味
def test_invalid_flavor():
    with pytest.raises(KeyError):
        calculate_total("不存在的口味", ["溏心蛋"])


# 錯誤加料
def test_invalid_topping():
    with pytest.raises(KeyError):
        calculate_total("豚骨", ["不存在的料"])


# 空值
def test_empty_topping():
    result = calculate_total("豚骨", ["", "溏心蛋"])
    assert result == 180 + 15

# 重複加料 
def test_multiple_same_topping():
    result = calculate_total("豚骨", ["溏心蛋", "溏心蛋"])
    assert result == 180 + 15 * 2