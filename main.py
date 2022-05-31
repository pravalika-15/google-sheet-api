# importing the Nse() function from the nsetools library  
from nsetools import Nse


  
# creating an NSE object  
nse_obj = Nse()  
stock_name = input("please enther the stock name: ")

try:
  # getting quotation of the company  
    the_quotation = nse_obj.get_quote(stock_name)  
  
# printing the name of the company  
    print(the_quotation["companyName"])  
    print(the_quotation["lastPrice"])   #printing the stock latest price
except:
  print("An error occurred! invalid stock name!")
