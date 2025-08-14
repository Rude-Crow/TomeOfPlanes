# plane_details_ui.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QTextEdit, QPushButton, QGroupBox
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from ui.styles import BookPage, FantasyButton

class PlaneDetailsUI(QWidget):
    def __init__(self, plane, controller, parent=None):
        super().__init__(parent)
        self.plane = plane
        self.controller = controller
        self.setup_ui()
        
    def setup_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create left page (details)
        left_frame = BookPage(side="left")
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(30, 20, 30, 20)
        left_layout.setSpacing(15)
        
        title = QLabel(self.plane.name)
        title.setFont(QFont("Georgia", 18, QFont.Bold))
        title.setStyleSheet("color: #3a1f0c;")
        title.setContentsMargins(0, 0, 0, 10)
        title.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(title)
        
        # Details container
        details_group = QGroupBox()
        details_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #8a6d3b;
                border-radius: 8px;
                margin-top: 10px;
                padding: 15px;
                background: rgba(245, 235, 215, 150);
            }
        """)
        details_layout = QVBoxLayout(details_group)
        details_layout.setSpacing(12)
        
        # Description
        desc_label = QLabel("Description:")
        desc_label.setFont(QFont("Georgia", 12, QFont.Bold))
        desc_label.setStyleSheet("color: #5a3f1c;")
        details_layout.addWidget(desc_label)
        
        description = QTextEdit()
        description.setFont(QFont("Georgia", 11))
        description.setPlainText(self.plane.description)
        description.setReadOnly(True)
        description.setStyleSheet("""
            QTextEdit {
                background: #f5ebd7;
                border: 1px solid #8a6d3b;
                border-radius: 4px;
                padding: 8px;
                color: #3a1f0c;
            }
        """)
        details_layout.addWidget(description)
        
        left_layout.addWidget(details_group)
        
        # Create right page (placeholder for related content)
        right_frame = BookPage(side="right")
        right_layout = QVBoxLayout(right_frame)
        right_layout.setContentsMargins(30, 20, 30, 20)
        right_layout.setSpacing(15)
        
        title = QLabel("Related Content")
        title.setFont(QFont("Georgia", 14, QFont.Bold))
        title.setStyleSheet("color: #3a1f0c;")
        title.setContentsMargins(0, 0, 0, 10)
        title.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(title)
        
        placeholder = QLabel("Locations, entities, and artifacts\nwill appear here")
        placeholder.setFont(QFont("Georgia", 12))
        placeholder.setStyleSheet("color: #5a3f1c;")
        placeholder.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(placeholder)
        
        # Add spacer to push button to bottom
        right_layout.addStretch()
        
        # Add edit button at bottom
        edit_btn = FantasyButton("Edit Plane")
        edit_btn.setFont(QFont("Georgia", 12))
        edit_btn.setMinimumHeight(40)
        edit_btn.setStyleSheet("""
            FantasyButton {
                background-color: #6d4c2c;
                color: #f9f2d9;
                border: 2px solid #5a3f1c;
                border-radius: 5px;
                padding: 8px;
            }
            FantasyButton:hover {
                background-color: #8a6d3b;
            }
        """)
        edit_btn.clicked.connect(self.edit_plane)
        right_layout.addWidget(edit_btn)
        
        main_layout.addWidget(left_frame, 1)
        main_layout.addWidget(right_frame, 1)
    
    def edit_plane(self):
        """Switch to edit view for this plane"""
        self.controller.edit_plane(self.plane.id)