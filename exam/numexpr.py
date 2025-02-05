def evaluate(expression: str) -> int:
    total = 0
    num = ""
    sign = 1

    for char in expression + "+":
        if char.isdigit():
            num += char
        else:
            if num:
                total += sign * int(num)
                num = ""
            sign = 1 if char == "+" else -1
    return total


def min_sub(expression: str) -> int:
    numbers = []
    num = ""
    signs = []

    for char in expression + "+":
        if char.isdigit():
            num += char
        else:
            if num:
                numbers.append(int(num))
                num = ""
            signs.append(char)
    total = numbers[0]
    for i in range(1, len(numbers)):
        if signs[i] == "-":
            total -= numbers[i]
        else:
            total += numbers[i]
    if total >= 0:
        return 0
    subtractions = sorted(
        [numbers[i] for i in range(1, len(numbers)) if signs[i] == "-"], reverse=True
    )
    count = 0
    for num in subtractions:
        total += num
        count += 1
        if total >= 0:
            break
    return count


def solve(input_file: str, output_file: str, output_file2: str):
    expressions = []
    results = {}

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            line = line.strip()
            if not line:
                continue
            result = evaluate(line)
            results[line] = result
            expressions.append(line)
            outfile.write(f"{line}={result}\n")

    expressions.sort(key=lambda x: results[x])
    with open(output_file2, "w") as outfile2:
        for expr in expressions:
            min_removals = min_sub(expr)
            outfile2.write(f"{expr} {min_removals}\n")


solve("in.txt", "out.txt", "out2.txt")
