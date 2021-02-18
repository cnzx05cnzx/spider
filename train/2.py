

import requests
from multiprocessing import Pool
import re
from bs4 import BeautifulSoup
from train.mainfun import get_respense


# 爬取笔趣阁小说信息   https://www.xsbiquge.com/

def get_list(Url):
    response = get_respense(Url)

    soup = BeautifulSoup(response.text, 'lxml')
    res = soup.select("#list dl dd a")
    return res


def get_con(Url):
    response = get_respense(Url)

    soup = BeautifulSoup(response.text, 'lxml')
    res = soup.find(id="content")
    return res


def write_con(Url, name):
    con = get_con(Url)
    con = re.sub('\s+', '\r\n\t', con.text).strip('\r\n')
    # print(con)
    path1 = "./model/"
    path2 = ".text"
    path = path1 + name + path2
    with open(path, 'w', encoding='utf-8') as fp:
        fp.write(con)
        fp.write('\r\n')


if __name__ == "__main__":
    # 爬取小说首页
    Url = "https://www.xsbiquge.com/97_97373/"
    # 爬取小说目录
    name_list = get_list(Url)

    for i in name_list:
        url = Url + i['href'].split('/')[2]
        # 爬取具体内容
        write_con(url, i.text)
