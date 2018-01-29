import re
import binascii

pdus = []
bytesRead = 0

#Find pdus
with open("k800iNAND.bin", 'rb') as file:
	byte = binascii.hexlify(file.read(16))
	bytesRead += 16
	while byte:
		pdu = b''
		#if re.match(b"(ff){5}", byte):
		#	byte = binascii.hexlify(file.read(3))
		if re.match(b"01(00|01|02)0791", byte):
			#byte += binascii.hexlify(file.read(13))
			#bytesRead += 16
			while re.match(b"(ff){5}", byte) is None:
				pdu += byte
				byte = binascii.hexlify(file.read(16))
				bytesRead += 16
			pdu += byte
			pdus.append(pdu)
		#else:
		#	byte += binascii.hexlify(file.read(13))
		#	bytesRead += 16
		byte = binascii.hexlify(file.read(16))
		bytesRead += 16
		
print ("Bytes read: %s" % (bytesRead))
print ("PDUs found: %s" % (len(pdus)))

#Clean pdus
for i in range(0, len(pdus)):
	cleanPdu = []
	for byte in range(0, len(pdus[i]), 2):
		cleanPdu.append(pdus[i][byte:byte+2])
	for byte in range(len(cleanPdu)-1,-1,-1):
		if cleanPdu[byte] == b"ff":
			cleanPdu.pop(byte)	#Remove trailing FF
		else:
			break
	pdus[i] = b"".join(cleanPdu)
	
#Write pdus to encodedPDU.txt	
with open("encodedPDU.txt", "w") as file:
	for p in pdus:
		file.write(p.decode("utf-8").upper())
		file.write("\n")