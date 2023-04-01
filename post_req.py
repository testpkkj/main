import requests
import json
from pprint import pprint
from datetime import datetime,date

# Find today time
time = datetime.now()
print(time)
today = date.today()
start = datetime.now()
#today = today - timedelta(days = 1)
# mm/dd/y
d3 = today.strftime("%Y-%m-%d")
print("d3 =", d3)


# Define the URL to send the request to
url = "https://soapbox.dishhome.com.np/soapboxwebws/live/epg"

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
1000,
"a": 
False,
"programmeDate": 
d3
}

def find_id_in_array(id, arr):
    # filtered_array = list(filter(lambda x: x.get('id') != id, arr))
    filtered_array = list(filter(lambda x: x[1] != id, arr))
    return filtered_array[0] if len(filtered_array) > 0 else None

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
filtered_epg_data=[] #Channel With less EPG event
Stored_epg_data =[] #channel list detch from API

for data in got_data["data"]:
    if((len(data["epg"])<18)):
        temp =data["title"],data["id"]
        filtered_epg_data.append(temp)
    temp2= data["title"],data["id"]
    Stored_epg_data.append(temp2)

# fw =open('./temp.txt',"w")

# # Write a string to the file
# fw.write(str(Stored_epg_data))

# # Close the file
# fw.close()
#print("ssss",Stored_epg_data)
#Opening Fixed store data

  
# Opening fixed_JSON file
fixedfile = open('../fixed.json')
  
fixedfile_json = json.load(fixedfile)

#Finding missing channel list from EPG_Data_Object and fixed.json

missing_epg =[]
for i in fixedfile_json:
    for j in Stored_epg_data:
        if( i["id"]==j[1]):
            status = 1
            break
        else:
            status = 0
    if(status == 0):
        missing_epg.append(i)
print(missing_epg)   


fixedfile.close()
