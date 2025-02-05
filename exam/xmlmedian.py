def process_line(line, stack, dict_stack, values):
    tokens = line.replace("<", " ").replace(">", " ").split()
    for token in tokens:
        if token.startswith("/"):
            stack.pop()
            dict_stack.pop()
        elif token.isdigit():
            values.append(int(token))
            dict_stack[-1][stack[-1]] = int(token)
        else:
            new_dict = {}
            dict_stack[-1][token] = new_dict
            stack.append(token)
            dict_stack.append(new_dict)


def calculate_median(values):
    values.sort()
    mid = len(values) // 2
    if len(values) % 2 == 0:
        return (values[mid] + values[mid - 1]) // 2
    return values[mid]


def process_file(in_file, out_file):
    stack = []
    values = []
    dict_stack = [{}]

    with open(in_file, "r") as infile:
        for line in infile:
            process_line(line, stack, dict_stack, values)

    dict_stack[0]["median"] = calculate_median(values)

    with open(out_file, "w") as outfile:
        outfile.write(str(dict_stack[0]))


def main():
    in_file = "in.txt"
    out_file = "out.txt"
    process_file(in_file, out_file)


if __name__ == "__main__":
    main()
