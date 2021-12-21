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
