from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import torch
import io


class ImageModerationModel:
    def __init__(self):
        self.model_name = "Falconsai/nsfw_image_detection"
        self.processor = AutoImageProcessor.from_pretrained(self.model_name)
        self.model = AutoModelForImageClassification.from_pretrained(self.model_name)

        self.model.eval()
        self.model_version = "nsfw-vit-v1"

        self.NSFW_LABELS = {"porn", "sexy", "hentai", "nsfw"}

    def predict(self, image_bytes: bytes) -> dict:
        print(" NEW IMAGE MODEL CODE RUNNING ")

        try:
           image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        except Exception as e:
          raise ValueError(f"Invalid image file: {str(e)}")

        inputs = self.processor(
           images=image,
           return_tensors="pt",
           padding=True   # <-- ADD THIS
        )

        with torch.no_grad():
           outputs = self.model(**inputs)

        logits = outputs.logits
        probs = torch.softmax(logits, dim=1)[0]

        id2label = self.model.config.id2label
  
        nsfw_score = 0.0

        for idx, prob in enumerate(probs):
           label = id2label[idx].lower()
           if label in self.NSFW_LABELS:
            nsfw_score = float(prob.item())
            break

        return {
           "score": nsfw_score,
           "model_version": self.model_version
       }
