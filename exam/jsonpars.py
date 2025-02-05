from collections import defaultdict

stack = []
max_depth = defaultdict(int)
tag_counts = defaultdict(int)
cur_depth = 0

with open("in.txt", "r", encoding="utf-8") as inf:
    for line in inf:
        i = 0
        while i < len(line):
            if line[i] == '"':
                j = i + 1
                while j < len(line) and line[j] != '"':
                    j += 1
                if j < len(line):
                    tag = line[i + 1 : j]
                    stack.append(tag)
                    tag_counts[tag] += 1
                    max_depth[tag] = max(max_depth[tag], cur_depth)
                i = j + 1
            else:
                if line[i] == "{":
                    cur_depth += 1
                elif line[i] == "}":
                    cur_depth -= 1
                i += 1

with open("out1.txt", "w", encoding="utf-8") as outf:
    for key in tag_counts.keys():
        c = tag_counts[key]
        d = max_depth[key]
        res = key + " " + str(c) + " " + str(d)
        outf.write(res + "\n")

with open("out2.txt", "w", encoding="utf-8") as outf:
    for key in sorted(tag_counts.keys(), reverse=True):
        c = tag_counts[key]
        d = max_depth[key]
        res = key + " " + str(c) + " " + str(d)
        outf.write(res + "\n")
