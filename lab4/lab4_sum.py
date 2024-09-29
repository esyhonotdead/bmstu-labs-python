from prettytable import PrettyTable 

def sum_series(x, epsilon, step):
    # Инициализация переменных
    n = 1  
    sum_result = 1  
    term = 1 / (n ** x)
    my_Table = PrettyTable(["# Итерации", "t", "y"])
    my_Table.add_row([n, round(term, 3), round(sum_result, 3)])
     

    # Пока текущий член больше или равен epsilon, продолжаем добавлять члены
    while abs(term) >= epsilon:
        n += 1  
        term = 1 / (n ** x)  
        sum_result += term
        my_Table.add_row([n, round(term, 3), round(sum_result, 3)])
    print(my_Table)
    


# Ввод данных:
x = int(input("Введите степень ряда: ")) 
step = int(input("введите шаг печати: "))  # TODO
epsilon = float(input("Введите точность: ")) 
sum_series(x, epsilon, step)    