from collections import defaultdict


def process_file(in_file, out_file):
    stack = []
    tag_counts = defaultdict(int)
    max_depth = defaultdict(int)
    current_depth = 0

    with open(in_file, "r", encoding="utf-8") as infile:
        for line in infile:
            i = 0
            while i < len(line):
                if line[i] == "<":
                    j = i + 1
                    while j < len(line) and line[j] != ">":
                        j += 1
                    if j < len(line):
                        tag = line[i + 1 : j]
                        if tag.startswith("/"):
                            stack.pop()
                            current_depth -= 1
                        else:
                            stack.append(tag)
                            tag_counts[tag] += 1
                            current_depth += 1
                            max_depth[tag] = max(max_depth[tag], current_depth)
                    i = j + 1
                else:
                    i += 1

    with open(out_file, "w", encoding="utf-8") as outfile:
        for tag in sorted(tag_counts.keys(), reverse=True):
            outfile.write(f"{tag} {tag_counts[tag]} {max_depth[tag]}\n")


def main():
    in_file = "in.txt"
    out_file = "out.txt"
    process_file(in_file, out_file)


if __name__ == "__main__":
    main()
