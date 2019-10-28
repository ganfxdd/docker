from selenium import webdriver
import time
import pandas as pd
import json
import datetime
import oandapyV20
from oandapyV20 import API
from oandapyV20.endpoints.pricing import PricingStream
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.pricing import PricingInfo
import oanda_common as oc
import threading


#マネーパートナーズレート取得

def manepa():
    
    val_bid = 0
    val_bid_pre = 0
    val_ask = 0
    val_ask_pre = 0

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://trade.moneypartners.co.jp/fxcwebpresen/RealtimeListPriceBoardAjax.do')
    time.sleep(5)

    while True:
        rate1 = driver.find_element_by_id('bidCurrencyPrice1')
        rate2 = driver.find_element_by_id('askCurrencyPrice1')
        val_ask_pre = val_ask
        val_ask = float(rate1.text)
        val_bid_pre = val_bid
        val_bid = float(rate2.text)
        #レートの更新があれば表示する
        if val_ask != val_ask_pre:
            print("manepaask:" + str(val_ask) + "manepabid:" + str(val_bid))
    
#OANDAよりレート取得
def oanda():
    account_id = ""
    access_token = ""

    api = API(access_token=access_token, environment="live")

    params = {"instruments": "USD_JPY"}
    pricing_info = PricingInfo(accountID=account_id, params=params)

    oal_ask = 0
    oal_ask_pre = 0
    oal_bid = 0
    oal_bid_pre = 0

    try:
        while True:
            api.request(pricing_info)
            response = pricing_info.response
            oal_ask_pre = oal_ask
            oal_ask = response['prices'][0]['asks']
            oal_bid_pre = oal_bid
            oal_bid = response['prices'][0]['bids']
            if oal_ask != oal_ask_pre:
                print("oandaask:" + str(oal_ask) + " oandabid:" + str(oal_bid))

    except V20Error as e:
        print("Error: {}".format(e))
    
#同期処理
if __name__ == "__main__":
    thread_1 = threading.Thread(target=manepa)
    thread_2 = threading.Thread(target=oanda)
    
    thread_1.start()
    thread_2.start()
