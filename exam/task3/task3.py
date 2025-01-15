with open("./out1.txt", "w") as out1f:
    with open("./in.txt", "r") as inf:
        max_line_len = 0
        for line in inf:
            line = line.strip().split()
            max_line_len = max(max_line_len, len(line))
            max_len_word = 0
            for word in line:
                max_len_word = max(max_len_word, len(word))
            for word in range(len(line)):
                line[word] = line[word] + " " * (max_len_word - len(line[word]))

            counter = 0
            for char in range(max_len_word):
                for word in line:
                    if word[char].isalpha():
                        counter += 1
                    out1f.write(word[char])
                out1f.write(f".{counter}\n")
                counter = 0

with open("./out2.txt", "w") as out2f:
    with open("./out1.txt", "r") as out1f:
        for i in range(max_line_len + 1):
            for line in out1f:
                line = line.rstrip()
                if line[-1] == str(i):
                    out2f.write(line + "\n")
            out1f.seek(0)
