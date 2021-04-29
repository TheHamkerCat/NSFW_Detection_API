from api import predict, app
from api.functions import download_image, calculate_horny
from config import PORT
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
    results = predict.classify(model, image)
    os.remove(image)
    hentai = results['data']['hentai']
    sexy = results['data']['sexy']
    porn = results['data']['porn']
    drawings = results['data']['drawings']
    neutral = results['data']['neutral']
    hornyfactor = await calculate_horny(hentai, neutral, porn, sexy)
    if neutral >= 20 or drawings >= 30:
        results['data']['is_nsfw'] = False
        return results
    elif hornyfactor >= 30:
        results['data']['is_nsfw'] = True
        return results
    else:
        results['data']['is_nsfw'] = False
        return results

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=PORT, log_level="info")
