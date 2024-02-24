import tkinter as tk
from tkinter import filedialog, Listbox, Text, Menu
from tkinter import ttk  # Pour des widgets plus modernes et un thème
from tkinter.messagebox import showwarning

from model.file import FileText
from model.directory import Directory
from model.exceptions import FileNotFoundException
from interfaces.ui import UIPort


class TkinterUI(UIPort):
    def __init__(self):
        super().__init__()
        self.file = FileText()
        self.directory = Directory()
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        self.main_window = tk.Tk()
        self.main_window.title("Votre Application")

        self.main_frame = ttk.Frame(self.main_window)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.editor = Text(self.main_frame, wrap="none")
        self.list_widget = Listbox(self.main_frame)

        self.editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.list_widget.pack(side=tk.RIGHT, fill=tk.Y)

        self.list_widget.bind("<<ListboxSelect>>", self.display_content_file)

        self.setup_menu()

    def setup_menu(self):
        self.menu_bar = Menu(self.main_window)
        self.main_window.config(menu=self.menu_bar)

        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Choisir dossier", command=self.ask_path_directory)
        self.menu_bar.add_cascade(label="Menu", menu=file_menu)

    def apply_styles(self):
        self.main_window.configure(background="#f0f0f0")
        self.editor.configure(
            bg="#f0f0f0", fg="#333", borderwidth=1, relief="solid", padx=5, pady=5
        )
        self.list_widget.configure(bg="#e8e8e8", borderwidth=0, relief="solid")

        style = ttk.Style()
        style.configure("TFrame", background="#f0f0f0")
        style.configure("TMenu", background="#c2c2c2")

    def display_content_file(self, event):
        try:
            widget = event.widget
            index = int(widget.curselection()[0])
            filename = widget.get(index)
            self.file.construct_from_directory(
                directory_name=self.directory.name, filename=filename
            )
            try:
                content = self.file.read_content()
            except FileNotFoundException as err:
                showwarning(title="Warning", message=err.message)
            else:
                self.editor.delete("1.0", tk.END)
                self.editor.insert(tk.END, content)
        except IndexError:
            pass

    def display_list_files(self):
        self.list_widget.delete(0, tk.END)
        files = self.directory.get_files()
        for filename in files:
            self.list_widget.insert(tk.END, filename)

    def ask_path_directory(self):
        self.directory.name = filedialog.askdirectory()
        self.display_list_files()
        self.editor.delete("1.0", tk.END)

    def show(self):
        self.main_window.mainloop()
