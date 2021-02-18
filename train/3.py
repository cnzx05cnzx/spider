from lxml import etree
import train.mainfun

if __name__ == '__main__':
    url = "https://konachan.com/post"
    # 获取网址信息
    res = train.mainfun.get_respense(url)
    # 将其转化为文本树
    tree = etree.HTML(res.text)
    # 通过xpath解析获得pic链接列表
    pic_list = tree.xpath('//ul[@id="post-list-posts"]/li/a[@class="directlink largeimg"]/@href')
    path = '../pic'
    i = 0
    name = '.jpg'
    for pic in pic_list:
        train.mainfun.get_pic(pic, path, str(i) + name)
        print(str(i) + " is finished")
        i = i + 1
