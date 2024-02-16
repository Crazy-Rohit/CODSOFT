#!/usr/bin/env python
# coding: utf-8

# In[12]:


import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import random

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        self.contact_manager = ContactManager()

        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", foreground="black", background="lightblue", font=("Arial", 10))

        tk.Label(self.root, text="Contact Book", font=("Arial", 20, "bold"), bg="#3498DB", fg="white").pack(fill=tk.X, pady=10)

        tk.Label(self.root, text="Name:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        tk.Entry(self.root, textvariable=self.name_var, width=30).pack(fill=tk.X, padx=20, pady=5)

        tk.Label(self.root, text="Phone:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        tk.Entry(self.root, textvariable=self.phone_var, width=30).pack(fill=tk.X, padx=20, pady=5)

        tk.Label(self.root, text="Email:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        tk.Entry(self.root, textvariable=self.email_var, width=30).pack(fill=tk.X, padx=20, pady=5)

        tk.Label(self.root, text="Address:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        tk.Entry(self.root, textvariable=self.address_var, width=30).pack(fill=tk.X, padx=20, pady=5)

        ttk.Button(self.root, text="Add Contact", command=self.add_contact, style="TButton").pack(fill=tk.X, padx=20, pady=10)
        ttk.Button(self.root, text="View Contact List", command=self.view_contact_list, style="TButton").pack(fill=tk.X, padx=20, pady=5)
        ttk.Button(self.root, text="Search Contact", command=self.search_contact, style="TButton").pack(fill=tk.X, padx=20, pady=5)
        ttk.Button(self.root, text="Update Contact", command=self.update_contact, style="TButton").pack(fill=tk.X, padx=20, pady=5)
        ttk.Button(self.root, text="Delete Contact", command=self.delete_contact, style="TButton").pack(fill=tk.X, padx=20, pady=5)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        contact = Contact(name, phone, email, address)
        self.contact_manager.add_contact(contact)
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contact_list(self):
        contact_list = "\n".join(f"{contact.name}: {contact.phone}" for contact in self.contact_manager.contacts)
        messagebox.showinfo("Contact List", contact_list)

    def search_contact(self):
        keyword = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if keyword:
            results = self.contact_manager.search_contact(keyword)
            if results:
                contact_list = "\n".join(f"{contact.name}: {contact.phone}" for contact in results)
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No contacts found.")

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter name to update:")
        if name:
            for contact in self.contact_manager.contacts:
                if contact.name.lower() == name.lower():
                    contact.phone = self.phone_var.get()
                    contact.email = self.email_var.get()
                    contact.address = self.address_var.get()
                    messagebox.showinfo("Success", "Contact updated successfully.")
                    return
            messagebox.showinfo("Error", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter name to delete:")
        if name:
            for contact in self.contact_manager.contacts:
                if contact.name.lower() == name.lower():
                    self.contact_manager.delete_contact(contact)
                    messagebox.showinfo("Success", "Contact deleted successfully.")
                    return
            messagebox.showinfo("Error", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()


# In[ ]:




