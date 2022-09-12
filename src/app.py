import os
from PIL import Image
import requests
from io import BytesIO


import requests
from PIL import Image
from flask import Blueprint, jsonify, request
from model.model_handler import Classifier

from flask import Flask


def _read_image(url):
    response = requests.get(url)
    file_stream = Image.open(BytesIO(response.content))

    return file_stream


def initialize():
    model = Classifier()
    model.initialize()
    return model


def run(url):
    image = _read_image(url)
    input_ = model.preprocess(image)
    output_ = model.inference(input_)
    result = model.postprocess(output_)

    return result


model = initialize()
route_blueprint = Blueprint("route_blueprint", __name__)


@route_blueprint.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        content = request.json
        class_id, class_name = run(content["url"])
        return jsonify({"class_id": class_id, "class_name": class_name})


@route_blueprint.route("/")
def main_page():
    super_secret = os.getenv("SECRET_VALUE")
    return f"{super_secret}</p>"


@route_blueprint.route("/test")
def test_page():
    return "test"


def create_app():
    app = Flask(__name__)
    app.register_blueprint(route_blueprint)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
