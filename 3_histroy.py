from fyers_apiv3 import fyersModel
import pandas as pd
import credrential as crs
import datetime as dt


#credentials
client_id = crs.client_id
secret_key = crs.secret_key
redirect_uri = crs.redirect_uri


#--------------------access token-------------------------------
#read acess token
with open('access.txt') as f:
    access_token=f.read()


exchange = 'NSE'
sec_type = 'EQ'
symbol ='ONGC'

ticker = f"{exchange}:{symbol}-{sec_type}"
print(ticker)

fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path="")



# data = {
#     "symbol":ticker,
#     "resolution":"1",
#     "date_format":1,
#     "range_from":"2024-01-01",
#     "range_to":"2024-02-25",
#     "cont_flag":"1",
   
# }

current_date=dt.date.today()
data = {
    "symbol":ticker,
    "resolution":"1",
    "date_format":'1',
    "range_from":(current_date-dt.timedelta(days=30)),
    "range_to":current_date,
    "cont_flag":"1",
   
}

response = fyers.history(data=data)
# print(response)

histroy_df=pd.DataFrame(response['candles'])
# print(histroy_df)

# print("----------------------------------------------------------------")
# time and date converstion
histroy_df.columns=['date','open','high','low','close','volume']
histroy_df['date']=pd.to_datetime(histroy_df['date'],unit='s')
histroy_df.date=(histroy_df.date.dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata'))
histroy_df['date']=histroy_df['date'].dt.tz_localize(None)
histroy_df=histroy_df.set_index('date')
print(histroy_df)

# 





