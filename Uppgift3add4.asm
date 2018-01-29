TITLE Add and Subtract, Version 2
; This program adds and subtracts 32-bit unsigned
; integers and stores the sum in a variable.

INCLUDE Irvine32.inc
.data
val1 DWORD 10000h
val2 DWORD 20000h
val3 DWORD 30000h
val4 DWORD 40000h
finalVal DWORD ?

.code
main PROC
	mov eax, 10000h
	add eax, val1
	add eax, val2
	add eax, val3
	add eax, val4
	call WriteDec ; Skriver ut B0000h som 720896
	exit
main ENDP
END main
