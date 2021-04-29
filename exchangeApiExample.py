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

from stakecube.exchangeApi import ExchangeAPI
from stakecube.userApi import *

api_key = "9609740d4984687e6a3b465d572f5360e9042d85c419cef360478512bdf7c3f8"
api_secret = "bd26cb5096d8c6c9e0a88965f9e19ffebad1564fae5787aeedd7de0299ecc4523bdd1a766732eb36480ace474ad3e17a62750c9b405f41b350eab59b10eaa7c4"

exchange = ExchangeAPI(api_key, api_secret)

# doge is the market coin and scc the base coin
market = "DOGE_SCC"

# side of the market
side = "BUY"

# price in the base coin
price = 0.01

# amount in the market coin
amount = 50

# buy 50 DOGE for 0.0001 SCC per DOGE
orderId = exchange.order(market, side, price, amount)

if orderId > 0:
    print("Order has been created. OrderId:", orderId)

    # cancel the order
    if exchange.cancelOrder(orderId):
        print("Successfully canceled the order.")
    else:
        print("Error occurred during removing the order.")
        print(exchange.getLastError())
else:
    # error occurred
    print(exchange.getLastError())