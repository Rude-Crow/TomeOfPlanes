# plane_form_ui.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QTextEdit, QComboBox, QPushButton
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from ui.styles import BookPage, FantasyButton

class PlaneFormUI(QWidget):
    def __init__(self, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.setup_ui()
        
    def setup_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create left page (form)
        left_frame = BookPage(side="left")
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Create New Plane")
        title.setFont(QFont("Georgia", 14, QFont.Bold))
        title.setStyleSheet("color: #000000;")
        title.setContentsMargins(20, 10, 20, 10)
        left_layout.addWidget(title, alignment=Qt.AlignCenter)
        
        # Plane Name
        name_label = QLabel("Plane Name:")
        name_label.setFont(QFont("Georgia", 11))
        left_layout.addWidget(name_label)
        
        self.name_input = QLineEdit()
        self.name_input.setFont(QFont("Georgia", 11))
        self.name_input.setStyleSheet("background: #f5ebd7; border: 1px solid #5a3f1c; padding: 5px;")
        left_layout.addWidget(self.name_input)
        
        # Plane Type
        type_label = QLabel("Plane Type:")
        type_label.setFont(QFont("Georgia", 11))
        left_layout.addWidget(type_label)
        
        self.type_combo = QComboBox()
        self.type_combo.setFont(QFont("Georgia", 11))
        self.type_combo.setStyleSheet("background: #f5ebd7; border: 1px solid #5a3f1c; padding: 5px;")
        self.type_combo.addItems(["Material Plane", "Ethereal Plane", "Elemental Plane", "Astral Plane", "Other"])
        left_layout.addWidget(self.type_combo)
        
        # Description
        desc_label = QLabel("Description:")
        desc_label.setFont(QFont("Georgia", 11))
        left_layout.addWidget(desc_label)
        
        self.desc_input = QTextEdit()
        self.desc_input.setFont(QFont("Georgia", 11))
        self.desc_input.setStyleSheet("background: #f5ebd7; border: 1px solid #5a3f1c; padding: 5px;")
        left_layout.addWidget(self.desc_input)
        
        # Submit Button
        submit_btn = FantasyButton("Create Plane")
        submit_btn.setFont(QFont("Georgia", 12))
        submit_btn.clicked.connect(self.on_submit)
        left_layout.addWidget(submit_btn, alignment=Qt.AlignCenter)
        
        # Create right page (guide)
        right_frame = BookPage(side="right")
        right_layout = QVBoxLayout(right_frame)
        right_layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Plane Creation Guide")
        title.setFont(QFont("Georgia", 14, QFont.Bold))
        title.setStyleSheet("color: #000000;")
        title.setContentsMargins(20, 10, 20, 10)
        right_layout.addWidget(title, alignment=Qt.AlignCenter)
        
        guide_text = """
        <div style="font-family: Georgia; font-size: 11pt;">
            <h3>Creating a New Plane</h3>
            <p>When creating a new plane, consider the following:</p>
            <ul>
                <li><strong>Name:</strong> Should be unique and descriptive</li>
                <li><strong>Type:</strong> Determines fundamental properties</li>
                <li><strong>Description:</strong> Include key features and inhabitants</li>
            </ul>
            <p><strong>Plane Types:</strong></p>
            <ul>
                <li><strong>Material:</strong> Physical worlds like the Prime Material Plane</li>
                <li><strong>Ethereal:</strong> Misty, transitional planes</li>
                <li><strong>Elemental:</strong> Pure elemental domains (Fire, Water, etc.)</li>
                <li><strong>Astral:</strong> Space between planes</li>
                <li><strong>Other:</strong> Custom plane types</li>
            </ul>
        </div>
        """
        
        guide_label = QLabel(guide_text)
        guide_label.setFont(QFont("Georgia", 11))
        guide_label.setWordWrap(True)
        guide_label.setStyleSheet("background: transparent;")
        right_layout.addWidget(guide_label)
        
        main_layout.addWidget(left_frame, 1)
        main_layout.addWidget(right_frame, 1)
    
    def on_submit(self):
        """Collect form data and pass to controller"""
        name = self.name_input.text().strip()
        plane_type = self.type_combo.currentText()
        description = self.desc_input.toPlainText().strip()
        
        if name:
            self.controller.create_plane(name, plane_type, description)