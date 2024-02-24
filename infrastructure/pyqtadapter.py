from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QPlainTextEdit,
    QListWidget,
    QHBoxLayout,
    QListWidgetItem,
    QMainWindow,
    QWidget,
    QFileDialog,
    QMessageBox,
)

from model.file import FileText
from model.directory import Directory
from model.exceptions import FileNotFoundException
from interfaces.ui import UIPort


class PyqtUI(UIPort):
    def __init__(self) -> None:
        super().__init__()
        self.file = FileText()
        self.directory = Directory()
        self.setup_ui()

    def setup_ui(self) -> None:
        self.main_window = QMainWindow()
        self.main_widget = QWidget()
        self.layout = QHBoxLayout(self.main_widget)
        self.editor = QPlainTextEdit(self.main_widget)
        self.list_widget = QListWidget(self.main_widget)
        self.message_box = QMessageBox(parent=self.main_widget)

        self.layout.addWidget(self.editor)
        self.layout.addWidget(self.list_widget)

        self.list_widget.itemClicked.connect(self.display_content_file)

        self.setup_menu()

        self.main_window.setCentralWidget(self.main_widget)

        self.apply_styles()

    def setup_menu(self) -> None:
        menu_bar = self.main_window.menuBar()
        menu = menu_bar.addMenu("&Menu")

        choose_directory_action = QAction(
            text="&Choisir dossier", parent=self.main_widget
        )
        choose_directory_action.triggered.connect(self.ask_path_directory)
        menu.addAction(choose_directory_action)

    def apply_styles(self) -> None:
        self.main_window.setStyleSheet(
            """
            QWidget {
                font-size: 14px;
                color: #333;
            }
            QPlainTextEdit {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                padding: 5px;
            }
            QListWidget {
                background-color: #e8e8e8;
                border: none;
            }
            QMenuBar {
                background-color: #a1a1a1;
            }
            QMenu {
                background-color: #c2c2c2;
            }
            QAction {
                background-color: #d3d3d3;
            }
        """
        )

    def display_content_file(self, item: QListWidgetItem) -> None:
        filename = item.text()
        self.file.construct_from_directory(
            directory_name=self.directory.name, filename=filename
        )
        try:
            content = self.file.read_content()
        except FileNotFoundException as err:
            self.message_box.setText(err.message)
            self.message_box.exec()
        else:
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

    def show(self) -> None:
        self.main_window.show()
