import re

import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import json

#爬取药监局信息

def useid(idlist):
    html_temp = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }


    for i in idlist:
        par = {
            'id': i['ID']
        }
        response = requests.post(html_temp, headers=headers, data=par)
        con=response.json()
        print(con['epsAddress'])


if __name__ == "__main__":
    Url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"

    param = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': ''

    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }

    response = requests.post(Url, headers=headers, data=param)

    list_data = response.json()
    com_data = list_data['list']
    useid(com_data)
    #print(list_data['list'])



    #详情页ajkx数据 http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById

    #temp = json.dumps(list_data, ensure_ascii=False)
    #movie_list = json.loads(temp)
