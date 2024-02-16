#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("300x400")
        self.root.configure(bg="#f0f0f0")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="To-Do List", bg="#3498DB", fg="white", font=("Arial", 16))
        self.label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, bg="white", font=("Arial", 12))
        self.task_entry.pack(pady=5, padx=20, ipady=5, fill=tk.X)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#2ECC71", fg="white", font=("Arial", 12))
        self.add_button.pack(pady=5, padx=20, ipady=5, fill=tk.X)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, bg="#E74C3C", fg="white", font=("Arial", 12))
        self.remove_button.pack(pady=5, padx=20, ipady=5, fill=tk.X)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="#3498DB", fg="white", font=("Arial", 12))
        self.update_button.pack(pady=5, padx=20, ipady=5, fill=tk.X)

        self.task_listbox = tk.Listbox(self.root, bg="white", font=("Arial", 12))
        self.task_listbox.pack(pady=10, padx=20, ipady=5, fill=tk.BOTH, expand=True)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            task = self.task_listbox.get(task_index)
            self.tasks.remove(task)
            self.task_listbox.delete(task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[task_index] = updated_task
                self.task_listbox.delete(task_index)
                self.task_listbox.insert(task_index, updated_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

