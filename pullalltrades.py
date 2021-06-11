

from stakecube.exchangeApi import ExchangeAPI
import pandas as pd

api_key = "xxx"
api_secret = "xxx"

exchange = ExchangeAPI(api_key, api_secret)

# pull all existing trading pairs
trading_pair =[]
markets = exchange.pull_markets()
for i in markets:
    trading_pair.append(i)

# print(markets)

# set dataframe columns
typ = []
buyamnt = []
buycur = []
sellamnt = []
sellcur = []
feeamnt = []
feecur = []
exchg = []
tradegr = []
comm = []
dat =[]
fields = {"Type": typ, "Buy Amount": buyamnt, "Buy Cur.": buycur, "Sell Amount": sellamnt, "Sell Cur.": sellcur,
          "Fee Amount": feeamnt, "Fee Cur.": feecur, "Exchange": exchg, "Trade Group": tradegr, "Comment": comm, "Date": dat}

# cycle through the existing markets and save trades
for i in trading_pair:
    counter = 0
    print(f"Downloading {i} trade history...")
    pair = i
    assets = pair.split("_")
    base_asset = assets[0]
    quote_asset = assets[1]
    trade_history = exchange.tradehistory("1000", pair)
    if trade_history == None:
        print("No Trades detected.")
        continue
    # save trade information on its respective columns
    for trade in trade_history:
        counter +=1
        print(f"Saving trade {counter} of {len(trade_history)}")
        trade_state = trade.get("state")
        if trade_state == "CANCELED":
            continue
        typ.append("Trade")
        side = trade.get("side")
        feeamnt.append(trade.get("makerFee"))
        exchg.append("Stakecube")
        tradegr.append("")
        comm.append("")
        dat.append(trade.get("filled"))
        if side == "BUY":
            buycur.append(base_asset)
            sellcur.append(quote_asset)
            base_amount = trade.get("executedAmount")
            execution_price = float(trade.get("price"))
            quote_amount = float(base_amount) * execution_price
            buyamnt.append(trade.get("executedAmount"))
            sellamnt.append(str(quote_amount))
            feecur.append(base_asset)
        if side == "SELL":
            buycur.append(quote_asset)
            sellcur.append(base_asset)
            sellamnt.append(trade.get("executedAmount"))
            execution_price = float(trade.get("price"))
            base_amount = trade.get("executedAmount")
            quote_amount = float(base_amount) * execution_price
            buyamnt.append(str(quote_amount))
            feecur.append(quote_asset)
#
#        print(trade)


# create dataframe and save it a csv file
df = pd.DataFrame(fields)
df.to_csv('trades.csv')

# print(fields)
# print(dat)