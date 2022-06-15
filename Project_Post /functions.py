# importing the requests library
import requests
from datetime import date, datetime
#importing cryptographic modules
import hmac
import hashlib
  
# defining the api-endpoint 
MOCK_URL = "https://studios.sapphireapps.com/ct/q1"
HASH_SALT = "EXAMPLEKEY"


def post(client_id:str, media_url:str, description:str,timestamp):
    """This function posts a request"""

    # data to be sent to api
    data = {'client_id':client_id,
            'media_url':media_url,
            'timestamp':timestamp,
            'description':description
        }
    # sending post request and saving response as response object
    r = requests.post(url = MOCK_URL, data = data)
    # extracting response text 
    if r.status_code == 200:
        #encoding the response
        h = hmac.new(key= HASH_SALT.encode(), msg = r.content, digestmod= 'sha256')
        print(h.hexdigest())

    else:
        print("BAD REQUEST")
        print(f"{client_id}_{timestamp}: {description}")

