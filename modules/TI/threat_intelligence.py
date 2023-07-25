import os 
import subprocess
import json
import requests


#Fills the database according to the path of the feed folder
#params:
#download_file: a bash script that download links in the feed_folder
#abuse_api_key: calls the abuseIPDB API to fill the file abuseIPDB.txt used also as a feed to the TI module

def fill_db(download_file, abuse_api_key, feed_folder):
    download_file = os.path.expanduser(download_file)
    #fill_database_with_abuseipdb(abuse_api_key, feed_folder)
    try :
        subprocess.run(['bash', download_file], check = True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error occured while filling the TI database: {e}")
        return False

#Searchs for the given ip in the feed_folder
def search_for_ip(ip, feed_folder):
    path = None
    feed_folder = os.path.expanduser(feed_folder)+"/"
    is_found = False
    for feed_file in os.listdir(feed_folder):
        with open(feed_folder+feed_file, 'r') as f:
            for line_number, line in enumerate(f, start = 1):
                if ip in line:
                    path=f"{feed_file},  Line: {line_number}"
                    is_found = True

    return (is_found, path)
    
# def search_for_domain(domain):
#     feed_folder = "feed"
#     is_found = 0
#     for feed_file in os.listdir(feed_folder):
#         print(feed_file)
#         with open("feed/"+feed_file, 'r') as f:
#             for line_number, line in enumerate(f, start = 1):
#                 if domain in line:
#                     print("File: ", feed_file,  "\tLine: " , line_number)
#                     is_found = 1

#     if is_found == 1:
#         return True
#     return False


#Used for reporting once the ip is found malicious
def set_malicious_ip(ip) :
    pass

def set_malicious_domain(ip) :
    pass


############ AbuseIPDB ###############

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
                
                with open(feed_folder+"/abuseIPDB.txt", 'a+') as feed:
                    feed.write(str(ip_address) + ', ' + str(threat_level) + ', ' + str(country) + '\n')
            print('La base de données a été mise à jour avec succès.')
        else:
            print('Erreur lors de la requête API :', response.status_code)
    except requests.exceptions.RequestException as e:
        print('Une erreur s\'est produite lors de la requête API :', str(e))


########################################################################

def main(ip, download_file, feed_folder, abuse_api_key):
    #First we fill the database with malicious iocs
    if fill_db(download_file, abuse_api_key, feed_folder):
        print("DB filled successufully")

        search_result = search_for_ip(ip, feed_folder)
        is_found = search_result[0]
        path = search_result[1]
        #If the ioc is found malicious
        if is_found :
            return f"Malicious IP found {ip} in {path}"

        else:
            pass
    else :
        return "DB could not be filled"

#__name__ == "__main__"

# main()
