TITLE ArrAdd version 2
; This program combines two arrays into a third by using indirect addressing

INCLUDE Irvine32.inc

.data
arr1 WORD 1000h,2000h,3000h
arr2 WORD 4000h,5000h,6000h
arr3 WORD 0h,0h,0h

.code
MAIN PROC
; Get array values and insert into 3rd array
	mov esi,0
	mov ax,arr1[esi]
	add ax,arr2[esi]
	mov arr3[esi],ax
	add esi,2
	mov ax,arr1[esi]
	add ax,arr2[esi]
	mov arr3[esi],ax
	add esi,2
	mov ax,arr1[esi]
	add ax,arr2[esi]
	mov arr3[esi],ax

; Dump third array
	mov esi,OFFSET arr3
	mov ecx,LENGTHOF arr3
	mov ebx,TYPE arr3
	call DumpMem

	exit
main ENDP
END main


