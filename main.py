# library_app.py

import tkinter as tk
from tkinter import messagebox
from model.book import Book  

class LibraryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.geometry("400x500")

        self.book_list = []

        # UI Elements
        self.frame = tk.Frame(self)
        self.frame.pack(pady=10)

        self.title_label = tk.Label(self.frame, text="Title:")
        self.title_label.grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(self.frame)
        self.title_entry.grid(row=0, column=1)

        self.author_label = tk.Label(self.frame, text="Author:")
        self.author_label.grid(row=1, column=0, sticky="w")
        self.author_entry = tk.Entry(self.frame)
        self.author_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.frame, text="Add Book", command=self.add_book)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.list_label = tk.Label(self, text="Books in Library:")
        self.list_label.pack()

        self.books_listbox = tk.Listbox(self, width=50)
        self.books_listbox.pack()

        self.remove_button = tk.Button(self, text="Remove Selected Book", command=self.remove_book)
        self.remove_button.pack(pady=5)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            book = Book(title, author)
            self.book_list.append(book)
            self.update_listbox()
            self.title_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Title and Author cannot be empty.")

    def remove_book(self):
        try:
            index = self.books_listbox.curselection()[0]
            del self.book_list[index]
            self.update_listbox()
        except IndexError:
            messagebox.showerror("Error", "Please select a book to remove.")

    def update_listbox(self):
        self.books_listbox.delete(0, tk.END)
        for book in self.book_list:
            self.books_listbox.insert(tk.END, f"{book.title} by {book.author}")

if __name__ == "__main__":
    app = LibraryApp()
    app.mainloop()
