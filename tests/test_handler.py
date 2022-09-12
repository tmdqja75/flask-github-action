import pytest
from PIL import Image
from model.model_handler import Classifier
from app import _read_image


@pytest.fixture
def sample_image():
    image = Image.open("tests/data/i4SqIP.jpg")
    return image


@pytest.fixture
def expectec_class():
    return "n02106030", "collie"


def test_model_hanlder(sample_image, expectec_class):
    model = Classifier()
    model.initialize()
    input_ = model.preprocess(sample_image)
    output_ = model.inference(input_)
    class_id, class_name = model.postprocess(output_)
    expected_class_id, expected_class_name = expectec_class
    assert class_id == expected_class_id
    assert class_name == expected_class_name


def test_read_image_url():
    image = _read_image(
        "https://i.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U"
    )
    print(image)
