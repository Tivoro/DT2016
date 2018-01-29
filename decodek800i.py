import re
import math
import binascii

def fixNumber(number):
	numToString = decodeMessage(number, "")
	if re.match("[A-Za-z|\s]{9}", numToString):
		return numToString

	rev = ""
	for byte in number:
		rev += byte[::-1]
	if "F" in rev[-1:]:
		rev = rev[:-1]
	return rev
	
def fixDate(date):
	rev = ""
	rev += "20" + date[0][::-1] + "/" + date[1][::-1] + "/" + date[2][::-1] + " "
	rev += date[3][::-1] + ":" + date[4][::-1] + ":" + date[5][::-1] + " "
	
	binGMT = bin(int(date[6],16)).lstrip('0b')
	#binGMT = bin(int("8a",16)).lstrip('0b') #<--- Från wiki för test
	if "1" in binGMT[4:5]:
		rev += "GMT-"
	else:
		rev += "GMT+"
	binGMT = int((int(hex(int(binGMT,2) & 247).lstrip('0x')[::-1],16)*15)/60) # https://en.wikipedia.org/wiki/GSM_03.40#Time_Format
	rev += str(binGMT)
	
	return rev

# Just nu bara stöd för GSM 7-bit
# Lösningen är stulen från (fick inte det att fungera själv): https://stackoverflow.com/questions/19530646/python-decode-gsm-sms-message-in-pdu
def decodeMessage(encMsg, encType):
	number = 0
	bitcount = 0
	output = ''
	for byte in encMsg:
		number = number + (int(byte,16) << bitcount)
		bitcount = bitcount + 1
		if number%128 == 15:
			output = output + '%s' % ('å')
		elif number%128 == 123:
			output = output + '%s' % ('ä')
		elif number%128 == 124:
			output = output + '%s' % ('ö')
		else:
			output = output + '%c' % (number % 128)
		number = number >> 7
		if bitcount == 7:
			if number == 15:
				output = output + '%c' % ('å')
			elif number == 123:
				output = output + '%c' % ('ä')
			elif number == 124:
				output = output + '%c' % ('ö')
			else:
				output = output + '%c' % (number)
			bitcount = 0
			number = 0
	#return ''.join(r'\x{0:x}'.format(ord(c)) for c in output)
	return output
	
encPDUs = []
encPDU = []
#Get encoded pdus
with open("encodedPDU.txt", "r") as file:
	byte = file.read(1)
	while byte:
		if "\n" in byte:
			encPDUs.append(encPDU)
			encPDU = []
			byte = file.read(1)
			continue
		else:
			byte += file.read(1)
			encPDU.append(byte)
		byte = file.read(1)

with open("decodedPDU.txt", "w") as file:
	c = 0
	for pdu in encPDUs:
		c += 1
		i = 0
		status = int(pdu[i],16); i += 1
		status2 = int(pdu[i],16); i += 1
		smscLen = int(pdu[i],16) - 1; i += 1
		smscType = pdu[i]; i += 1
		file.write("SMSC number: %s\n" % (fixNumber(pdu[i:i+smscLen]))); i += smscLen
		
		i += 5 # Plocka bort "FFFFFFFF.."
		if status2 == 2: #Det verkar som när stats är 2 så följer där en byte som jag inte vet vad den är
			i += 1
		
		smsType = pdu[i]; i += 1
		senderLen = int(pdu[i],16); i += 1
		senderType = int(pdu[i],16); i += 1
		file.write("Sender number: %s\n" % (fixNumber(pdu[i:i+math.ceil(senderLen/2)]))); i += math.ceil(senderLen/2)
		
		tpPID = pdu[i]; i += 1
		encType = pdu[i]; i += 1
		ts = ""; valPeriod = ""
		if smsType == "04":	# Stulen från smsdecode.py
			file.write("Timestamp: %s\n" % (fixDate(pdu[i:i+7]))); i += 7
		else:
			valPeriod = pdu[i]; i += 1
		
		msgLen = math.ceil((int(pdu[i],16)*7)/8); i += 1 #Försöker få bort lite skräp data i slutet, fungerade typ
		file.write("Message: %s\n" % (decodeMessage(pdu[i:i+msgLen], encType)))
			
		file.write("\n\n\n")
	

	
