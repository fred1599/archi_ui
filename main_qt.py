import sys

from PyQt6.QtWidgets import QApplication

from infrastructure.pyqtadapter import PyqtUI

app = QApplication(sys.argv)
ui = PyqtUI()
ui.display_list_files()
ui.show()
sys.exit(app.exec())
