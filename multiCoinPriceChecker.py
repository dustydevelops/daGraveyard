
import cbpro, time, numpy
from apiShit import auth_client

def account(iD):
 for account in auth_client.get_accounts():
  if account['currency'] == iD:
   return account['id']

  
while True:
 currencies = ['BTC-USD','ETH-USD','LTC-USD', 'XTZ-USD']
 
 currency = currencies[0]
 price = float(auth_client.get_product_ticker(product_id=currency)['price'])
 print(price)

 currency = currencies[1]
 price = float(auth_client.get_product_ticker(product_id=currency)['price'])
 print(price)
 
 currency = currencies[2]
 price = float(auth_client.get_product_ticker(product_id=currency)['price'])
 print(price)
 
 currency = currencies[3]
 price = float(auth_client.get_product_ticker(product_id=currency)['price'])
 print(price)
 time.sleep(5)

'''  except Exception as e:
   print(e)'''
