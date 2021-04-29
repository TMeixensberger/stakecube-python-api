#
#This file is part of the stakecube-python-api.
#
#stakecube-python-api is free software: you can redistribute it and/or modify
#it under the terms of the GNU Lesser General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#stakecube-python-api is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU Lesser General Public License for more details.
#
#You should have received a copy of the GNU Lesser General Public License
#along with stakecube-python-api.  If not, see <http://www.gnu.org/licenses/>.
#
# copyright Tobias Meixensberger (C) 2021
# author    Tobias Meixensberger
# contact   tobias@tmeixensberger.de
#
 
from typing import OrderedDict
import requests
from .helper.security import *
from .helper.utility import *

class ExchangeAPI:
    def __init__(self, api_key, api_secret) -> None:
        self.last_error = ""
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {'X-API-KEY': self.api_key,
                        'Host': api_base_host,
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    def getLastError(self):
        tmp = self.last_error
        self.last_error = ""
        return tmp
    
    def sellOrderbook(self, market):
        orderbook = self.orderbook("SELL", market)
        if orderbook != None:
            return orderbook['asks']
        else:
            return None

    def buyOrderbook(self, market):
        orderbook = self.orderbook("BUY", market)
        if orderbook != None:
            return orderbook['bids']
        else:
            return None

    def orderbook(self, side, market):
        paramerters = "market=" + market + "&side=" + side
        signature = "signature=" + getHMAC(paramerters, self.api_secret)
        url = api_base_url + "exchange/spot/orderbook?" + paramerters + "&" + signature

        # send the api request
        response = requests.get(url, headers = self.headers)

        # check if the request was successful
        if response.status_code == 200 and response.json()['success'] == True:
            return response.json()['result']
        else:    
            return None

    def cancelOrder(self, orderId):
        
        currentNonce = getNonce()

        # sum up all parameters
        paramerters = "orderId=" + str(orderId) + "&nonce=" + currentNonce

        url = api_base_url + "exchange/spot/cancel"

        postObj = {
            "orderId" : orderId,
            "nonce" : currentNonce,
            "signature": getHMAC(paramerters, self.api_secret)
        }

        # send the api request
        response = requests.post(url, headers = self.headers, data=postObj)
        
        # check if the request was successful
        if response.status_code == 200 and response.json()['success'] == True:
            return True
        else:    
            self.last_error = response.json()['error']
            return False

    def order(self, market, side, price, amount):

        currentNonce = getNonce()

        # sum up all parameters
        paramerters = "market=" + market + "&side=" + side + "&price=" + str(price) + "&amount=" + str(amount) + "&nonce=" + currentNonce

        url = api_base_url + "exchange/spot/order"

        postObj = {
            "market" : market,
            "side" : side,
            "price" : price,
            "amount" : str(amount),
            "nonce" : currentNonce,
            "signature": getHMAC(paramerters, self.api_secret)
        }

        # send the api request
        response = requests.post(url, headers = self.headers, data=postObj)
        
        # check if the request was successful
        if response.status_code == 200 and response.json()['success'] == True:
            return response.json()['result']['orderId']
        else:    
            self.last_error = response.json()['error']
            return -1