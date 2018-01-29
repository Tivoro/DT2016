def initKML(output):
	output.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
	output.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">")
	output.write("<Folder><Placemark><name>LineMarker</name><description>For effect!</description>")
	output.write("<LineString><coordinates>")
	
def writeLine(output, x, y, z):
	output.write("%s,%s,%s\n" % (x, y, z))
def writePoint(output, x, y, z, speed, timestamp):
	output.write("<Placemark><name>Marker_%s</name><description>%s\nSpeed: %s</description>" % (count, timestamp, speed))
	output.write("<Point><coordinates>%s,%s,%s</coordinates></Point>" % (x, y, z))
	output.write("</Placemark>")
	
def finLine(output):
	output.write("</coordinates></LineString>")
	output.write("</Placemark>")
def finKML(output):
	output.write("</Folder></kml>")

source = "navlog.txt"
dest = "kml.kml"


#Write KML data for the line
with open(source, 'r') as file, open(dest, 'w') as output:
	initKML(output)
	
	line = file.readline()
	while line:
		data = line.split(';')
		writeLine(output, data[1], data[0], data[2])
		
		line = file.readline()
	finLine(output)
	file.close()
	output.close()

#Write points and close KML file
count = 0
clutterCount = 0
with open(source, 'r') as file, open(dest, 'a') as output:
	line = file.readline()
	while line:
		data = line.split(';')
		data[5] = data[5][:-1] #Remove \n
		
		#writePoint(output, data[1], data[0], data[2], data[4], data[5])
		#A fix to draw every 10:th point (Became too cluttered otherwise)
		if(clutterCount == 0):
			writePoint(output, data[1], data[0], data[2], data[5])
			count += 1
			clutterCount = 10
		else:
			clutterCount -= 1
		
		line = file.readline()
	finKML(output)
	file.close()
	output.close()