#!/bin/env python3

"""
This bit of code humbly ripped from https://github.com/vivithemage/mrisa/blob/master/src/server.py
"""

import json
from bs4 import BeautifulSoup


def parse_results(code):
    """Parse/Scrape the HTML code for the info we want."""

    soup = BeautifulSoup(code, 'lxml')

    results = {
        'links': [],
        'descriptions': [],
        'titles': [],
        'similar_images': [],
        'best_guess': ''
    }

    for div in soup.findAll('div', attrs={'class': 'rc'}):
        link = div.find('a')
        results['links'].append(link['href'])

    for desc in soup.findAll('span', attrs={'class': 'st'}):
        results['descriptions'].append(desc.get_text())

    for title in soup.findAll('h3', attrs={'class': 'r'}):
        results['titles'].append(title.get_text())

    for similar_image in soup.findAll('div', attrs={'rg_meta'}):
        tmp = json.loads(similar_image.get_text())
        img_url = tmp['ou']
        results['similar_images'].append(img_url)

    for best_guess in soup.findAll('a', attrs={'class': '_gUb'}):
      results['best_guess'] = best_guess.get_text()

    return json.dumps(results)
