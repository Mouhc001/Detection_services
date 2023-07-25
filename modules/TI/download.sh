#!/bin/bash

data_config=$( cat config.json )
eval "ti_folder=$( echo ${data_config} | jq -r ".TI_path" )"
DB_size=$( cat $( dirname ${ti_folder} )/TI/TI_feeds.csv | grep "^https" | wc -l )

if [ $( ls ${ti_folder}/feed | wc -l ) -lt ${DB_size} ]
then
    cd ${ti_folder}/feed
    echo "filling DB"
    for link in $( cat ../TI_feeds.csv | cut -d',' -f 1 )
    do
	if [[  ${link} =~ ^https ]]
	then
	    file_name=$( basename ${link} )
	    if [ ! -f ${file_name} ]
	    then
		wget ${link} > /dev/null 2>&1
		echo -n "."
	    fi
	fi
    done
    echo "" 
    
    # echo ">>>>>>>>>>>>>>>>>>>>>>> abuseIPDB"
    # python3 ../abuseIPDB.py

fi
