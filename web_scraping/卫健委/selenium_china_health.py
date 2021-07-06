import time

from selenium import webdriver
from scrapy import Selector


def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML,'
                         ' like Gecko) Chrome/86.0.4240.198 Safari/537.36')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--disable-gpu')

    # chromedriver.exe文件需要去下面的网址下载适合自己电脑chrome的版本，并更换文件名
    # http://npm.taobao.org/mirrors/chromedriver/
    return webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=options)


driver = init_driver()

with open('stealth.min.js') as f:
    js = f.read()

driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': js
})

driver_get_url = 'http://www.nhc.gov.cn/xcs/yqjzqk/202106/74ed0aa148744960988030bf6a3186da.shtml'
driver.get(driver_get_url)
time.sleep(2)
html = driver.page_source
selector = Selector(text=html)

text_result = selector.css('#xw_box>p::text').extract_first()
print(text_result)

driver.quit()
