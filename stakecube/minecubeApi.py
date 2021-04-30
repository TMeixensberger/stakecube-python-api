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
 
import requests
from .helper.security import *
from .helper.utility import *

class MinecubeAPI:
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

    def buyWorker(self, method = "SCC", amount = 10):

        currentNonce = getNonce()

        # sum up all parameters
        paramerters = "nonce=" + currentNonce + "&method=" + method + "&amount=" + str(amount)

        url = api_base_url + "minecube/buyWorker"

        postObj = {
            "nonce" : currentNonce,
            "method" : method,
            "amount" : str(amount),
            "signature": getHMAC(paramerters, self.api_secret)
        }

        # send the api request
        response = requests.post(url, headers = self.headers, data=postObj)
        
        # check if the request was successful
        if response.status_code == 200 and response.json()['success'] == True:
            return True
        elif response.status_code != 200:
            self.last_error = "Http error"
        elif response.json()['success'] != True:
            self.last_error = response.json()['error']
        return False