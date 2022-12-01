m = []
s = 0
with open("input.txt") as f:
    lines = f.readlines()
    for l in lines:
        if l == "" or l == "\n":
            m.append(s)
            s = 0
        else:
            s += int(l)
print(sum(sorted(m, reverse=True)[:3]))