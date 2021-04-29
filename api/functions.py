from config import MAX_IMAGE_SIZE
from random import randint
import aiohttp
import aiofiles

MAX_IMAGE_SIZE = MAX_IMAGE_SIZE * 1000000

async def download_image(url):
    file_name = f"{randint(6969, 6999)}.jpg"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                if int(resp.headers['Content-Length']) > MAX_IMAGE_SIZE:
                    return False
                f = await aiofiles.open(file_name, mode='wb')
                await f.write(await resp.read())
                await f.close()
            else:
                return False
    return file_name


async def calculate_horny(hentai_value, neutral_value, porn_value, sexy_value):
    weight_hentai = 0.18
    weight_neutral = 0.32
    weight_sexy = 0.22
    weight_porn = 0.28
    prominent = max (hentai_value, porn_value, sexy_value)
    if neutral_value < prominent:
        factor_calculation = weight_hentai * hentai_value - weight_neutral * neutral_value + weight_sexy * sexy_value + weight_porn * porn_value
        horny_factor = ((1 - factor_calculation/prominent) * 100)
        return horny_factor
    else:
        return -1 * neutral_value
