#!/bin/env python3

import asyncio
import aiohttp
import result_parser as rp
from kyoukai import Kyoukai
from kyoukai.util import as_json

    
LOOP = asyncio.get_event_loop()
SESSION = aiohttp.ClientSession(loop=LOOP)
SEARCH_URI = 'https://www.google.com/searchbyimage?&image_url={}'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.97 Safari/537.11'}


app = Kyoukai('image_search', loop=LOOP)

async def get_resp_obj(url):
    """ Gets the html response of a google images search page """ 
    async with SESSION.get(url, headers=HEADERS) as r:
        if r.status == 200:
            return r
        else:
            return None

async def is_image(r: aiohttp.ClientResponse):
    """ Checks whether the supplied URL is a proper image """ 
    return r.content_type.startswith('image')

@app.route('/search', methods=['POST'])
async def search_handler(ctx):
    """ Returns json respresentiaton of a google reverse image search query """
    img_url = ''
    for url in ctx.request.form:
        img_url = url

    # Check whether the image exists and is actually a proper image
    image_response = await get_resp_obj(img_url)
    if image_response.status != 200:
        return as_json({'error': 'URL is unreachable'})
    elif not is_image(image_response):
        return as_json({'error': 'URL does not contain a proper image'})

    # Search for the image via reverse google image search
    else: 
        try:
            # Decode the HTML into a json response
            resp_json = rp.parse_results(
                            await get_resp_obj(SEARCH_URI.format(img_url)).text()
                            )
        except Exception as e:
            return as_json({'error': f'Soup parsing error: {e}'})

    return as_json(resp_json)


if __name__ == '__main__':
    app.run(ip='localhost', port=8000)
