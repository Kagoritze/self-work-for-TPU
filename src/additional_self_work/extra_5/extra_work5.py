"""
Создать приложение, осуществляющее математические операции сложения, вычитания и произведения над матрицами.
"""

import tkinter as tk
from tkinter import messagebox

import numpy as np


class MatrixApp:
    def __init__(self, master):
        self.master = master
        master.title("Операции с матрицами")

        self.label1 = tk.Label(master, text="Matrix A:")
        self.label1.grid(row=0, column=0, padx=10, pady=10)

        self.matrix_a_text = tk.Text(master, height=5, width=30)
        self.matrix_a_text.grid(row=1, column=0, padx=10, pady=10)

        self.label2 = tk.Label(master, text="Matrix B:")
        self.label2.grid(row=0, column=1, padx=10, pady=10)

        self.matrix_b_text = tk.Text(master, height=5, width=30)
        self.matrix_b_text.grid(row=1, column=1, padx=10, pady=10)

        self.add_button = tk.Button(master, text="Add", command=self.add_matrices)
        self.add_button.grid(row=2, column=0, padx=10, pady=10)

        self.subtract_button = tk.Button(
            master, text="Subtract", command=self.subtract_matrices
        )
        self.subtract_button.grid(row=2, column=1, padx=10, pady=10)

        self.multiply_button = tk.Button(
            master, text="Multiply", command=self.multiply_matrices
        )
        self.multiply_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(master, text="Result:")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.result_text = tk.Text(master, height=5, width=60)
        self.result_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def get_matrix(self, text_widget):
        try:
            matrix = []
            lines = text_widget.get("1.0", tk.END).strip().split("\n")
            for line in lines:
                row = list(map(float, line.split()))
                matrix.append(row)
            return np.array(matrix)
        except Exception as e:
            messagebox.showerror(
                "Input Error",
                "Invalid matrix input. Please ensure you enter numeric values.",
            )
            return None

    def add_matrices(self):
        mat_a = self.get_matrix(self.matrix_a_text)
        mat_b = self.get_matrix(self.matrix_b_text)
        if mat_a is not None and mat_b is not None:
            if mat_a.shape == mat_b.shape:
                result = mat_a + mat_b
                self.display_result(result)
            else:
                messagebox.showerror(
                    "Error", "Matrices must have the same dimensions for addition."
                )

    def subtract_matrices(self):
        mat_a = self.get_matrix(self.matrix_a_text)
        mat_b = self.get_matrix(self.matrix_b_text)
        if mat_a is not None and mat_b is not None:
            if mat_a.shape == mat_b.shape:
                result = mat_a - mat_b
                self.display_result(result)
            else:
                messagebox.showerror(
                    "Error", "Matrices must have the same dimensions for subtraction."
                )

    def multiply_matrices(self):
        mat_a = self.get_matrix(self.matrix_a_text)
        mat_b = self.get_matrix(self.matrix_b_text)
        if mat_a is not None and mat_b is not None:
            if mat_a.shape[1] == mat_b.shape[0]:
                result = np.dot(mat_a, mat_b)
                self.display_result(result)
            else:
                messagebox.showerror(
                    "Error",
                    "Number of columns in Matrix A must equal number of rows in Matrix B for multiplication.",
                )

    def display_result(self, result):
        self.result_text.delete("1.0", tk.END)
        for row in result:
            self.result_text.insert(tk.END, " ".join(map(str, row)) + "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()
