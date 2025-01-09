"""
Прямоугольная матрица размером до 9х9, символы разделены пробелом. Найти максимальную непрерывную горизонтальную последовательность из символов #.
Потом в конец добавить строку, в которой пишется количество # для каждого столбца, который содержит решётку из найденной последовательности.
Если в столбце не содержится решётка из последовательности, то на этом месте в строке пишется 0.
Затем отсортировать столбцы по этой добавленной строке в порядке убывания.

Пример:
0 # 6 #
# 7 # #
2 # # #
1 3 8 #
———
0 # 6 #
# 7 # #
2 # # #
1 3 8 #
0 2 2 4
"""

matrix = [
    ["0", "#", "6", "#"],
    ["#", "7", "#", "#"],
    ["2", "#", "#", "#"],
    ["1", "3", "8", "#"],
]

max_sequence_length = 0
max_sequence_row = -1

for i, row in enumerate(matrix):
    current_length = 0
    for cell in row:
        if cell == "#":
            current_length += 1
            if current_length > max_sequence_length:
                max_sequence_length = current_length
                max_sequence_row = i
        else:
            current_length = 0

appended_str = [0] * len(matrix[0])
if max_sequence_row != -1:
    for j in range(len(matrix[0])):
        if matrix[max_sequence_row][j] == "#":
            for i in range(len(matrix)):
                if matrix[i][j] == "#":
                    appended_str[j] += 1

matrix.append(appended_str)
for row in matrix:
    print(" ".join(map(str, row)))

sorted_matrix = list(zip(*matrix))
sorted_matrix.sort(key=lambda x: x[-1], reverse=True)
sorted_matrix = list(zip(*sorted_matrix))

for row in sorted_matrix:
    print(" ".join(map(str, row)))
