from parse import parse

ENTRY_FILE = "input.txt"

def get_file_contents():
    lines = []
    with open(ENTRY_FILE, "r") as f:
        lines = f.readlines()
    return lines

def split_content(file_content, sep="\n"):
    content = [[], []]
    content_idx = 0
    # Find empty line
    for line in file_content:
        if line == sep:
            content_idx = 1
            continue # skip empty line
        content[content_idx].append(line.replace("\n", ""))
    return content

def parse_cargo_content(file_content):
    # create cargo stack
    cargo_count = len([i for i in file_content[-1].split(" ") if i != ""])
    cargo_stack = [[] for i in range(cargo_count)]

    # read each crate line
    for crate_line in file_content:
        for i in range(0, cargo_count):
            if crate_line[i*4] == '[':
                cargo_stack[i].insert(0, crate_line[i*4+1])

    return cargo_stack

# part 1
def process_crane_9000(instr, cargo):
    res = parse('move {} from {} to {}', instr)
    if res:
        count, src, dest = [int(value) for value in res]
        for i in range(count):
            crate = cargo[src-1].pop()
            cargo[dest-1].append(crate)
        print("Step: ", cargo)
    return cargo

# part 2
def process_crane_9001(instr, cargo):
    res = parse('move {} from {} to {}', instr)
    if res:
        count, src, dest = [int(value) for value in res]
        cargo[src-1], toadd = cargo[src-1][:-count], cargo[src-1][-count:]
        cargo[dest-1] = cargo[dest-1] + toadd
        print("Step: ", instr, ":", cargo)
    return cargo

def main():
    content = get_file_contents()
    cargo_content, instr_content = split_content(content, "\n")
    cargo = parse_cargo_content(cargo_content)

    top_letters = []
    for instr in instr_content:
        cargo = process_crane_9001(instr, cargo)
    
    top_letters = [cargo[i][-1] for i in range(len(cargo))]
    return "".join(top_letters)

if __name__ == "__main__":
    res = main()
    print(res)