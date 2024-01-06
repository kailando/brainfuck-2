from sys import argv
codeChars, mem_size, mem, pointer, ram, ptr, stack=[">", "<", "-", "+", "^", ".", ",", "[", "]", "#", "!"], 8, [0] * 8, 0, 0, 0, []
try: code=''.join(char for char in open(argv[1]).read() if char in codeChars)
except IndexError: code=''.join(char for char in input("Brainf**k V.2 code:\n") if char in codeChars)
while ptr<len(code):
    char, ptr=code[ptr], ptr+1
    if char==codeChars[0]: pointer+=1
    elif char==codeChars[1]: pointer-=1
    elif char==codeChars[2]: ram-=1
    elif char==codeChars[3]: ram+=1
    elif char==codeChars[4]: mem[pointer]=ram
    elif char==codeChars[5]: ram=mem[pointer]
    elif char==codeChars[6]: print(chr(mem[pointer]), end="")
    elif char==codeChars[7]:
        if mem[pointer]==0:
            stack.append(ptr)
            while stack:
                ptr+=(code[ptr]=="[")-(code[ptr]=="]")
                stack.append(ptr) if code[ptr]=="[" else stack.pop()
    elif char==codeChars[8]:
            ((ptr:=stack[-1]) if mem[pointer]!=0 else (stack.pop()))
        else:
            stack.pop()
    elif char==codeChars[9]: ram=min(255, max(0, int(input("0-255: "))))
    elif char==codeChars[10]: exit()
    mem_size, pointer, ram, mem, ram=mem_size+pointer>=mem_size, max(pointer, 0), max(0, min(255, ram)), [min(255, m) for m in mem], min(255, max(0, ram))