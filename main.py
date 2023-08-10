import modules.TI.threat_intelligence as TI
import modules.virusTotal.vt as VT
import os
import json

    
def main():

    #The ip_to_search should be extracted from the flow automatically
    ip_to_search = "88.204.166.59" 

    print(">>>>>>>>> VirusTotal <<<<<<<")
    vt_key = "ea70c492edb06211d4a2f269890021c4634c21029be7e40f66afc8f6b90960a6" 
    vt = VT.virusTotal(vt_key)
    print(vt.main(ip_to_search))
    
    print(">>>>>>>>> Threat Intelligence <<<<<<<")

    TI_folder = os.getcwd() + "/modules/TI/"
    download_file = TI_folder + "download.sh"
    feed_folder = TI_folder + "feed"
    abuse_key = "85f871fd5a565f2ee0f280392b108107c01c7da97feaf9b46c81d26cab08d7d32bc5002c00b81ffa"
    ti = TI.ThreatIntelligence(download_file, abuse_key, feed_folder)
    print(ti.main(ip_to_search))
    
if __name__ == "__main__" :
    main()
