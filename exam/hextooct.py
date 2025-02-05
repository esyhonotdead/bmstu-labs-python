def hex_to_oct(n):
    res = ""
    if n.startswith("+") or n.startswith("-"):
        res += n[0]
        n = n[1:]

    return res + oct(int(n, 16))[2:]


current_sentence = ""
current_num = ""
result = []
with open("in.txt", "r", encoding="utf-8") as infile:
    for line in infile:
        line = line.strip("\n")
        for symbol in line:
            if symbol == ".":
                result.append(current_sentence)
                current_sentence = ""
            elif symbol == "+" or symbol == "-":
                current_num += symbol
            elif current_num and (
                symbol.isdigit() or symbol == "x" or symbol in "ABCDEF"
            ):
                current_num += symbol
            elif symbol == " ":
                if current_num:
                    n = hex_to_oct(current_num)
                    current_sentence += str(n)
                    current_num = ""
                current_sentence += " "
            else:
                current_sentence += symbol

with open("out.txt", "w", encoding="utf-8") as outfile:
    for line in result:
        outfile.write(str(line) + "\n")
