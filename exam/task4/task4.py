import string

with open("./in.txt", "r", encoding="UTF-8") as inf:
    max_line_len = 0
    for line in inf:
        line = line.rstrip()
        max_line_len = max(max_line_len, len(line))
    
print(max_line_len)
