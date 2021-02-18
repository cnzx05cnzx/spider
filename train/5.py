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
            var step = 200; 
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

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options = chrome_options
    option = ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    options = option

    browser = webdriver.Chrome(options=option, chrome_options=chrome_options)
    # 输入动漫之家爬取漫画主页(用于·国漫爬取)
    browser.get(url)

    sleep(1)
    browser.find_element_by_xpath('//div[@class="login_tip out"]').click()
    sleep(0.1)
    browser.find_element_by_class_name("red_reset").click()
    sleep(0.1)
    browser.find_element_by_id("mode_2").click()
    sleep(0.1)
    browser.find_element_by_xpath('//div[@class="bar_open_btn"]/a[@class="qd cus"]').click()
    sleep(1)
    scroll(browser)
    # pic_list = WebDriverWait(browser, 0.5).until(
    #     EC.presence_of_all_elements_located((By.XPATH, '//div[@class="comic_wraCon autoHeight"]/a/img'))
    # )
    pic_list = browser.find_elements_by_xpath('//div[@class="comic_wraCon autoHeight"]/a/img')
    # i用于计数
    i = 0
    for pic in pic_list:
        pic_url = pic.get_attribute('src')
        #print(pic_url)
        pic_name = str(i) + '.jpg'
        train.mainfun.get_pic(pic_url, pathname, pic_name)
        i = i + 1
    print(name + "爬取成功")
    browser.close()


# 爬取动漫之家漫画
if __name__ == '__main__':
    # 输入动漫首页
    url = "https://www.dmzj1.com/info/lingzhushimedewusuoweila.html"

    # 获取网址信息
    res = train.mainfun.get_respense(url)
    tree = etree.HTML(res.text)
    # 通过xpath解析获得信息

    # 创建文件夹
    title_name = tree.xpath(
        '//div[@class="comic_deCon"]/h1/a/text()')[0]
    filename = "C:/Users/violet/Desktop/comic/" + title_name
    train.mainfun.mkdir(filename)
    # print(title_name)

    news_list = tree.xpath(
        '//div[@class="tab-content zj_list_con autoHeight"]/ul[@class="list_con_li autoHeight"]/li/a')
    # print(news_list)

    for li in news_list:
        href = li.xpath('./@href')[0]
        name = li.xpath('./span/text()')[0]
        path_name = filename + '/' + name
        get_main_pic(href, name, path_name)
        sleep(0.5)
        # print(href + "  " + name)
