from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty
from kivy.lang import Builder
import os

# Load the corresponding .kv file
kv_path = os.path.join(os.path.dirname(__file__), "planes_manager_page.kv")
Builder.load_file(kv_path)


class Plane:
    def __init__(self, name, description="No description", locations=None):
        self.name = name
        self.description = description
        self.locations = locations or []

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "locations": self.locations
        }


class PlanesManager(BoxLayout):
    plane_name_input = ObjectProperty(None)
    description_input = ObjectProperty(None)
    planes = ListProperty([])  # This will hold Plane objects

    def add_plane(self):
        name = self.plane_name_input.text.strip()
        description = self.description_input.text.strip()

        if name:
            new_plane = Plane(name, description)
            self.planes.append(new_plane)
            self.clear_inputs()
            self.update_plane_list()

    def clear_inputs(self):
        self.plane_name_input.text = ""
        self.description_input.text = ""

    def update_plane_list(self):
        self.ids.plane_list.clear_widgets()
        for plane in self.planes:
            self.ids.plane_list.add_widget(
                self._create_plane_label(plane)
            )

    def _create_plane_label(self, plane):
        from kivy.uix.label import Label
        return Label(
            text=f"{plane.name} | Description: {plane.description} | Locations: {', '.join(plane.locations)}",
            size_hint_y=None,
            height=30
        )
