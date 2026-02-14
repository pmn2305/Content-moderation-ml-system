from transformers import pipeline
from PIL import Image
import io


class ImageModerationModel:
    def __init__(self):
        self.pipe = pipeline(
            "image-classification",
            model="Falconsai/nsfw_image_detection"
        )
        self.model_version = "nsfw-vit-v1"

        # Labels considered unsafe
        self.NSFW_LABELS = {"porn", "sexy", "hentai", "nsfw"}

    def predict(self, image_bytes: bytes) -> dict:
        """
        Accepts raw image bytes.
        Converts to PIL.Image internally.
        Returns:
        {
            "score": float,
            "model_version": str
        }
        """

        try:
            # Convert bytes -> PIL Image
            image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        except Exception as e:
            raise ValueError(f"Invalid image file: {str(e)}")

        # Run inference
        outputs = self.pipe(image)

        # Debug (optional — remove in production)
        print("model outputs:", outputs)

        nsfw_score = 0.0

        for out in outputs:
            if out["label"].lower() in self.NSFW_LABELS:
                nsfw_score = float(out["score"])
                break

        return {
            "score": nsfw_score,
            "model_version": self.model_version
        }
