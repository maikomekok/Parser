import requests, json
from bs4 import BeautifulSoup

# ეროვნული ბანკი
def EB_parser():
	
	EB_url = "https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/ka/json"
	response = requests.request("GET", EB_url)

	data = json.loads(response.text)

	EB_USD = None
	EB_EUR = None

	
	for index, currency in enumerate(data[0]['currencies']):
	    if currency["code"] == "USD":

	        EB_USD = float(currency["rate"])

	    elif currency["code"] == "EUR":
	    	EB_EUR = float(currency["rate"])
	    
	return ([EB_USD, EB_USD], [EB_EUR, EB_EUR])
