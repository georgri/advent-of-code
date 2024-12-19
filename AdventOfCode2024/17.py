text = """
Register A: 22817223
Register B: 0
Register C: 0

Program: 2,4,1,2,7,5,4,5,0,3,1,7,5,5,3,0
"""

text_test = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
"""

text_test2 = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
"""

def read_input(text):
    regs, program = [0,0,0], []
    for line in text.split('\n'):
        if not line:
            continue

        if 'Register' in line:
            reg, val = line.split(': ')
            _, reg = reg.split()
            regs[ord('A') - ord(reg)] = int(val)

        else:
            _, vals = line.split(': ')
            program = list(map(int, vals.split(',')))

    return regs, program

print(read_input(text_test))

def combo(regs, val):
    if val < 4:
        return val
    return regs[val-4]

def execute(regs, program, ip, output):
    if ip >= len(program) - 1:
        return ip + 2 # halt
    
    command, arg = program[ip], program[ip + 1]
    
    if command == 0: # adv
        regs[0] = regs[0] >> combo(regs, arg)
    elif command == 1: # bxl
        regs[1] ^= arg
    elif command == 2: # bst
        regs[1] = combo(regs, arg) % 8
    elif command == 3: # jnz
        if regs[0] != 0:
            # perform jump
            return arg
    elif command == 4: # bxc
        regs[1] ^= regs[2]
    elif command == 5: # out
        output.append(combo(regs, arg) % 8)
    elif command == 6: # bdv
        regs[1] = regs[0] >> combo(regs, arg)
    else:
        regs[2] = regs[0] >> combo(regs, arg)

    return ip + 2


def run(regs, program):
    output = []

    ip = 0
    regs = regs[:]
    while ip < len(program):
        ip = execute(regs, program, ip, output)

    return ','.join(map(str,output))


def solve(text):
    regs, program = read_input(text)
    return run(regs, program)

print(solve(text))


def solve2(text):
    regs, program = read_input(text)
    
    target = ','.join(map(str,program))
    
    for i in range(1_000):
        regs[0] = i
        res = run(regs, program)
        if target == res:
            return i
    return -1


# print(solve2(text_test2))

"""
reverse program: 
2,4, # bst 4 => B = A % 8         # get last 3 binary digits of A into B
1,2, # bxl 2 => B = B xor 2       # B xor 2
7,5, # cdv 5 => C = A // (2 ** B) # C = A >> B
4,5, # bxc 5 => B = B xor C       # B xor C
1,7, # bxl 7 => B = B xor 7       # B xor 7
0,3, # adv 3 => A = A // 8        # get rid of 3 last binary digits of A
5,5, # out 5 => output(B % 8)     # output last 3 binary digits of B
3,0 # jnz 0
"""
def solve3(text):
    regs, program = read_input(text)
    
    target = ','.join(map(str,program))
    
    cur_res = 0
    for i in range(len(program)):
        target = ','.join(map(str, program[-i-1:]))
        for j in range(8):
            regs[0] = (cur_res << 3) + j
        
            res = run(regs, program)
            # print(res)
            if target == res:
                cur_res = (cur_res << 3) + j
                break
    return cur_res

print(solve3(text))
