ENTRY_FILE = "input.txt"

def get_file_contents():
    lines = []
    with open(ENTRY_FILE, "r") as f:
        lines = f.readlines()
    return lines

def main():
    pass

if __name__ == "__main__":
    res = main()
    print(res)