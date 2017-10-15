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

async def get_search_html(url):
    """ Gets the html response of a google images search page """ 
    async with SESSION.get(url, headers=HEADERS) as r:
        if r.status == 200:
            return await r.text()
        else:
            return None

@app.route('/search', methods=['POST'])
async def get_handler(ctx):
    """ Returns json respresentiaton of a google reverse image search query """
    img_url = ''
    for url in ctx.request.form:
        img_url = url

    resp_html = await get_search_html(SEARCH_URI.format(img_url))
    if resp_html:
        resp_json = rp.parse_results(resp_html)
    else:
        return None

    return as_json(resp_json)


if __name__ == '__main__':
    app.run(ip='localhost', port=8000)
