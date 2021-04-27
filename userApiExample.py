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

from stakecube.userApi import *

api_key = "5be9c7a58e975f3d4a74ca760c8a9d4f3dc91d10707e588434f961b369d204c5"
api_secret = "f82fcc9c82505e5aaaea4a8d9256465bf24301a2e1929fddf7cc6c41e0f1906955706173b92f3344d90316fcd365af6d922bc4d395beef214a5f2504e531995d"

user = UserAPI(api_key, api_secret)

print("Users bitcoin balance:", user.getBalance('BTC'))
print("Users stakecubecoin balance:", user.getBalance('SCC'))
print("Users bitcoin address:", user.getDepositAddress('BTC'))

#user.withdraw("sTEjazvJtunSHZma1kGbLaAbHmeZ4kM8Kf",1,"SCC")