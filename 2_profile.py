from fyers_apiv3 import fyersModel
import pandas as pd
import credrential as crs

#credentials
client_id = crs.client_id
secret_key = crs.secret_key
redirect_uri = crs.redirect_uri


#--------------------access token-------------------------------
#read acess token
with open('access.txt') as f:
    access_token=f.read()
#print(access_token)  


#---------------------------profile-----------------------------------------
# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

# Make a request to get the user profile information
response_profile = fyers.get_profile()

# Print the response received from the Fyers API
print(response_profile)

print("                                                                            ")

print("------------    ---------------------    -------------------    ------------")


#--------------------------FUNDS-----------------------------
# Make a request to get the funds information
response_funds = fyers.funds()
#print(response_funds)

#seperate dict
data_funds=response_funds.get('fund_limit')
#print(data_funds)


#converts into data frame using pandas
df=pd.DataFrame(data_funds)
print(df)
print("                                                     ")
print("-------------------------   ------------------   ----------------")
#-------------------order placed by algo ----------------------
order_response = fyers.orderbook()
#print(order_response)
if order_response['orderBook']:
    order_df=pd.DataFrame(order_response['orderBook'])
else:
    order_df=pd.DataFrame()

print(order_df) 
print("                                     ")
print(" ----------- ---------------   ----------------  ----------------")

order_df.to_csv('order.csv')

#--------------------- Position -----------------------

position_response=fyers.positions()
#print(position_response)
if position_response['netPositions']:
    position_df = pd.DataFrame(position_response['netPositions'])
else:
    position_df = pd.DataFrame()
print(position_df)    
        


#----------------- Tradebook -----------------------------
trade_response=fyers.tradebook()
#print(trade_response)
if trade_response['tradeBook']:
    trade_df=pd.DataFrame(trade_response['tradeBook'])  
else:
    trade_df=pd.DataFrame()
print(trade_df)               








