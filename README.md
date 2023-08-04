## Project
Package that contains modules to be added to Sonic project: VirusTotal and ThreatIntelligence

## Modules
The Two modules accept an IP address as an input (so fat, domains can be added too ..) and answers wheter the IP given is malicious or not
Threat intelligence module fills  a database of malicious iocs and look for the given IP inside of it.

## configuration
So far, the API keys are set in the config.json file, this will be changed as soon as possible.

## Running
The main.py contains a call for both modules

## Tests
cd test; pytest -v
