import tkinter as tk
from tkinter import messagebox
import random


class PasswordGenerator:
    def __init__(self, window):
        self.window = window
        self.window.title("Emmanuel Password Generator")

        self.title_label = tk.Label(window, text="Welcome to the Emmanuel Password Generator!")
        self.title_label.pack(pady=10)

        self.letters_label = tk.Label(window, text="How many letters would you like?")
        self.letters_label.pack()
        self.letters_entry = tk.Entry(window)
        self.letters_entry.pack()

        self.symbols_label = tk.Label(window, text="How many symbols would you like?")
        self.symbols_label.pack()
        self.symbols_entry = tk.Entry(window)
        self.symbols_entry.pack()

        self.numbers_label = tk.Label(window, text="How many numbers would you like?")
        self.numbers_label.pack()
        self.numbers_entry = tk.Entry(window)
        self.numbers_entry.pack()

        self.generate_button = tk.Button(window, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(window, text="Your generated password is: ")
        self.password_label.pack(pady=10)

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                   'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '(', ')']

        try:
            nr_letters = int(self.letters_entry.get())
            nr_symbols = int(self.symbols_entry.get())
            nr_numbers = int(self.numbers_entry.get())

            password_list = []
            for i in range(nr_letters):
                password_list.append(random.choice(letters))

            for j in range(nr_symbols):
                password_list.append(random.choice(symbols))

            for k in range(nr_numbers):
                password_list.append(random.choice(numbers))

            random.shuffle(password_list)
            password = ''.join(password_list)

            self.password_label.config(text=f"Your generated password is: {password}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers!")


def main():
    window = tk.Tk()
    PasswordGenerator(window)
    window.mainloop()


main()
