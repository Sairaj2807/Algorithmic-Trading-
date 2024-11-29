import credrential as crs
# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel
import webbrowser

# Replace these values with your actual API credentials
client_id = crs.client_id
secret_key = crs.secret_key
redirect_uri = crs.redirect_uri
response_type = "code"
state = "sample_state"
grant_type = "authorization_code"
# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type
)

# Generate the auth code using the session model
response = session.generate_authcode()

# Print the auth code received in the response
print(response)

webbrowser.open(response,new=1)


#authcode_create
newurl = input("enter the url : ")
auth_code = newurl[newurl.index('auth_code')+10:newurl.index('&state')]
print(auth_code)

session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key, 
    redirect_uri=redirect_uri, 
    response_type=response_type, 
    grant_type=grant_type
)

# Set the authorization code in the session object
session.set_token(auth_code)

# Generate the access token using the authorization code
response1 = session.generate_token()

# Print the response, which should contain the access token and other details
print(response1)

#create new text file with access_token 
try:
    access_token = response1["access_token"]
    with open('access.txt','w') as k:
        k.write(access_token)
except Exception as e:
    print(e,response1)         