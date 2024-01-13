from sys import argv
mem_size, mem, pointer, ram, ptr, stack=8, [0]*8, 0, 0, 0, []
try: code=''.join(char for char in open(argv[1]).read() if char in "><-+^.,[]#!*")
except IndexError: code=''.join(char for char in list(input("Brainf**k V.2 code:\n")) if char in "><-+^.,[]#!*")
while ptr<len(code):
    char, ptr=code[ptr], ptr+1
    match char:
        case "><-+^.,[]#!*"[0]: pointer+=1
        case "><-+^.,[]#!*"[1]: pointer-=1
        case "><-+^.,[]#!*"[2]: ram-=1
        case "><-+^.,[]#!*"[3]: ram+=1
        case "><-+^.,[]#!*"[4]: mem[pointer]=ram
        case "><-+^.,[]#!*"[5]: ram=mem[pointer]
        case "><-+^.,[]#!*"[6]: print(chr(mem[pointer]), end="")
        case "><-+^.,[]#!*"[7]:
            if mem[pointer]==0:
                stack.append(ptr)
                while stack:
                    ptr+=(code[ptr]=="[")-(code[ptr]=="]")
                    stack.append(ptr) if code[ptr]=="[" else stack.pop()
        case "><-+^.,[]#!*"[8]:
                ((ptr:=stack[-1]) if mem[pointer]!=0 else (stack.pop()))
            else:
                stack.pop()
        case "><-+^.,[]#!*"[9]: ram=min(255, max(0, int(input("0-255: "))))
        case "><-+^.,[]#!*"[10]: exit()
        case "><-+^.,[]#!*"[11]: print("", end="")
    mem_size, pointer, ram, mem, ram=mem_size+pointer>=mem_size, max(pointer, 0), max(0, min(255, ram)), [min(255, m) for m in mem], min(255, max(0, ram))