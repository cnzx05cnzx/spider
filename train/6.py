import random
from lxml import etree
import train.mainfun
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

def scroll(driver):
    driver.execute_script(""" 
        (function () { 
            var y = document.body.scrollTop; 
            var step = 100; 
            window.scroll(0, y); 
            function f() { 
                if (y < document.body.scrollHeight) { 
                    y += step; 
                    window.scroll(0, y); 
                    setTimeout(f, 50); 
                }
                else { 
                    window.scroll(0, y); 
                    document.title += "scroll-done"; 
                } 
            } 
            setTimeout(f, 1000); 
        })(); 
        """)
def get_main_pic(url, name, pathname):
    train.mainfun.mkdir(pathname)

    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options = chrome_options
    # option = ChromeOptions()
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # options = option

    browser = webdriver.Chrome()
    # 输入动漫之家爬取漫画主页(用于·日漫爬取)
    browser.get(url)

    sleep(1)
    browser.find_element_by_xpath('//div[@class="login_tip out"]').click()
    sleep(0.1)

    browser.find_element_by_id("qiehuan_txt").click()
    scroll(browser)
    # pic_list = WebDriverWait(browser, 0.5).until(
    #     EC.presence_of_all_elements_located((By.XPATH, '//div[@class="comic_wraCon autoHeight"]/a/img'))
    # )

    pic_list = browser.find_elements_by_xpath('//div[@id="center_box"]/div/a/img')
    sleep(2)
    # i用于计数
    i = 0
    for pic in pic_list:
        pic_url = pic.get_attribute('src')
        # print(pic_url)
        pic_name = str(i) + '.jpg'
        train.mainfun.get_pic(pic_url, pathname, pic_name)
        i = i + 1
        sleep(random.random())
    print(name + "爬取成功")
    browser.close()

    # 爬取动漫之家漫画
    # if __name__ == '__main__':
    #     # 输入动漫首页
    #     url = "http://manhua.dmzj1.com/emengfunk/"
    #     temp = "http://manhua.dmzj1.com"
    #     # 获取网址信息
    #     res = train.mainfun.get_respense(url)
    #     tree = etree.HTML(res.text)
    #     # 通过xpath解析获得信息
    #
    #     # 创建文件夹
    #     title_name = tree.xpath(
    #         '//div[@class="odd_anim_title_m"]/span/a/h1/text()')[0]
    #     filename = "C:/Users/violet/Desktop/comic/" + title_name
    #     train.mainfun.mkdir(filename)
    #     # print(title_name)
    #
    #     news_list = tree.xpath(
    #         '//div[@class="cartoon_online_border"]/ul/li/a')
    #     # print(news_list)
    #
    #     for li in news_list:
    #         href = li.xpath('./@href')[0]
    #         name = li.xpath('./text()')[0]
    #         path_name = filename + '/' + name
    #         href = temp + href
    #         get_main_pic(href, name, path_name)


if __name__ == '__main__':
    get_main_pic("http://manhua.dmzj1.com//emengfunk/42239.shtml", "第一话", "C:/Users/violet/Desktop/comic/噩梦Funk/第一话")
