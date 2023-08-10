## Project
Package that contains modules to be added to Sonic project: VirusTotal and ThreatIntelligence

## Modules
The Two modules accept an IP address as an input (so fat, domains can be added too ..) and answers wheter the IP given is malicious or not
Threat intelligence module fills  a database of malicious iocs and look for the given IP inside of it.

## configuration
A config.json should be in the same folder as main.py, and must contain the two keys : "vt_key" and "abuse_key"

## Running
The main.py contains a call for both modules

python3 main.py config.json 

## Tests
cd test; pytest -v
