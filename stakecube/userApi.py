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
# copyright Tobias Meixensberger (C) 2017
# author    Tobias Meixensberger
# contact   tobias@tmeixensberger.de
#
 
import requests
from .helper.security import *
from .helper.utility import *

class UserAPI:
    def __init__(self, api_key, api_secret) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {'X-API-KEY': self.api_key,
                        'Host': api_base_host,
                        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

    def getBalanceInMasternodes(self, coinTicker):
        # get the data
        wallet = self.getCoinWallet(coinTicker)

        # check if the data could be received
        if wallet != None:
            return wallet['balanceInMasternodes']
        return None

    def getBalanceInOrder(self, coinTicker):
        # get the data
        wallet = self.getCoinWallet(coinTicker)

        # check if the data could be received
        if wallet != None:
            return wallet['balanceInOrder']
        return None

    def getDepositAddress(self, coinTicker):
        # get the data
        wallet = self.getCoinWallet(coinTicker)

        # check if the data could be received
        if wallet != None:
            return wallet['address']
        return None

    def getBalance(self, coinTicker):
        # get the data
        wallet = self.getCoinWallet(coinTicker)

        # check if the data could be received
        if wallet != None:
            return wallet['balance']
        return None
    
    def getCoinWallet(self, coinTicker):
        # fetch the data from the api
        apiData = self.account()
        if apiData != None:
            wallets = apiData['wallets']
            for wallet in wallets:
                if wallet['asset'] == coinTicker:
                    return wallet
        return None

    def getUsername(self):
        # fetch the data from the api
        apiData = self.account()
        if apiData != None:
            return apiData['user']
        else:
            return None

    def getExchangeFee(self):
        # fetch the data from the api
        apiData = self.account()
        if apiData != None:
            return apiData['exchangeFee']
        else:
            return None

    def account(self):
        
        nonce = "nonce=" + getNonce()
        paramerters = nonce
        signature = "signature=" + getHMAC(paramerters, self.api_secret)
        url = api_base_url + "user/account?" + paramerters + "&" + signature

        # send the api request
        response =requests.get(url, headers = self.headers)

        # check if the request was successful
        if response.status_code == 200 and response.json()['success'] == True:
            return response.json()['result']
        else:    
            return None
            