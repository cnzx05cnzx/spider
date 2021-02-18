from lxml import etree
import train.mainfun

if __name__ == '__main__':
    url = "https://www.baidu.com"
    # 获取网址信息
    res = train.mainfun.get_respense(url)
    # 将其转化为文本树
    tree = etree.HTML(res.text)
    # 通过xpath解析获得pic链接列表

    news_list = tree.xpath('//div[@class="s-hotsearch-title"]/ul/li/a/@href')

    for li in news_list:
        print(news_list)
