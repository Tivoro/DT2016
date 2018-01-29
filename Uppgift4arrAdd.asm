TITLE ArrAdd
; This program combines two arrays into a third by using indirect addressing

INCLUDE Irvine32.inc
.data
arr1 BYTE 10h,20h,30h
arr2 BYTE 40h,50h,60h
arr3 BYTE 0h,0h,0h

.code
main PROC
; Get the offsets for the arrays
	mov ebx,OFFSET arr1
	mov ecx,OFFSET arr2
	mov edx,OFFSET arr3

; Get and add the values
	mov al,[ebx]
	add al,[ecx]
	mov [edx],al
	inc ebx
	inc ecx
	inc edx
	mov al,[ebx]
	add al,[ecx]
	mov [edx],al
	inc ebx
	inc ecx
	inc edx
	mov al,[ebx]
	add al,[ecx]
	mov [edx],al
	inc ebx
	inc ecx
	inc edx

; Dump the array
	mov esi,OFFSET arr3
	mov ecx,LENGTHOF arr3
	mov ebx,TYPE arr3
	call DumpMem

	exit
main ENDP
END main


