import requests
from bs4 import BeautifulSoup


# თიბისი ბანკი
def TBC_parser():
	TBC_r = requests.get("https://www.tbcbank.ge/web/ka/web/guest/exchange-rates?p_p_id=exchangeratessmall_WAR_tbcpwexchangeratessmallportlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_p_col_id=column-5&p_p_col_count=1")


	TBC_c = TBC_r.text
	TBC_soup = BeautifulSoup(TBC_c, "html.parser")
	TBC_data = TBC_soup.find('div', {"id":"ExchangeRates"})
	TBC_rows = TBC_data.find_all('div', {"class":"currency"})


	# USD ყიდვა/გაყიდვა
	TBC_USD_buy = float((TBC_rows[0].find('div', {'class':'currBuy'}).find('div', {'class':'currRate'}).text).strip())
	TBC_USD_sell = float((TBC_rows[0].find('div', {'class':'currSell'}).find('div', {'class':'currRate'}).text).strip())


	# EURO ყიდვა/გაყიდვა
	TBC_EUR_buy = float((TBC_rows[1].find('div', {'class':'currBuy'}).find('div', {'class':'currRate'}).text).strip())
	TBC_EUR_sell = float((TBC_rows[1].find('div', {'class':'currSell'}).find('div', {'class':'currRate'}).text).strip())

	return ([TBC_USD_buy, TBC_USD_sell], [TBC_EUR_buy, TBC_EUR_sell])