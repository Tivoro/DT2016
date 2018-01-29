import json
import urllib.request

def initKML(output):
	output.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
	output.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">")
	output.write("<Folder>")
	
def writePoint(output, x, y, timestamp):
	output.write("<Placemark><name>Marker_%s</name><description>%s</description>" % (count, timestamp))
	output.write("<Point><coordinates>%s,%s</coordinates></Point>" % (x, y))
	output.write("</Placemark>")
	
def finKML(output):
	output.write("</Folder></kml>")
	
def getPosition(CID, LAC, MCC):
	#Build the JSON request
	reqData = {
		"cellTowers": [
			{
				"cellId": CID,
				"locationAreaCode": LAC,
				"mobileCountryCode": MCC
			}
		]
	}
	#Encode the request to JSON
	params = json.dumps(reqData).encode("UTF-8")
	#Send the request
	req = urllib.request.Request(URL + API_KEY, data=params, headers={"content-type": "application/json"})
	#Read the response
	response = urllib.request.urlopen(req)
	#Convert the HTTPResponse object
	str = json.load(response)
	#Return location data
	return str["location"]
	
API_KEY = "AIzaSyA2HsDqW6VUsUEiok0-snFR_3-KVIZWA98"
URL = "https://www.googleapis.com/geolocation/v1/geolocate?key="
source = "cellid_suspect.txt"
dest = "kml.kml"

count = 0
with open(source, 'r') as file, open(dest, 'w') as output:
	initKML(output)
	line = file.readline()
	while line:
		data = line.split(',')
		location = getPosition(data[0], data[1], data[2])
		writePoint(output, location["lng"], location["lat"], data[3])
		
		count += 1
		line = file.readline()
	finKML(output)
	file.close()
	output.close()