TITLE XOR encryption/decryption
; This program combines two arrays into a third by using indirect addressing

INCLUDE Irvine32.inc

XORVAL = 239
SSIZE = 80

.data
prompt1 BYTE "Enter a string: ",0
prompt2 BYTE "Encrpyted string: ",0
prompt3 BYTE "Decrypted string: ",0
oString BYTE SSIZE DUP(0),0
cString BYTE ?

.code
main PROC
; Prompt the user to enter a string and then store it in oString and cString
	mov edx,OFFSET prompt1
	call WriteString
	mov edx,OFFSET oString
	mov ecx,80
	call ReadString

; XOR all chars in oString and store them in cString
	mov esi,0
	L1:
		mov al,oString[esi]
		xor al,XORVAL
		mov cString[esi],al
		
		inc esi
		cmp oString[esi], 0h
		jne L1

; Print the encrypted string
	mov edx,OFFSET prompt2
	call WriteString
	mov edx,OFFSET cString
	call WriteString

; Decrypt cString by XOR(ing?)
	mov oString,0h
	mov esi,0
	L2:
		mov al,cString[esi]
		xor al,XORVAL
		mov oString[esi],al

		inc esi
		cmp cString[esi],0h
		jne L2

; Print the decrypted string
	call Crlf
	mov edx,OFFSET prompt3
	call WriteString
	mov edx,OFFSET oString
	call WriteString


	exit
main ENDP
END main



