import re
registers, program = "".join(open("big.txt").readlines()).split("\n\n")
A, B, C = [int(re.findall(r"\d+", item)[0]) for item in registers.split("\n")]
program = list(map(int, re.findall(r"\d+", program)))

def single_step(a):
    b = a % 8
    b = b ^ 1
    c = a >> b
    a = a >> 3
    b = b ^ c
    b = b ^ 6
    return b % 8

def find(A, col=0):
    if single_step(A) != program[-(col+1)]:
        return
    if col == len(program) -1:
        As.append(A)
    else:
        for B in range(8):
            find(A*8+B, col+1)

As = []
for a in range(8):
    find(a)
print(As[0])