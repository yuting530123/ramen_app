import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_order_success(client):
    response = client.post("/order", data={
        "flavor": "豚骨",
        "toppings": ["溏心蛋", "叉燒"]
    })

    assert response.status_code == 200
    assert "豚骨" in response.get_data(as_text=True)

def test_order_no_topping(client):
    response = client.post("/order", data={
        "flavor": "味噌",
        "toppings": []
    })

    assert response.status_code == 200
    assert "味噌" in response.get_data(as_text=True)

def test_order_invalid_flavor(client):
    response = client.post("/order", data={
        "flavor": "不存在的口味",
        "toppings": ["溏心蛋"]
    })

    assert response.status_code == 200
    assert "Error" in response.get_data(as_text=True)

import db

@pytest.fixture(autouse=True)
def mock_db(monkeypatch):
    monkeypatch.setattr(db, "insert_order", lambda *args: None)