import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import subprocess
import os

class CodeEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Code Editor")
        self.root.geometry("800x600")

        # Initialize variables
        self.file_path = None
        self.target_file_path = None  # Variable to store the opened file path

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
        # Bind Ctrl+R to open a new PowerShell window and run app.py
        self.root.bind('<Control-r>', self.open_powershell)

    def open_file(self):
        """Open a file for editing."""
        self.file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if self.file_path:
            self.target_file_path = self.file_path  # Store the path of the opened file
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

    def open_powershell(self, event=None):
        """Open a new PowerShell window, pass target_file_path, and run app.py."""
        ide_path = os.path.abspath(__file__)  # Get the path of the current file (ide.py)
        directory = os.path.dirname(ide_path)  # Get the directory of ide.py
        script_path = os.path.join(directory, 'app.py')  # Path to app.py
        
        # Include the target file path as an argument to app.py
        if self.target_file_path:
            subprocess.Popen(['powershell', '-NoExit', '-Command', f'Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd \'{directory}\' ; python \'{script_path}\' \'{self.target_file_path}\'"'])
        else:
            messagebox.showwarning("Warning", "No code file opened to pass to app.py.")

if __name__ == "__main__":
    root = tk.Tk()
    editor = CodeEditor(root)
    root.mainloop()



















































# import tkinter as tk
# from tkinter import filedialog, messagebox, scrolledtext
# import subprocess
# import os

# class CodeEditor:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Simple Code Editor")
#         self.root.geometry("800x600")

#         # Initialize variables
#         self.file_path = None

#         # Create a menu
#         self.menu = tk.Menu(self.root)
#         self.root.config(menu=self.menu)

#         # File menu
#         self.file_menu = tk.Menu(self.menu, tearoff=0)
#         self.menu.add_cascade(label="File", menu=self.file_menu)
#         self.file_menu.add_command(label="Open", command=self.open_file)
#         self.file_menu.add_command(label="Save", command=self.save_file)
#         self.file_menu.add_separator()
#         self.file_menu.add_command(label="Exit", command=self.root.quit)

#         # Create a text area
#         self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Courier New", 12))
#         self.text_area.pack(expand=True, fill='both')

#         # Status bar to show the file path
#         self.status_bar = tk.Label(self.root, text="No file opened", bd=1, relief=tk.SUNKEN, anchor='w')
#         self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

#         # Bind Ctrl+S to save functionality
#         self.root.bind('<Control-s>', self.save_file)
#         # Bind Ctrl+R to open a new PowerShell window and run app.py
#         self.root.bind('<Control-r>', self.open_powershell)

#     def open_file(self):
#         """Open a file for editing."""
#         self.file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
#         if self.file_path:
#             with open(self.file_path, 'r') as file:
#                 code = file.read()
#                 self.text_area.delete(1.0, tk.END)  # Clear the text area
#                 self.text_area.insert(tk.END, code)  # Insert the code
#                 self.status_bar.config(text=f"Opened: {self.file_path}")

#     def save_file(self, event=None):
#         """Save the current file."""
#         if self.file_path:
#             with open(self.file_path, 'w') as file:
#                 code = self.text_area.get(1.0, tk.END)
#                 file.write(code)
#                 messagebox.showinfo("Info", "File saved successfully!")
#         else:
#             messagebox.showwarning("Warning", "No file opened to save.")

#     def open_powershell(self, event=None):
#         """Open a new PowerShell window and run app.py in the directory of ide.py."""
#         ide_path = os.path.abspath(__file__)  # Get the path of the current file (ide.py)
#         directory = os.path.dirname(ide_path)  # Get the directory of ide.py
#         script_path = os.path.join(directory, 'app.py')  # Path to app.py
#         subprocess.Popen(['powershell', '-NoExit', '-Command', f'Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd \'{directory}\' ; python \'{script_path}\'"'])
        
# if __name__ == "__main__":
#     root = tk.Tk()
#     editor = CodeEditor(root)
#     root.mainloop()

