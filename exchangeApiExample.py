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

api_key = "8046ba0fb805056d227956e94ef6d76436667a7908e8fe4f5d067d04534e0f55"
api_secret = "4965e04499708b1cb35f7fd7eb4a394b8361a450a3adb494b65c2f6b6825e8b249bf989a1c40e83ccd8fd7ef6559b0dca6971267e39ea6d6575564cdd6c5c05b"

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
exchange.order(market, side, price, amount)