from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QPlainTextEdit,
    QListWidget,
    QHBoxLayout,
    QListWidgetItem,
    QMainWindow,
    QWidget,
    QFileDialog,
)

from model.file import FileText
from model.directory import Directory
from interfaces.ui import UIPort


class PyqtUI(UIPort):
    def __init__(self):
        super().__init__()
        self.file = FileText()
        self.directory = Directory()
        self.setup_ui()

    def setup_ui(self):
        self.main_window = QMainWindow()
        self.main_widget = QWidget()
        self.layout = QHBoxLayout(self.main_widget)
        self.editor = QPlainTextEdit(self.main_widget)
        self.list_widget = QListWidget(self.main_widget)

        self.layout.addWidget(self.editor)
        self.layout.addWidget(self.list_widget)

        self.list_widget.itemClicked.connect(self.display_content_file)

        self.setup_menu()

        self.main_window.setCentralWidget(self.main_widget)

    def setup_menu(self):
        menu_bar = self.main_window.menuBar()
        menu = menu_bar.addMenu("&Menu")

        choose_directory_action = QAction(
            text="&Choisir dossier", parent=self.main_widget
        )
        choose_directory_action.triggered.connect(self.ask_path_directory)
        menu.addAction(choose_directory_action)

    def display_content_file(self, item: QListWidgetItem) -> None:
        filename = item.text()
        self.file.construct_from_directory(
            directory_name=self.directory.name, filename=filename
        )
        content = self.file.read_content()
        self.editor.setPlainText(content)

    def display_list_files(self) -> None:
        self.list_widget.clear()
        files = self.directory.get_files()
        for filename in files:
            self.list_widget.addItem(QListWidgetItem(filename))

    def ask_path_directory(self) -> str:
        self.directory.name = QFileDialog.getExistingDirectory()
        self.display_list_files()
        self.editor.clear()

    def show(self):
        self.main_window.show()
