import json
import requests
from json2html import *


def get_studies():
    pack_dat = {}
    x = 0
    resp = requests.get('https://api.otreeba.com/v1/studies?page=1&count=16').json()
    for x in resp['data']:
        study = OrderedDict({
                "Title": x['name'],
                "Updated": x['updatedAt'],
                "Key Findings": x['keyFindings']
           })
        pack_dat.update(study)
    html_dat = json2html.convert(json=pack_dat, table_attributes="class=\"table tablesorter\"")
    return html_dat


def get_brands():
    pack_dat = {}
    x = 0
    resp = requests.get('https://api.otreeba.com/v1/brands?page=2W&count=1').json()
    for x in resp['data']:
        study = OrderedDict({
            "Name": x['name'],
            "Brand": x,
            # "Key Findings": x['keyFindings']
        })
        pack_dat.update(**study)
        return pack_dat
        #
    # html_dat = json2html.convert(json=pack_dat, table_attributes="class=\"table tablesorter\"")
    # return html_dat
    return pack_dat