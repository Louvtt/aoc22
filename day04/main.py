ENTRY_FILE = "input.txt"

def get_file_contents():
    lines = []
    with open(ENTRY_FILE, "r") as f:
        lines = f.readlines()
    return lines

# Part 1
def full_overlap_test(range0, range1):
    min0, max0 = range0
    min1, max1 = range1
    if min0 <= min1 and max1 <= max0:
        return True # first overlap second
    if min1 <= min0 and max0 <= max1:
        return True # second overlap first
    return False

# Part 2
def overlap_test(range0, range1):
    min0, max0 = range0
    min1, max1 = range1
    # |------|
    #    |-----|
    if min0 <= max1 and max0 >= min1:
        return True
    if min1 <= max0 and max1 >= min0:
        return True
    return False

def main():
    lines = get_file_contents()

    overlaps = 0
    for line in lines:
        range0, range1 = line.split(",")
        # get min and max
        range0 = [int(e) for e in range0.split("-")]
        range1 = [int(e) for e in range1.split("-")]

        # check
        if overlap_test(range0, range1):
            # print(f"Overlap {range0} and {range1}")
            overlaps+=1
    return overlaps

if __name__ == "__main__":
    res = main()
    print(res)