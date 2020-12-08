import sys

content = []
with open('input.txt') as f:
    content = f.readlines()

def get_instr(idx: int):
    if idx >= len(content):
        raise Exception("Out of bounds {}".format(idx))

    try:
        line = content[idx].split(" ")
    except:
        print("###***Failing at {}***###".format(idx))
        raise
    return line[0], int(line[1])

# Execute the emulator

def exec_inst(curr_inst, acc, swp_idx):

    inst, input = get_instr(curr_inst)
    # print("Executing instruction {} {}, looking for swap {}".format(inst, input, swp_idx))

    if curr_inst == swp_idx:
        if inst == 'nop':
            inst = 'jmp'
        elif inst == 'jmp':
            inst = 'nop'

    if inst == "nop":
        return curr_inst + 1, acc
    elif inst == "acc":
        acc += input
        return curr_inst + 1, acc
    elif inst == "jmp":
        return curr_inst + input, acc
    else:
        raise Exception("Unknown instruction at", curr_inst)


def find_swp(instruction_set, search_start):
    for i in range(search_start, -1, -1):
        cmd, input = get_instr(i)
        if cmd == "nop" or cmd == 'jmp':
            print("Found a potential swap {} - {} at {}".format(cmd, input, i))
            try:
                acc = run_swp_nop_jmp(i)
                print("Finished execution. Accumlator value:", acc)
                sys.exit()

            except Exception as ex:
                print(ex)
                continue

def run_swp_nop_jmp(swp_idx: int):
    print("Swapping idx {}".format(swp_idx))
    acc = 0
    curr_inst = 0
    seen = [0 for _ in range(len(content))]

    while(True):
        if curr_inst >= len(content):
            print("Execution terminated. Acc: {}".format(acc))
            return acc

        # Cycle detection
        if seen[curr_inst] != 0:
            raise Exception(
                "Swap at {} not-accepted. Cycle at {}".format(swp_idx, curr_inst))

        seen[curr_inst] = 1
        curr_inst, acc = exec_inst(curr_inst, acc, swp_idx)


def start():
    curr_inst = 0
    acc = 0
    seen = [0 for _ in range(len(content))]
    instructions = []

    # Detect the first cycle
    while(True):
        if seen[curr_inst] != 0:
            find_swp(instructions, len(instructions) - 1)

        instructions.append(curr_inst)

        seen[curr_inst] = 1

        curr_inst, acc = exec_inst(curr_inst, acc, -1)

start()
