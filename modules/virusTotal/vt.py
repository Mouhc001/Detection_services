import requests
import json

# In case of checking multiple ioc (IP, domain or URL), this class could be useful
# class IOC:
#     def __init__(self, ioc_type, ioc):
#         self.ioc_type = ioc_type
#         self.ioc = ioc


#Calls the virusTotal API
def query_vt_apiv3(ip, key):
    headers = {
        "accept": "application/json",
        "x-apikey": key
    }

    # if ioc.ioc_type == "ip":
    #     url = "https://www.virustotal.com/api/v3/ip_addresses/" + ioc.ioc

    # elif ioc.ioc_type == "domain":
    #     url = "https://www.virustotal.com/api/v3/domains/"+ioc.ioc
    # elif ioc.ioc_type == "url":
    #     url = "https://www.virustotal.com/api/v3/urls/"+ioc.ioc

    url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip
    response = requests.get(url, headers=headers)
    return json.loads(response.text)

#Used to extract useful info from the API answer
#Different kind of returns this function could have, check the API documentation for more info
def interpret_response(response):
    data = response["data"]
    attributes = data["attributes"]
    last_analysis_stats = attributes["last_analysis_stats"]
    harmless = last_analysis_stats["harmless"]
    malicious = last_analysis_stats["malicious"]
    undetected = last_analysis_stats["undetected"]
    total = harmless + malicious + undetected
    #print(data["data"]["attributes"]["last_analysis_stats"])
    #print("score = ", malicious,"/", total)
    return malicious


def main(ip, key):
    report = query_vt_apiv3(ip, key)
    return interpret_response(report)


