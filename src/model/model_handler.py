import json

from PIL import Image
import torch
from torchvision import models
import torchvision.transforms as transforms


class Classifier:
    def __init__(self):
        self.model = None
        self.class_index = None

    def initialize(self, class_index_path: str = "models/index_to_name.json"):
        self.class_index = json.load(open(class_index_path))
        self.model = models.densenet121(pretrained=True)
        self.model.eval()

    def preprocess(self, image: Image.Image) -> torch.Tensor:
        my_transforms = transforms.Compose(
            [
                transforms.Resize(255),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
            ]
        )
        tensor = my_transforms(image).unsqueeze(0)
        return tensor

    def inference(self, inputs: torch.Tensor) -> torch.Tensor:
        outputs = self.model.forward(inputs)
        return outputs

    def postprocess(self, outputs: torch.Tensor):
        _, y_hat = outputs.max(1)
        predicted_idx = str(y_hat.item())
        class_id, class_name = self.class_index[predicted_idx]
        return class_id, class_name
