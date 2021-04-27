from api import predict, app
from api.functions import download_image
import os
import uvicorn

model = predict.load_model('nsfw_detector/nsfw_model.h5')


@app.get("/")
async def detect_nsfw(url: str):
    if not url:
        return {"ERROR": "URL PARAMETER EMPTY"}
    image = await download_image(url)
    if not image:
        return {"ERROR": "IMAGE SIZE TOO LARGE OR INCORRECT URL"}
    data = predict.classify(model, image)
    os.remove(image)
    return data

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, log_level="info")
