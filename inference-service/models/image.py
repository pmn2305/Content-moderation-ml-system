from transformers import pipeline
from PIL import Image
import io


class ImageModerationModel:
    def __init__(self):
        self.pipe = pipeline(
            task="image-classification",
            model="Falconsai/nsfw_image_detection",
            top_k=None  # important
        )
        self.model_version = "nsfw-vit-v1"
        self.NSFW_LABELS = {"porn", "sexy", "hentai", "nsfw"}

    def predict(self, image_bytes: bytes) -> dict:
        try:
            image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        except Exception as e:
            raise ValueError(f"Invalid image file: {str(e)}")

        # wrap image in list to avoid tensor shape mismatch
        outputs = self.pipe([image])[0]

        nsfw_score = 0.0

        for out in outputs:
            if out["label"].lower() in self.NSFW_LABELS:
                nsfw_score = float(out["score"])
                break

        return {
            "score": nsfw_score,
            "model_version": self.model_version
        }
