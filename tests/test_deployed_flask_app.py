import os
import json
import requests

BASE_URL = os.getenv("FLASK_SERVER_URL")


def test_main_page_status():
    resp = requests.get(f"{BASE_URL}")
    assert resp.status_code == 200


def test_test_page():
    resp = requests.get(f"{BASE_URL}test")
    assert resp.status_code == 200
    assert resp.text == "test"


def test_predict():
    # Additional headers.
    headers = {"Content-Type": "application/json"}
    # Body
    payload = {
        "url": "https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U"
    }
    resp = requests.post(
        f"{BASE_URL}predict", headers=headers, data=json.dumps(payload, indent=4)
    )
    resp_json = resp.json()
    assert resp.status_code == 200
    expected = {"class_id": "n02099712", "class_name": "Labrador_retriever"}
    assert len(resp_json) == len(expected)
    for item, expected_item in zip(resp_json.items(), expected.items()):
        assert item[0] == expected_item[0]
        assert item[1] == expected_item[1]
    
    print("\n\nPredict Results")
    print("---------------------------------------------------------")
    print("Input:")
    print(payload)
    print("Output:")
    print(resp_json)
    print("-----------------------------------------------------------")
    