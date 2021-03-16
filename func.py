####################
#
# 初期設定 
#
####################

# モジュール
import time
import os
import traceback

# セレニウム
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# アプリのルートディレクトリ
APP_DIRE = os.path.dirname(os.path.abspath(__file__))





####################
#
# 関数
#
####################
def get_ad_url(word):
    
    try:
        # ブラウザ起動
        driver_path = '/app/.chromedriver/bin/chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('--headless') # ヘッドレスモード
        options.add_argument('--no-sandbox') # セキュリティブロックオフ
        options.add_argument('--disable-gpu') # 
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 自動操作の表示オフ
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-dev-shm-usage') # shm無効
        options.add_argument(f'--window-size=1280x720') # ウィンドウサイズ変更
        options.add_argument(f'user-data-dir={APP_DIRE}/user_data') # セッション偽装

        driver = webdriver.Chrome(options=options, executable_path=driver_path) # heroku環境用
        # driver = webdriver.Chrome('chromedriver.exe', options=options) # ローカル環境用

        url = f'https://www.google.com/search?q={word}'
        driver.get(url)
        time.sleep(5)
        page_source = driver.page_source

        return page_source


    except:
        return traceback.format_exc()