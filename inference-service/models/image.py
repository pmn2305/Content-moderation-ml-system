from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
import io


class ImageModerationModel:
    def __init__(self):
        self.model_name = "AdamCodd/vit-base-nsfw-detector"
        self.processor = AutoImageProcessor.from_pretrained(self.model_name)
        self.model = AutoModelForImageClassification.from_pretrained(self.model_name)

        self.model.eval()
        self.model_version = "vit-nsfw-lite-v1"

    def predict(self, image_bytes: bytes) -> dict:
        print(" NEW LIGHT MODEL RUNNING ")

        try:
            image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        except Exception as e:
            raise ValueError(f"Invalid image file: {str(e)}")

        inputs = self.processor(images=image, return_tensors="pt")

        with torch.no_grad():
            outputs = self.model(**inputs)

        logits = outputs.logits
        probs = torch.softmax(logits, dim=1)[0]

        # This model outputs 2 classes: safe / nsfw
        nsfw_score = float(probs[1].item())

        return {
            "score": nsfw_score,
            "model_version": self.model_version
        }
