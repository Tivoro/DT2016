# DT2016
Undersökning av Android

Diverse scripts som jag skapat under kursen.

Python:
 - carv.py -> Hittar och karvar PDU data från en NAND dump. Modell: W800i
 - decode.py -> Decodar PDU data som carv.py har hittat. Endast stöd för GSM-7bit
 - carvk800i.py -> Hittar och karvar PDU data från en NAND dump. Modell: k800i
 - decodek800i.py -> Decodar PDU data som carvk800i har hittat. Endast stöd för GSM-7bit
 - txt2kml_1.py -> Konverterar GPS data till en KML fil som kan användas med google för kartläggning.
 - txt2kml_2.py -> Samma som ovan. Använder bara annan design för KML filen.
 
Assembly:
 - Uppgift3add4.asm -> Adderar 4 värden till EAX registret och skriver ut.
 - Uppgift4arrAdd.asm -> Kombinerarar två arrayer till en tredje, använder indirekt addressering.
 - Uppgift5arrAdd.asm -> Samma som ovan. Använder en annan metod.
 - Uppgift6XOR.asm -> XORar två strängar.
