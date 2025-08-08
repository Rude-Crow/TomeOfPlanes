from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from ui.planes_manager_page import PlanesManager

class MainScreen(Screen):
    pass

class TomeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(PlanesManager(name="planes"))
        return sm

if __name__ == '__main__':
    TomeApp().run()