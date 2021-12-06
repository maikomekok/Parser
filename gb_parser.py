import requests
from bs4 import BeautifulSoup


def GB_parser():

	G_r = requests.get("https://conditions.bog.ge/ge/services/treasury-operations/exchange-rates")
	G_c = G_r.text


	G_soup =  BeautifulSoup(G_c, "html.parser")
	G_data = G_soup.find('table', {"id":"AllDataTable"}).find("tbody").find_all('tr')


	# usd 
	GB_USD_buy = float((G_data[0].find_all("td")[-2].text).strip()) 
	GB_USD_sell = float((G_data[0].find_all("td")[-1].text).strip()) 

	# eur
	GB_EUR_buy = float((G_data[1].find_all("td")[-2].text).strip()) 
	GB_EUR_sell = float((G_data[1].find_all("td")[-1].text).strip()) 

	return ([GB_USD_buy, GB_USD_sell], [GB_EUR_buy, GB_EUR_sell])


GB_parser()
































# საქართველოს ბანკი
# def GB_parser():

# 	bank_rows = []
# 	buy_sell_tds = []

# 	bank_rows2 = []
# 	buy_sell_tds2 = []

# 	G_r = requests.get("https://www.lari.ge/index.php?do=currency/banks")
# 	G_c = G_r.text


# 	G_soup =  BeautifulSoup(G_c, "html.parser")
# 	G_data = G_soup.find('body')

# 	G_rows_USD = G_data.find('table', {"id":"USD"}).find_all('tr')
# 	G_rows_EUR = G_data.find('table', {"id":"EUR"}).find_all('tr')


# 	for item in G_rows_USD:
# 		bank_rows.append(item)


# 	for item in bank_rows[-3].find_all('td'):
# 		buy_sell_tds.append(item)



# 	for item in G_rows_EUR:
# 		bank_rows2.append(item)


# 	for item in bank_rows2[-3].find_all('td'):
# 		buy_sell_tds2.append(item)

# 	# usd 
# 	GB_USD_buy = float((buy_sell_tds[1].text).strip()) 
# 	GB_USD_sell = float((buy_sell_tds[2].text).strip()) 

# 	# eur
# 	GB_EUR_buy = float((buy_sell_tds2[1].text).strip()) 
# 	GB_EUR_sell = float((buy_sell_tds2[2].text).strip()) 

# 	return ([GB_USD_buy, GB_USD_sell], [GB_EUR_buy, GB_EUR_sell])