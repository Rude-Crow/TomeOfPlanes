from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock

from data.planes_manager import PlanesManager
from kivy.lang import Builder
import os

kv_path = os.path.join(os.path.dirname(__file__), "tome_style.kv")
Builder.load_file(kv_path)

class OpenBookLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.planes_manager = PlanesManager()
        Clock.schedule_once(self._finish_init, 0)

    def _finish_init(self, dt):
        self.load_planes_index()

    def load_planes_index(self):
        self.ids.left_page.clear_widgets()
        right_page = self.ids.right_container.ids.right_page
        right_page.clear_widgets()

        planes = self.planes_manager.get_all_planes()
        half = (len(planes) + 1) // 2

        left_planes = planes[:half]
        right_planes = planes[half:]

        for plane in left_planes:
            btn = Button(text=plane.name, size_hint_y=None, height=50)
            btn.bind(on_release=lambda btn, p=plane: self.show_plane_detail(p))
            self.ids.left_page.add_widget(btn)

        for plane in right_planes:
            btn = Button(text=plane.name, size_hint_y=None, height=50)
            btn.bind(on_release=lambda btn, p=plane: self.show_plane_detail(p))
            right_page.add_widget(btn)

        add_btn = Button(text="➕ Add Plane", size_hint_y=None, height=50)
        add_btn.bind(on_release=self.show_create_plane_form)
        right_page.add_widget(add_btn)

    def show_plane_detail(self, plane):
        self.ids.left_page.clear_widgets()
        right_page = self.ids.right_container.ids.right_page
        right_page.clear_widgets()

        self.ids.left_page.add_widget(Label(text=plane.name, font_size=24))
        right_page.add_widget(Label(text=plane.description, font_size=18))

    def show_create_plane_form(self, instance):
        self.ids.left_page.clear_widgets()
        right_page = self.ids.right_container.ids.right_page
        right_page.clear_widgets()

        self.name_input = TextInput(hint_text="Plane Name", size_hint_y=None, height=40)
        self.desc_input = TextInput(hint_text="Description", multiline=True, size_hint_y=None, height=100)
        save_btn = Button(text="Save Plane", size_hint_y=None, height=40)
        save_btn.bind(on_release=self.save_plane)

        self.ids.left_page.add_widget(Label(text="Create New Plane", font_size=22))
        right_page.add_widget(self.name_input)
        right_page.add_widget(self.desc_input)
        right_page.add_widget(save_btn)

    def save_plane(self, instance):
        name = self.name_input.text.strip()
        description = self.desc_input.text.strip()
        if not name:
            # Optional: add error popup or message
            return
        self.planes_manager.add_plane(name, description)
        self.load_planes_index()
