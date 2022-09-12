import pytest
import json
from app import create_app


@pytest.fixture
def api():
    app = create_app()
    api = app.test_client()
    return api


def test_predict(api):
    resp = api.post(
        "/predict",
        data=json.dumps(
            {
                "url": "https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U"
            }
        ),
        content_type="application/json",
    )
    resp_json = json.loads(resp.data.decode("utf-8"))
    expected = {"class_id": "n02099712", "class_name": "Labrador_retriever"}
    assert len(resp_json) == len(expected)
    for item, expected_item in zip(resp_json.items(), expected.items()):
        assert item[0] == expected_item[0]
        assert item[1] == expected_item[1]
