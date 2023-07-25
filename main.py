import modules.TI.threat_intelligence as TI
import modules.virusTotal.vt as VT
import os
import json

def read_config_file():
    with open(os.getcwd()+"/config.json") as config:
        data_config = json.load(config)
    return data_config
    
def main():

    #The ip_to_search should be extracted from the flow automatically
    ip_to_search = "88.204.166.59" 
    data_config = read_config_file()

    print(">>>>>>>>> VirusTotal <<<<<<<")
    vt_key = data_config.get("VT_API_KEY")
    print(VT.main(ip_to_search, vt_key))
    print(">>>>>>>>> Threat Intelligence <<<<<<<")
    TI_folder = data_config.get("TI_path")
    download_file = TI_folder + "download.sh"
    feed_folder = TI_folder + "feed"
    abuse_key = data_config.get("ABUSE_API_KEY")
    print(TI.main(ip_to_search, download_file, feed_folder, abuse_key))
    
if __name__ == "__main__" :
    main()
