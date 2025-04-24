import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry widget for displaying expressions
        input_frame = tk.Frame(self.root)
        input_frame.pack()

        input_field = tk.Entry(input_frame, textvariable=self.input_text, font=("Arial", 18), justify="right")
        input_field.grid(row=0, column=0, ipady=10, ipadx=10)

        # Buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack()

        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create buttons dynamically
        for (text, row, col) in buttons:
            if text == "=":
                button = tk.Button(buttons_frame, text=text, font=("Arial", 14), command=self.calculate_result)
            elif text == "C":
                button = tk.Button(buttons_frame, text=text, font=("Arial", 14), command=self.clear_input)
            else:
                button = tk.Button(buttons_frame, text=text, font=("Arial", 14), command=lambda t=text: self.append_to_expression(t))
            button.grid(row=row, column=col, ipadx=15, ipady=10, padx=5, pady=5)

    def append_to_expression(self, char):
        self.expression += str(char)
        self.input_text.set(self.expression)

    def clear_input(self):
        self.expression = ""
        self.input_text.set(self.expression)

    def calculate_result(self):
        try:
            result = eval(self.expression)  # Evaluate the expression
            self.input_text.set(result)
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
            self.clear_input()


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()