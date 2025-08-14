# main.py
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
import sys
from tome_controller import TomeController

if __name__ == "__main__":
    # Enable high DPI scaling
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    
    app = QApplication(sys.argv)
    controller = TomeController()
    sys.exit(app.exec())