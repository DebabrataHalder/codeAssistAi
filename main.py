import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class CodeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Code Editor")
        self.root.geometry("800x600")

        # Initialize variables
        self.file_path = None

        # Create a menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # File menu
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Create a text area
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Courier New", 12))
        self.text_area.pack(expand=True, fill='both')

        # Status bar to show the file path
        self.status_bar = tk.Label(self.root, text="No file opened", bd=1, relief=tk.SUNKEN, anchor='w')
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Bind Ctrl+S to save functionality
        self.root.bind('<Control-s>', self.save_file)

    def open_file(self):
        """Open a file for editing."""
        self.file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if self.file_path:
            with open(self.file_path, 'r') as file:
                code = file.read()
                self.text_area.delete(1.0, tk.END)  # Clear the text area
                self.text_area.insert(tk.END, code)  # Insert the code
                self.status_bar.config(text=f"Opened: {self.file_path}")

    def save_file(self, event=None):
        """Save the current file."""
        if self.file_path:
            with open(self.file_path, 'w') as file:
                code = self.text_area.get(1.0, tk.END)
                file.write(code)
                messagebox.showinfo("Info", "File saved successfully!")
        else:
            messagebox.showwarning("Warning", "No file opened to save.")

if __name__ == "__main__":
    root = tk.Tk()
    editor = CodeEditor(root)
    root.mainloop()