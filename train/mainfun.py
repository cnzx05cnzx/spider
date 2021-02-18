import requests
import os


def get_respense(Url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Referer":"http://manhua.dmzj1.com/emengfunk/"
    }

    response = requests.get(Url, timeout=5)
    response.encoding = response.apparent_encoding

    return response


def get_pic(url, path, name):
    path = path + '/' + name

    response = get_respense(url)
    # print(response.text)
    with open(path, 'wb') as fp:
        fp.write(response.content)


def mkdir(path):
    # 引入模块
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')

    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
