# planes_index_ui.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
    QListWidget, QListWidgetItem
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from ui.styles import BookPage

class PlanesIndexUI(QWidget):
    def __init__(self, planes, controller, parent=None):
        super().__init__(parent)
        self.controller = controller
        self.planes = planes
        self.setup_ui()
        
    def setup_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create left page
        left_frame = BookPage(side="left")
        left_layout = QVBoxLayout(left_frame)
        left_layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Index Of Planes")
        title.setFont(QFont("Georgia", 14, QFont.Bold))
        title.setStyleSheet("color: #000000;")
        title.setContentsMargins(20, 10, 20, 10)
        left_layout.addWidget(title, alignment=Qt.AlignCenter)
        
        self.left_list = QListWidget()
        self.left_list.setFont(QFont("Georgia", 11))
        self.left_list.setStyleSheet("""
            QListWidget {
                background: transparent;
                border: none;
                color: #000000;
            }
            QListWidget::item {
                border-bottom: 1px dashed #5a3f1c;
                padding: 8px;
            }
            QListWidget::item:selected {
                background-color: rgba(90, 63, 28, 50);
                color: #000000;
            }
        """)
        left_layout.addWidget(self.left_list)
        
        # Create right page
        right_frame = BookPage(side="right")
        right_layout = QVBoxLayout(right_frame)
        right_layout.setContentsMargins(30, 30, 30, 30)
        
        title = QLabel("Index Continued")
        title.setFont(QFont("Georgia", 14, QFont.Bold))
        title.setStyleSheet("color: #000000;")
        title.setContentsMargins(20, 10, 20, 10)
        right_layout.addWidget(title, alignment=Qt.AlignCenter)
        
        self.right_list = QListWidget()
        self.right_list.setFont(QFont("Georgia", 11))
        self.right_list.setStyleSheet(self.left_list.styleSheet())
        right_layout.addWidget(self.right_list)
        
        main_layout.addWidget(left_frame, 1)
        main_layout.addWidget(right_frame, 1)
        
        self.populate_lists()
        
    def populate_lists(self):
        # Split planes between left and right pages
        total_planes = len(self.planes)
        left_count = (total_planes + 1) // 2  # Left gets one more if odd
        left_planes = self.planes[:left_count]
        right_planes = self.planes[left_count:]
        
        # Add planes to left list
        for plane in left_planes:
            item = QListWidgetItem(plane.name)
            item.setData(Qt.UserRole, plane.id)
            self.left_list.addItem(item)
        
        # Add planes to right list
        for plane in right_planes:
            item = QListWidgetItem(plane.name)
            item.setData(Qt.UserRole, plane.id)
            self.right_list.addItem(item)
        
        # Add "No Planes" message if needed
        if not left_planes and not right_planes:
            item = QListWidgetItem("No planes found. Create one using the sidebar button.")
            item.setFlags(item.flags() & ~Qt.ItemIsEnabled)
            self.left_list.addItem(item)
        
        # Connect click events
        self.left_list.itemClicked.connect(self.on_plane_clicked)
        self.right_list.itemClicked.connect(self.on_plane_clicked)
    
    def on_plane_clicked(self, item):
        """Handle plane item click"""
        plane_id = item.data(Qt.UserRole)
        self.controller.show_plane_details(plane_id)
        
        # For now, just show a back button in sidebar
        self.controller.current_sidebar_state = "details"
        self.controller.update_sidebar()