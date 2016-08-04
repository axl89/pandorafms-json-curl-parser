#!/bin/env python
import pycurl
import json
import sys
from StringIO import StringIO

u"""
Usage instructions:

        python pandorafms_jsonparser.py "http://you_url_which_returns_json/" json_key1 [json_key2] [json_key3]...

        Having this JSON
		
		{
				"count": 9,
				"next": null,
				"previous": null,
				"results": [{
						"url": "http://your_other_awesome_url",
						"id": "ELwaa4bC8",
						"language": "es",
						"timestamp": "2016-07-28T11:44:39",
				}]

		}
		
        To get the id inside results, we just need to indicate the order of the keys of the JSON to get to it

        >>> python pandorafms_jsonparser.py "http://you_url_which_returns_json/" results 0 id
                ELwjZ4bC8
"""

#Get the arguments and store them in l
l = sys.argv

#Create a buffer to store the curl response
buffer = StringIO()

#Create the Curl object and perform the request to the first argument (the URL)
c = pycurl.Curl()
c.setopt(c.URL, sys.argv[1])
c.setopt(c.WRITEFUNCTION, buffer.write)
c.perform()

#Parse the result to JSON and store it in json_response
json_response = json.loads(buffer.getvalue())
tmp = json_response


#Now we iterate over the remaining arguments
for key in l[2:]:
    if key.isdigit():
        tmp = tmp[int(key)]
    else:
        tmp = tmp[key]

print tmp
