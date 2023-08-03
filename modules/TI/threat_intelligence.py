import os 
import subprocess
import json
import requests
from . import download

#Fills the database according to the path of the feed folder
#params:
#download_file: a bash script that download links in the feed_folder
#abuse_api_key: calls the abuseIPDB API to fill the file abuseIPDB.txt used also as a feed to the TI module

class ThreatIntelligence:

    def __init__(self, TI_feed, key, feed_folder):
        if not TI_feed or not key or not feed_folder:
            raise TypeError("Arguments cannot be None or empty")
        self.download_file = os.path.expanduser(TI_feed)
        self.abuse_api_key = key
        self.feed_folder = feed_folder
        
    def fill_db(self):
        #fill_database_with_abuseipdb(abuse_api_key, feed_folder)
        # try :
        #     subprocess.run(['bash', self.download_fil], check = True)
        #     return True
        # except subprocess.CalledProcessError as e:
        #     print(f"Error occured while filling the TI database: {e}")
        #     return False

        return download.download_files(os.path.dirname(self.feed_folder))
        
        #Searchs for the given ip in the feed_folder
    def search_for_ip(self, ip, feed_folder):
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
    def set_malicious_ip(self, ip) :
        pass
    
    def set_malicious_domain(self, ip) :
        pass
    
    
    
    def main(self, ip):
        #First we fill the database with malicious iocs
        filled = self.fill_db()
        print("filled = ", filled)
        if filled == True:
            print("DB filled successufully")
            
            search_result = self.search_for_ip(ip, self.feed_folder)
            is_found = search_result[0]
            path = search_result[1]
            #If the ioc is found malicious
            if is_found :
                return f"Malicious IP found {ip} in {path}"
            
            else:
                pass
        else :
            return "DB could not be filled"
