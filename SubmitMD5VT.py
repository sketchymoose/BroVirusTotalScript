#VirusTotal MD5 Hash Submission
#By Sketchymoose
#Version 1.0

import os
import hashlib
import urllib
import urllib2
import simplejson
import time
import sys

output=sys.argv[1]
filename=sys.argv[2]

VTResultsPath = os.path.join(os.path.abspath(output), "VirusTotalResults.txt")
VTResults = open(VTResultsPath, 'a')
f = file(filename, "rb")
for line in f.readlines():
	hashValue= line.split(' ')[0]
	#hashValue = line
	#print hashValue
        
        #first check and see if there is any response from uploading the MD5
        url = "https://www.virustotal.com/vtapi/v2/file/report"
        parameters = {"resource": hashValue,
		      "apikey": "<Insert VT API Key Here>"}
        data = urllib.urlencode(parameters)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        json = response.read()
        

        response_dict = simplejson.loads(json)
        toot = response_dict.get("positives")
        #print toot
        if str(toot) == "None":
            errorStatement = "Hash not found in VirusTotal Database... may need to upload\n\n"
            VTResults.write(errorStatement)
            #time.sleep(15)
        else:
            Symantec = response_dict.get("scans", {}).get("Symantec", {}).get("result")
            Microsoft = response_dict.get("scans", {}).get("Microsoft", {}).get("result")
            McAfee = response_dict.get("scans", {}).get("McAfee", {}).get("result")
            Kaspersky = response_dict.get("scans", {}).get("Kaspersky", {}).get("result")
            permalink = response_dict.get("permalink", {})

            getHashValue= "MD5 Hash: " + str(hashValue) + "\n"
	    numberHits = "Number of positive hits: " + str(toot) + "\n"
            link = "Link: " + str(permalink) + "\n"
            mcAfeeStr = "McAfee says its " + str(McAfee) + "\n"
            symantecStr = "Symantec says its " + str(Symantec) + "\n"
            microsoftStr = "Microsoft says its " + str(Microsoft) + '\n'
            kasperskyStr = "Kaspersky says its " + str(Kaspersky) + "\n\n"
            VTResults.write(getHashValue)
	    VTResults.write(numberHits)
            VTResults.write(link)
            VTResults.write(mcAfeeStr)
            VTResults.write(symantecStr)
            VTResults.write(microsoftStr)
            VTResults.write(kasperskyStr)

            #time.sleep(15)

VTResults.close()
print "Check your results!"
