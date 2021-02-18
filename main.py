import re

import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import os


def get_res(Url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    }

    response = requests.get(Url, timeout=5)
    response.encoding = response.apparent_encoding

    num = re.findall("\d+", Url)[0]
    print(num)
    get_content(response, num)
    # 当爬取的界面需要用户名密码登录时候，构建的请求需要包含auth字段
    # response = requests.get(newUrl,headers=headers,auth=('username','passsword'))
    # print(soup.prettify())
    # return response


def get_content(res, pos):
    soup = BeautifulSoup(res.text, 'lxml')
    content = soup.find(id="post-list-posts")
    lists = content.select('li')
    sum = 0
    for lis in lists:
        sum += 1
        picurl = lis.find("a", class_="directlink")['href']
        save_img(picurl, sum, pos)

    # print(soup.prettify())


def save_img(image_url, uid, loc):
    """
    """
    try:
        save_folder = 'C://Users//violet//Desktop//meizi//'
        response = requests.get(image_url, timeout=5)
        dir = save_folder + str(loc) + '_' + str(uid) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(response.content)
        fp.close()
        print(str(loc) + '_' + str(uid) + ' finish')
    except IOError as e:
        print('error')


if __name__ == "__main__":
    # re_scraper("https://www.qiushibaike.com/8hr/page/1/")

    urls = ["https://konachan.com/post?page={}&tags=underwear".format(str(i)) for i in range(12, 14)]
    # url = 'https://konachan.com/post?page=1&tags=breasts'

    pool = Pool(processes=4)
    pool.map(get_res, urls)
    print('complete')
