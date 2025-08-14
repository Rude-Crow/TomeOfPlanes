# tome_controller.py
from data.tables_and_relations import SessionLocal, init_db
from PySide6.QtWidgets import (QWidget, QVBoxLayout, 
    QLabel
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from data.data_managers.plane_manager import PlaneManager
from ui.base_book_ui import TomeOfPlanesUI
from ui.pages.plane_details_ui import PlaneDetailsUI
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
        self.sections = ["Planes", "Locations", "Sub-Locations", "Quests", "NPCs"]
        
        # Initialize sidebar and content
        self.ui.sidebar = self.ui.sidebar
        self.previous_sidebar_state = None
        self.current_sidebar_state = "main"
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
        
        for section in self.sections:
            btn = self.ui.add_nav_button(section)
            btn.clicked.connect(lambda checked, s=section: self.navigate_to(s))
            self.nav_buttons[section] = btn
        
        # Create action buttons
        self.create_plane_btn = self.ui.add_action_button("Create New Plane")
        self.create_plane_btn.clicked.connect(self.show_create_plane_form)

    def update_sidebar(self):
        """Update sidebar based on current state"""
        # Clear existing buttons PROPERLY
        self.ui.clear_nav_buttons()
        self.ui.clear_action_buttons()
        
        # Add new buttons based on state
        if self.current_sidebar_state == "main":
            self.setup_main_sidebar()
        elif self.current_sidebar_state == "form":
            self.update_sidebar_for_form()
        elif self.current_sidebar_state == "details":
            self.update_sidebar_for_details()
        
        # Force UI refresh
        self.ui.sidebar.updateGeometry()
        self.ui.sidebar.update()
        self.ui.sidebar.repaint()
    
    def setup_main_sidebar(self):
        """Set up sidebar for main navigation"""
        # Add navigation buttons
        for section in self.sections:
            btn = self.ui.add_nav_button(section)
            btn.clicked.connect(lambda checked, s=section: self.navigate_to(s))
            self.nav_buttons[section] = btn
        
        # Add Create Plane button
        self.create_plane_btn = self.ui.add_action_button("Create New Plane")
        self.create_plane_btn.clicked.connect(self.show_create_plane_form)
    
    def update_sidebar_for_form(self):
        """Update sidebar for form view with back button"""
        # Add Back to Planes button
        back_btn = self.ui.add_action_button("Back to Planes")
        back_btn.clicked.connect(self.show_planes_index)
        
        # Style the back button differently
        back_btn.setStyleSheet("""
            WEndTabButton {
                background-color: #5a3f1c;
                color: #f9f2d9;
            }
            WEndTabButton:hover {
                background-color: #7a5f3c;
            }
        """)
    
    def initialize_content(self):
        """Initialize all content pages"""
        self.pages = {}
        
        # Create planes section container
        self.planes_container = QWidget()
        self.planes_container_layout = QVBoxLayout(self.planes_container)
        self.planes_container_layout.setContentsMargins(0, 0, 0, 0)
        self.ui.add_page(self.planes_container)
        self.pages["Planes"] = self.planes_container
        
        # Create other sections (simplified)
        for section in self.sections:
            if section == "Planes":
                continue
                
            # For simplicity, just add placeholder widgets
            widget = QLabel(f"Content for {section} section")
            widget.setFont(QFont("Georgia", 16))
            widget.setAlignment(Qt.AlignCenter)
            self.ui.add_page(widget)
            self.pages[section] = widget
        
    
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
            # If we're in form state, don't reset to index
            if self.current_sidebar_state != "form":
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
        
        # Restore sidebar state
        self.current_sidebar_state = "main"
        self.previous_sidebar_state = None
        
        # Update sidebar
        self.update_sidebar()
    
    def show_create_plane_form(self):
        """Show the create plane form"""
        # Save current sidebar state
        self.previous_sidebar_state = self.current_sidebar_state
        self.current_sidebar_state = "form"
        
        # Navigate to Planes section
        self.navigate_to("Planes")
        
        # Clear container
        self.clear_layout(self.planes_container_layout)
        
        # Create and add plane form UI
        plane_form = PlaneFormUI(self)
        self.planes_container_layout.addWidget(plane_form)
        
        # Update sidebar for form view
        self.update_sidebar()
    
    def create_plane(self, name, description):
        """Create a new plane in the database"""
        try:
            # Create the plane
            plane = self.plane_manager.create(
                name=name,
                description=description
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

    def update_sidebar_for_details(self):
        """Update sidebar for details view with back button"""
        # Add Back to Planes button
        back_btn = self.ui.add_action_button("Back to Planes")
        back_btn.clicked.connect(self.show_planes_index)
        
        # Style the back button
        back_btn.setStyleSheet("""
            WEndTabButton {
                background-color: #5a3f1c;
                color: #f9f2d9;
            }
            WEndTabButton:hover {
                background-color: #7a5f3c;
            }
        """)

    def edit_plane(self, plane_id):
        """Edit a specific plane"""
        # TODO: Implement edit functionality
        print(f"Editing plane: {plane_id}")
        # For now, just show a message
        plane = self.plane_manager.get_by_id(plane_id)
        if plane:
            print(f"Editing: {plane.name}")

    def update_sidebar_for_details(self):
        """Update sidebar for details view with back button"""
        # Clear existing buttons
        self.ui.clear_nav_buttons()
        self.ui.clear_action_buttons()
        
        # Add Back to Planes button
        back_btn = self.ui.add_action_button("Back to Planes")
        back_btn.clicked.connect(self.show_planes_index)
        
        # Style the back button
        back_btn.setStyleSheet("""
            WEndTabButton {
                background-color: #5a3f1c;
                color: #f9f2d9;
            }
            WEndTabButton:hover {
                background-color: #7a5f3c;
            }
        """)
    
    def show_plane_details(self, plane_id):
        """Show details for a specific plane"""
        # Get plane from database
        plane = self.plane_manager.get_by_id(plane_id)
        
        if not plane:
            print(f"Plane with ID {plane_id} not found")
            return
            
        # Save current sidebar state
        self.previous_sidebar_state = self.current_sidebar_state
        self.current_sidebar_state = "details"
        
        # Navigate to Planes section
        self.navigate_to("Planes")
        
        # Clear container
        self.clear_layout(self.planes_container_layout)
        
        # ALWAYS create a new details UI - remove caching logic
        details_ui = PlaneDetailsUI(plane, self)
        
        # Add to container
        self.planes_container_layout.addWidget(details_ui)
        
        # Update sidebar
        self.update_sidebar()