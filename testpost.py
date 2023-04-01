import requests
import json
from pprint import pprint

# Define the URL to send the request to
url = "https://soapbox.dishhome.com.np/soapboxwebws/live/epg";

# Define the JSON data to send in the request body
data = {
    "startTimeTimestamp": 
1680286500000,
"stopTimeTimestamp": 
1680372900000,
"account_id": 
1,
"offset": 
0,
"limit": 
10,
"a": 
False,
"programmeDate": 
"2023-04-01"
}

# Convert the JSON data to a string
json_data = json.dumps(data)

# Define the headers for the request
headers = {
    "Content-Type": "application/json"
}

# Send the POST request with the JSON data in the request body
response = requests.post(url, data=json_data, headers=headers)

# Print the response from the server
# print(response.text)
#pprint(json.loads(response.text))
got_data=json.loads(response.text)
filtered_epg_data=[]
Stored_epg_data =[]

for data in got_data["data"]:
    if((len(data["epg"])<18)):
        temp =data["id"],data["title"]
        filtered_epg_data.append(temp)
    

#Opening Fixed store data
fixedfile = open('DS/fixed.json',"rb")
print(fixedfile)
# fixedfile_json= json.loads(fixedfile)

# for i in fixedfile[id]:
#     if(i["id"] == 37):
#         print(i)


fixedfile.close()