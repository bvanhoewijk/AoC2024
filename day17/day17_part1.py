import re 

def part1(program, A, B, C):
    pointer = 0
    output = []
    while pointer+1 < len(program):
        opcode, operand = program[pointer], program[pointer+1]

        # Should be impossible
        combo = None

        # Get combo value:
        if operand <= 3: 
            combo = operand
        elif operand == 4: 
            combo = A
        elif operand == 5: 
            combo = B
        elif operand == 6: 
            combo = C

        if opcode == 0:
            A = A // 2**combo
        if opcode == 1:
            B = B ^ operand
        if opcode == 2:
            B = combo % 8
        if opcode == 3:
            if A != 0:
                pointer = operand
                continue
        if opcode == 4:
            B = B ^ C
        if opcode == 5:
            output.append(combo % 8)
        if opcode == 6:
            B = A // 2**combo
        if opcode == 7:
            C = A // 2**combo

        pointer += 2

    print("Registers:", A, B, C)
    print("Out", ",".join(map(str, output)))


registers, program = "".join(open("big.txt").readlines()).split("\n\n")
A, B, C = [int(re.findall(r"\d+", item)[0]) for item in registers.split("\n")]
program = list(map(int, re.findall(r"\d+", program)))
part1(program, A, B, C)