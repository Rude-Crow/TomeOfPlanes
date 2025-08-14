# plane_form_ui.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QLineEdit, QTextEdit, QPushButton,
    QGroupBox, QSizePolicy, QScrollArea
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
        left_layout.setContentsMargins(30, 20, 30, 20)
        left_layout.setSpacing(15)
        
        title = QLabel("Create New Plane")
        title.setFont(QFont("Georgia", 16, QFont.Bold))
        title.setStyleSheet("color: #3a1f0c;")
        title.setContentsMargins(0, 0, 0, 10)
        title.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(title)
        
        # Form group box
        form_group = QGroupBox()
        form_group.setStyleSheet("""
            QGroupBox {
                border: 1px solid #8a6d3b;
                border-radius: 8px;
                margin-top: 10px;
                padding: 15px;
                background: rgba(245, 235, 215, 150);
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 5px;
                color: #5a3f1c;
            }
        """)
        form_layout = QVBoxLayout(form_group)
        form_layout.setSpacing(12)
        
        # Plane Name
        name_label = QLabel("Plane Name:")
        name_label.setFont(QFont("Georgia", 12))
        name_label.setStyleSheet("color: #3a1f0c;")
        form_layout.addWidget(name_label)
        
        self.name_input = QLineEdit()
        self.name_input.setFont(QFont("Georgia", 12))
        self.name_input.setStyleSheet("""
            QLineEdit {
                background: #f5ebd7;
                border: 1px solid #8a6d3b;
                border-radius: 4px;
                padding: 8px;
                color: #3a1f0c;
            }
        """)
        form_layout.addWidget(self.name_input)
        
        # Description
        desc_label = QLabel("Description:")
        desc_label.setFont(QFont("Georgia", 12))
        desc_label.setStyleSheet("color: #3a1f0c;")
        form_layout.addWidget(desc_label)
        
        self.desc_input = QTextEdit()
        self.desc_input.setFont(QFont("Georgia", 12))
        self.desc_input.setStyleSheet("""
            QTextEdit {
                background: #f5ebd7;
                border: 1px solid #8a6d3b;
                border-radius: 4px;
                padding: 8px;
                color: #3a1f0c;
            }
        """)
        form_layout.addWidget(self.desc_input)
        
        left_layout.addWidget(form_group)
        
        # Submit Button - centered with proper sizing
        submit_btn = FantasyButton("CREATE PLANE")
        submit_btn.setFont(QFont("Georgia", 13, QFont.Bold))
        submit_btn.setMinimumHeight(50)
        submit_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        submit_btn.setStyleSheet("""
            FantasyButton {
                background-color: #8a6d3b;
                color: #f9f2d9;
                border: 2px solid #5a3f1c;
                border-radius: 5px;
                padding: 12px;
                min-width: 200px;
            }
            FantasyButton:hover {
                background-color: #a1885f;
            }
        """)
        submit_btn.clicked.connect(self.on_submit)
        left_layout.addWidget(submit_btn, alignment=Qt.AlignCenter)
        
        # Create right page (guide)
        right_frame = BookPage(side="right")
        right_layout = QVBoxLayout(right_frame)
        right_layout.setContentsMargins(30, 15, 30, 15)
        right_layout.setSpacing(10)
        
        title = QLabel("Plane Creation Guide")
        title.setFont(QFont("Georgia", 14, QFont.Bold))
        title.setStyleSheet("color: #3a1f0c;")
        title.setContentsMargins(0, 0, 0, 5)
        title.setAlignment(Qt.AlignCenter)
        right_layout.addWidget(title)
        
        # Create scroll area for guide content
        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: none;
            }
            QScrollBar:vertical {
                border: none;
                background: #f5ebd7;
                width: 10px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #8a6d3b;
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)
        scroll_area.setWidgetResizable(True)
        
        # Create container for guide text
        guide_container = QWidget()
        guide_container.setStyleSheet("background: transparent;")
        guide_container_layout = QVBoxLayout(guide_container)
        guide_container_layout.setContentsMargins(0, 0, 10, 0)
        
        guide_text = """
        <div style="font-family: Georgia; font-size: 11pt; color: #3a1f0c;">
            <h3 style="color: #5a3f1c; margin-top: 5px; margin-bottom: 8px;">Creating a New Plane</h3>
            <p>When creating a new plane, consider the following:</p>
            <ul style="margin-top: 3px; margin-bottom: 12px;">
                <li><strong>Name:</strong> Should be unique and descriptive</li>
                <li><strong>Description:</strong> Include key features, inhabitants, and environment</li>
            </ul>
            
            <h3 style="color: #5a3f1c; margin-top: 15px; margin-bottom: 8px;">Tips for Description</h3>
            <ul style="margin-top: 3px;">
                <li>Describe the plane's physical characteristics</li>
                <li>Mention notable locations or landmarks</li>
                <li>Include any unique magical properties</li>
                <li>Describe potential dangers or special conditions</li>
                <li>Note how this plane connects to others</li>
                <li>Detail the inhabitants and their societies</li>
                <li>Explain any unusual laws of physics or magic</li>
                <li>Include climate and environmental features</li>
            </ul>
            
            <h3 style="color: #5a3f1c; margin-top: 15px; margin-bottom: 8px;">Examples</h3>
            <p style="margin-bottom: 10px;"><strong>Feywild:</strong> A vibrant, chaotic reflection of the material plane filled with wild magic and fey creatures. Time flows differently here, and emotions manifest physically.</p>
            <p><strong>Shadowfell:</strong> A gloomy, desolate plane where light and hope fade, inhabited by shadow creatures and the undead. Everything here feels heavy and oppressive.</p>
        </div>
        """
        
        guide_label = QLabel(guide_text)
        guide_label.setFont(QFont("Georgia", 11))
        guide_label.setWordWrap(True)
        guide_label.setStyleSheet("background: transparent;")
        guide_label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        guide_container_layout.addWidget(guide_label)
        guide_container_layout.addStretch()
        
        scroll_area.setWidget(guide_container)
        right_layout.addWidget(scroll_area)
        
        main_layout.addWidget(left_frame, 1)
        main_layout.addWidget(right_frame, 1)
    
    def on_submit(self):
        """Collect form data and pass to controller"""
        name = self.name_input.text().strip()
        description = self.desc_input.toPlainText().strip()
        
        if name:
            self.controller.create_plane(name, description)