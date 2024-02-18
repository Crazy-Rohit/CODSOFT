#!/usr/bin/env python
# coding: utf-8

# In[8]:


import tkinter as tk

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())

        if operation == "+":
            result = num1 + num2
            operation_str = " + "
        elif operation == "-":
            result = num1 - num2
            operation_str = " - "
        elif operation == "x":
            result = num1 * num2
            operation_str = " × "
        elif operation == "/":
            if num2 == 0:
                result = "Cannot divide by zero!"
                operation_str = ""
            else:
                result = num1 / num2
                operation_str = " ÷ "
        elif operation == "^":
            result = num1 ** num2
            operation_str = " ^ "
        elif operation == "√":
            result = num1 ** (1/num2)
            operation_str = " √ "
        elif operation == "%":
            result = num1 % num2
            operation_str = " % "
        elif operation == "C":
            entry_num1.delete(0, tk.END)
            entry_num2.delete(0, tk.END)
            result_label.config(text="")
            return
        else:
            result = "Invalid operation"
            operation_str = ""

        result_label.config(text=f"Result :{num1}{operation_str}{num2} = {result}")
    except ValueError:
        result_label.config(text="Invalid input")

def clear_entries():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    result_label.config(text="")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Change background color to light blue
root.configure(bg="#ADD8E6")

# Add white color border/frame
frame = tk.Frame(root, bg="white", bd=5)
frame.grid(row=0, column=0, padx=10, pady=10)

# Number 1 Entry
label_num1 = tk.Label(frame, text="Enter first number:", bg="white", fg="black", font=("Arial", 16))
label_num1.grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_num1 = tk.Entry(frame, font=("Arial", 16))
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# Number 2 Entry
label_num2 = tk.Label(frame, text="Enter second number:", bg="white", fg="black", font=("Arial", 16))
label_num2.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_num2 = tk.Entry(frame, font=("Arial", 16))
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Operation Buttons
operations = ["+", "-", "x", "/", "^", "√", "%", "C"]
row_num = 2
column_num = 0
for operation in operations:
    button = tk.Button(frame, text=operation, command=lambda op=operation: calculate(op), bg="pink", font=("Arial", 16))
    button.grid(row=row_num, column=column_num, padx=5, pady=5, sticky="nsew")
    column_num += 1
    if column_num > 1:
        column_num = 0
        row_num += 1

# Clear Button
clear_button = tk.Button(frame, text="Clear", command=clear_entries, bg="lightgreen", font=("Arial", 16))
clear_button.grid(row=row_num, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Result Label
result_label = tk.Label(frame, text="", bg="white", fg="black", font=("Arial", 16))
result_label.grid(row=row_num + 1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Center all contents
for widget in frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)
    widget.grid_configure(ipadx=10, ipady=10)

# Run the GUI
root.mainloop()


# In[ ]:




