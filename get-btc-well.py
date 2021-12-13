import os
import requests
from urllib import request
from datetime import date
today = date.today()
d1 = today.strftime("%Y-%m-%d")
d2 = today.strftime("%d.%m.%Y")
def rubs_to_btc(rubs):
	rubs = int(rubs)
	url = "https://pokur.su/rub/btc"
	try:
		zedik = request.urlopen(f'{url}/{rubs}/')
		lr = 0
		for line in zedik:
			zen = line.decode('utf-8')
			if " BTC " in zen:
				zer = zen.replace(f'<span class="pretty-sum">{rubs}</span> RUB <img src="/flags/ru.svg" width="24" height="24" alt="Государственный флаг России"> = ','')
				btcs = zer.replace(f'<img src="/flags/btc.svg" width="24" height="24" alt="Биткоин"> по курсу на <time datetime="{d1}">{d2}</time>.                            </p>','')
				btcc = btcs.replace('\n','')
				btccc = btcc.replace(' ','')
				btcccc = btccc.replace(' ','')
				btc = btcccc.replace('BTC','')
				return btc
				break
			lr += 1
	except:
		pass
def btc_to_rub(your_btc):
    url = "https://pokur.su/btc/rub"
    try:
    	btc = 1
    	zedik = request.urlopen(f'{url}/{btc}/')
    	lr = 0
    	for line in zedik:
    		zen = line.decode('utf-8')
    		if " BTC " in zen:
    			zer = zen.replace(f'<span class="pretty-sum">{btc}</span> BTC <img src="/flags/btc.svg" width="24" height="24" alt="Биткоин"> = ','')
    			btcs = zer.replace(f' RUB <img src="/flags/ru.svg" width="24" height="24" alt="Государственный флаг России"> по курсу на <time datetime="{d1}">{d2}</time>.                            </p>','')
    			btcc = btcs.replace('\n','')
    			btccc = btcc.replace(' ','')
    			btcccc = btccc.replace(' ','')
    			btcs = btcccc.replace('BTC','')
    			btcr2 = btcs.replace(',',' ')
    			btcr = ' '.join(word for word in btcr2.split()[:-1])
    			#print(f'Your btc:{your_btc},btcs:{btcs}')
    			return int(int(btcr)*your_btc)
    			break
    		lr += 1
    except:
    		pass
if __name__ == "__main__":
	print('Loaded')