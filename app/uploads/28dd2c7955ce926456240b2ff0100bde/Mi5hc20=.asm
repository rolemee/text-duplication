assume cs:code,ds:data
data segment
        db "Hello World";
data ends

code segment
        start:
        mov ax,data
        mov ds,ax;
        mov ax,0B800H
        mov es,ax;
        mov bx,0
        mov si,319
        
        
        mov cx,11
        s:
        mov ah,[bx]
        mov al,00000111b
        mov es:[si],ax
        add bx,1
        add si,2
        loop s;
        
        all:
        jmp all
        mov ax,4C00h
        int 21h
code ends
end start
