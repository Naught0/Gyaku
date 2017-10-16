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
    """ Gets the aiohttp response object for a given URL """ 
    async with SESSION.get(url, headers=HEADERS) as r:
        return r

async def get_resp_html(url):
    """ Gets the HTML response of a given URL """
    async with SESSION.get(url, headers=HEADERS) as r:
        if r.status == 200:
            return await r.text
        else:
            return None

def is_image(r: aiohttp.ClientResponse):
    """ Checks whether the supplied URL is a proper image """ 
    return r.content_type.startswith('image')

@app.route('/search', methods=['POST'])
async def search_handler(ctx):
    """ Returns json respresentiaton of a google reverse image search query """
    img_url = ''
    for url in ctx.request.form:
        img_url = url

    # Check whether the image exists and is actually a proper image
    image_resp = await get_resp_obj(img_url)
    if image_resp is None:
        return as_json({'error': 'Image does not exist'})
    if not is_image(image_resp):
        return as_json({'error': 'URL does not contain a proper image'})

    # Search for the image via reverse google image search
    google_html = await get_resp_html(SEARCH_URI.format(img_url))
    if google_html is None:
        return as_json({'error': 'Google has blocked this IP\nRe-captcha may be required'})

    # Try to decode HTML into JSON response
    try:
        # Decode the HTML into a json response
        return as_json(rp.parse_results(google_html))
    except Exception as e:
        return as_json({'error': f'Soup parsing error: {e}'})

    return as_json(resp_json)


if __name__ == '__main__':
    app.run(ip='localhost', port=8000)
