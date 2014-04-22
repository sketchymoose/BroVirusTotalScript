BroVirusTotalScript
===================

This is a collection of scripts which can work in combination with Bro file extraction. It consists of two scripts which take the PE32 files from a directory, hash them, and pass those hashes to VirusTotal. If any results are observed in VT, they are written to a file. More information about this can be found on the following blog post:


runMD5.sh: This is the script which is directly invoked. It takes 3 agruments. 
 1 -> directory of extracted_files
 2 -> directory of where you want the VT Results to 
 3 -> full path of where you want the MD5.txt file
 
SubmitMD5VT.py: This script is invoked by the shell script, but it can be run on its own. It takes 2 arguments:

 1 -> Directory where the results will be saved to (the filename is VirusTotalResults.txt)
 2 -> Full path of the MD5.txt file which will be passed to VirusTotal
 
 Please remember you need a VT API for this! Search in the python script for \<Insert VT API Key Here\> and replace with your API key. If you have a free version, uncomment out the sleep commands and it should work fine in the restriction of the API. 
