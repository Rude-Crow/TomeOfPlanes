# tome_controller.py
from data.tables_and_relations import SessionLocal, init_db
from PySide6.QtWidgets import (QWidget, QVBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from data.data_managers.plane_manager import PlaneManager
from ui.base_book_ui import TomeOfPlanesUI
from ui.pages.planes_index_ui import PlanesIndexUI
from ui.pages.plane_form_ui import PlaneFormUI
from ui.styles import WEndTabButton

class TomeController:
    def __init__(self):
        # Initialize database
        init_db()
        self.session = SessionLocal()
        self.plane_manager = PlaneManager(self.session)
        
        # Create minimal UI
        self.ui = TomeOfPlanesUI(controller=self)
        
        # Initialize sidebar and content
        self.initialize_sidebar()
        self.initialize_content()
        
        # Set initial view
        self.navigate_to("Planes")
        
        # Show UI
        self.ui.show()
    
    def initialize_sidebar(self):
        """Initialize sidebar with navigation and action buttons"""
        # Create navigation buttons
        self.nav_buttons = {}
        sections = ["Planes"]
        
        for section in sections:
            btn = self.ui.add_nav_button(section)
            btn.clicked.connect(lambda checked, s=section: self.navigate_to(s))
            self.nav_buttons[section] = btn
        
        # Create action buttons
        self.create_plane_btn = self.ui.add_action_button("Create New Plane")
        self.create_plane_btn.clicked.connect(self.show_create_plane_form)
    
    def initialize_content(self):
        """Initialize all content pages"""
        self.pages = {}
        
        # Create planes section container
        self.planes_container = QWidget()
        self.planes_container_layout = QVBoxLayout(self.planes_container)
        self.planes_container_layout.setContentsMargins(0, 0, 0, 0)
        self.ui.add_page(self.planes_container)
        self.pages["Planes"] = self.planes_container
        
    
    def navigate_to(self, section):
        """Navigate to the specified section"""
        # Update button highlighting
        for btn in self.nav_buttons.values():
            btn.setStyleSheet("")
        
        if section in self.nav_buttons:
            self.nav_buttons[section].setStyleSheet("""
                background-color: rgba(200, 180, 120, 50);
            """)
        
        # Set current page
        if section in self.pages:
            self.ui.set_current_page(self.pages[section])
        
        # Special handling for Planes section
        if section == "Planes":
            self.show_planes_index()
    
    def show_planes_index(self):
        """Show the planes index view"""
        # Clear container
        self.clear_layout(self.planes_container_layout)
        
        # Get planes from database
        planes = self.plane_manager.get_all()
        
        # Create and add planes index UI
        planes_index = PlanesIndexUI(planes, self)
        self.planes_container_layout.addWidget(planes_index)
    
    def show_create_plane_form(self):
        """Show the create plane form"""
        # Navigate to Planes section
        self.navigate_to("Planes")
        
        # Clear container
        self.clear_layout(self.planes_container_layout)
        
        # Create and add plane form UI
        plane_form = PlaneFormUI(self)
        self.planes_container_layout.addWidget(plane_form)
    
    def create_plane(self, name, plane_type, description):
        """Create a new plane in the database"""
        try:
            # Create the plane
            plane = self.plane_manager.create(
                name=name,
                description=f"[{plane_type}] {description}"
            )
            
            # Return to planes index
            self.show_planes_index()
            
            print(f"Created plane: {plane.name}")
            
        except Exception as e:
            print(f"Error creating plane: {str(e)}")
    
    def clear_layout(self, layout):
        """Clear all widgets from a layout"""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    