import requests
import json
import os
#API_key 85f871fd5a565f2ee0f280392b108107c01c7da97feaf9b46c81d26cab08d7d32bc5002c00b81ffa

import requests

def fill_database_with_abuseipdb(api_key, feed_folder):
    base_url = 'https://api.abuseipdb.com/api/v2/'

    # Exemple de paramètres de requête pour obtenir les adresses IP malveillantes signalées
    query_params = {
        'limit': 10000#,  # Nombre maximal d'adresses IP à récupérer
        #'confidenceMinimum': 50 ,  # Niveau de confiance minimum pour les signalements
    }

    headers = {
        'Key': api_key,
        'Accept': 'application/json',
    }

    try:
        response = requests.get(base_url + 'blacklist', params=query_params, headers=headers)
        if response.status_code == 200:
            malicious_ips = response.json().get('data', [])
            # # Parcourir les adresses IP malveillantes et les ajouter à votre base de données
            for ip in malicious_ips:
                ip_address = ip['ipAddress']
                threat_level = ip['abuseConfidenceScore']
                country = ip['countryCode']
                #     description = ip['abuseSeverity']
                #     tags = ip['abuseTags']

                if not os.path.exists("abuseIPDB.txt"):
                    open("abuseIPDB.txt", 'w').close()
                
                with open(feed_folder+"abuseIPDB.txt", 'a') as feed:
                    feed.write(str(ip_address) + ', ' + str(threat_level) + ', ' + str(country) + '\n')
            print('La base de données a été mise à jour avec succès.')
        else:
            print('Erreur lors de la requête API :', response.status_code)
    except requests.exceptions.RequestException as e:
        print('Une erreur s\'est produite lors de la requête API :', str(e))

