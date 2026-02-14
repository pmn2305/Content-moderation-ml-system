from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from models.text import TextModerationModel
from models.image import ImageModerationModel

app = FastAPI(title="Inference Service")

text_model = TextModerationModel()
image_model = ImageModerationModel()


class TextRequest(BaseModel):
    text: str


@app.post("/infer/text")
def infer_text(req: TextRequest):

    if not req.text.strip():
        return {
            "score": 0.0,
            "model_version": "toxic-bert-v1"
        }

    score = text_model.predict(req.text)

    return {
        "score": round(score, 3),
        "model_version": "toxic-bert-v1"
    }


@app.post("/infer/image")
async def infer_image(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()

        if not image_bytes:
            raise ValueError("Empty file")

        result = image_model.predict(image_bytes)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image file: {str(e)}")

    return {
        "score": round(result["score"], 3),
        "model_version": result["model_version"]
    }


@app.get("/health")
def health():
    return {"status": "ok"}
