# base_book_ui.py
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QStackedWidget, QFrame
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class TomeOfPlanesUI(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.setWindowTitle("Tome Of Planes")
        self.setMinimumSize(1000, 700)
        self.controller = controller
        self.font = QFont("Georgia", 10)
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Create empty content area
        self.content_area = self.create_content_area()
        main_layout.addWidget(self.content_area, 1)
        
        # Create empty sidebar
        self.sidebar = self.create_sidebar()
        main_layout.addWidget(self.sidebar)
        
        # Apply styling
        self.setStyleSheet("""
            QMainWindow {
                background-color: #3a1f0c;
                border: 2px solid #5a3f1c;
            }
            QLabel {
                background: transparent;
            }
        """)
    
    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setFixedWidth(240)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #2a1808;
                border-left: 2px solid #5a3f1c;
            }
        """)
        
        self.sidebar_layout = QVBoxLayout(sidebar)
        self.sidebar_layout.setSpacing(5)
        self.sidebar_layout.setContentsMargins(10, 60, 5, 20)
        
        # Add title
        title = QLabel("TOME OF PLANES")
        title.setFont(QFont("Georgia", 16, QFont.Bold))
        title.setStyleSheet("color: #e0c89c;")
        title.setAlignment(Qt.AlignCenter)
        self.sidebar_layout.addWidget(title)
        
        # Add decorative element
        deco = QLabel("✧ ✦ ✧")
        deco.setFont(QFont("Arial", 18))
        deco.setStyleSheet("color: #e0c89c;")
        deco.setAlignment(Qt.AlignCenter)
        self.sidebar_layout.addWidget(deco)
        
        # Create spacer
        self.sidebar_layout.addSpacing(20)
        
        # Create container for navigation buttons
        self.nav_buttons_container = QWidget()
        self.nav_buttons_layout = QVBoxLayout(self.nav_buttons_container)
        self.nav_buttons_layout.setSpacing(5)
        self.nav_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.addWidget(self.nav_buttons_container)
        
        # Create container for action buttons
        self.action_buttons_container = QWidget()
        self.action_buttons_layout = QVBoxLayout(self.action_buttons_container)
        self.action_buttons_layout.setSpacing(5)
        self.action_buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_layout.addWidget(self.action_buttons_container)
        
        # Add spacer
        self.sidebar_layout.addStretch()
        
        # Add footer
        footer = QLabel("© 2025 Tome Of Planes")
        footer.setFont(QFont("Georgia", 10))
        footer.setStyleSheet("color: #a09070;")
        footer.setAlignment(Qt.AlignCenter)
        self.sidebar_layout.addWidget(footer)
        
        return sidebar
    
    def create_content_area(self):
        """Create an empty content area structure"""
        content_area = QFrame()
        content_layout = QVBoxLayout(content_area)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(0)
        
        # Create stacked widget for pages
        self.stacked_widget = QStackedWidget()
        content_layout.addWidget(self.stacked_widget)
        
        return content_area
    
    def add_nav_button(self, section):
        """Add a navigation button to the sidebar"""
        from .styles import WEndTabButton  # Import here to avoid circular dependencies
        
        btn = WEndTabButton(section)
        btn.setFont(self.font)
        self.nav_buttons_layout.addWidget(btn)
        return btn
    
    def add_action_button(self, text):
        """Add an action button to the sidebar"""
        from .styles import WEndTabButton  # Import here to avoid circular dependencies
        
        btn = WEndTabButton(text)
        btn.setFont(self.font)
        self.action_buttons_layout.addWidget(btn)
        return btn
    
    def clear_nav_buttons(self):
        """Clear all navigation buttons"""
        while self.nav_buttons_layout.count():
            item = self.nav_buttons_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
    def clear_action_buttons(self):
        """Clear all action buttons"""
        while self.action_buttons_layout.count():
            item = self.action_buttons_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
    def add_page(self, widget):
        """Add a page to the content area"""
        return self.stacked_widget.addWidget(widget)
    
    def set_current_page(self, widget):
        """Set the current page in the content area"""
        self.stacked_widget.setCurrentWidget(widget)