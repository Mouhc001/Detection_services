import modules.TI.threat_intelligence as TI
import modules.virusTotal.vt as VT
import os
import json
import sys
    
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py config.json")
        return

    config_file = sys.argv[1]

    try:
        with open(config_file, "r") as f:
            config = json.load(f)
            vt_key = config.get("vt_key")
            abuse_key = config.get("abuse_key")
            
    except FileNotFoundError:
        print(f"Le fichier de configuration {config_file} n'a pas été trouvé.")
        return 
    except json.JSONDecodeError:
        print(f"Le fichier de configuration {config_file} n'est pas au format JSON valide.")
        return 
        
    #The ip_to_search should be extracted from the flow automatically
    ip_to_search = "88.204.166.59" 

    print(">>>>>>>>> VirusTotal <<<<<<<")
    vt = VT.virusTotal(vt_key)
    print(vt.main(ip_to_search))
    
    print(">>>>>>>>> Threat Intelligence <<<<<<<")

    TI_folder = os.getcwd() + "/modules/TI/"
    download_file = TI_folder + "download.sh"
    feed_folder = TI_folder + "feed"
    ti = TI.ThreatIntelligence(download_file, abuse_key, feed_folder)
    print(ti.main(ip_to_search))
    
if __name__ == "__main__" :
    main()
