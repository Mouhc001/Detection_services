import requests
import json

#Calls the virusTotal API
class virusTotal:

    def __init__(self, vt_api_key):
        self.key = vt_api_key
        
    def query_vt_apiv3(self, ip):
        headers = {
            "accept": "application/json",
            "x-apikey": self.key
        }
        
        
        url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip
        response = requests.get(url, headers=headers)
        return json.loads(response.text)

    #Used to extract useful info from the API answer
    #Different kind of returns this function could have, check the API documentation for more info
    def interpret_response(self, response):
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
    

    def main(self, ip):
        response = self.query_vt_apiv3(ip)
        return self.interpret_response(response)


