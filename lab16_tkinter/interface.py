import tkinter as tk
from tkinter import messagebox
from logic import binary_to_decimal, decimal_to_binary


def insert_text(entry, value):
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "Enter":
        pass  # Можно добавить обработку ввода
    else:
        entry.insert(tk.END, value)


def open_keyboard(entry):
    keyboard_window = tk.Toplevel()
    keyboard_window.title("Экранная клавиатура")

    buttons = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "C", "Enter"]

    for i, btn in enumerate(buttons):
        tk.Button(
            keyboard_window,
            text=btn,
            width=5,
            height=2,
            command=lambda b=btn: insert_text(entry, b),
        ).grid(row=i // 4, column=i % 4)


def convert():
    try:
        input_text = entry.get().strip()
        if not input_text:
            return

        if input_mode.get() == "10 to 2":
            result = decimal_to_binary(float(input_text))
        else:
            result = binary_to_decimal(input_text)

        output_field.config(state="normal")
        output_field.delete(0, tk.END)
        output_field.insert(0, str(result))
        output_field.config(state="readonly")
    except ValueError:
        messagebox.showerror("Ошибка", "Некорректный ввод. Проверьте данные.")


def clear_input():
    entry.delete(0, tk.END)


def clear_output():
    output_field.config(state="normal")
    output_field.delete(0, tk.END)
    output_field.config(state="readonly")


def show_info():
    messagebox.showinfo("О программе", "Конвертер чисел. Сделал никикита))")


root = tk.Tk()
root.title("Конвертер чисел")
input_mode = tk.StringVar(value="10 to 2")

menu = tk.Menu(root)
root.config(menu=menu)
menu.add_command(label="О программе", command=show_info)

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Введите число:").grid(row=0, column=0)
entry = tk.Entry(frame)
entry.grid(row=0, column=1)

tk.Label(frame, text="Результат:").grid(row=1, column=0)
output_field = tk.Entry(frame, state="readonly")
output_field.grid(row=1, column=1)

convert_button = tk.Button(frame, text="Конвертировать", command=convert)
convert_button.grid(row=2, column=1)

tk.Button(frame, text="Очистить ввод", command=clear_input).grid(row=3, column=0)
tk.Button(frame, text="Очистить вывод", command=clear_output).grid(row=3, column=1)

tk.Radiobutton(
    frame, text="Десятичная → Двоичная", variable=input_mode, value="10 to 2"
).grid(row=4, column=0)
tk.Radiobutton(
    frame, text="Двоичная → Десятичная", variable=input_mode, value="2 to 10"
).grid(row=4, column=1)

keyboard_button = tk.Button(
    root, text="Открыть клавиатуру", command=lambda: open_keyboard(entry)
)
keyboard_button.pack()

root.mainloop()
