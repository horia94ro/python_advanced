import requests

# Configurăm o zonă de memorie ce ne permite să adăugăm monezile pentru care obținem cursul valutar
valuta = ['EUR', 'USD']

try:
    for current in valuta:
        # Am inclus cheia în cadrul request-ului. Această cheie trebuie înlocuită cu cea a contului vostru.
        url_baza = f'https://v6.exchangerate-api.com/v6/5bcc896a2e54340f132d8fa6/latest/{current}'
        resp = requests.get(url_baza)
        #Extragem JSON-ul ce conține rezultatele
        data = resp.json()
        #Extragem valoarea în RON a monezii analizate
        rata_conversie = data['conversion_rates']['RON']
        print(f"Cursul {current} este de: {round(rata_conversie, 2)} RON.")
except Exception as e:
    print(repr(e))