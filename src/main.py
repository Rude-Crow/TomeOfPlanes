from kivy.app import App
from kivy.lang import Builder
from city_logic import CityManager

class CityOfHoldingApp(App):
    def build(self):
        self.title = "City of Holding"
        Builder.load_file("city_gui.kv")
        return CityManager()

if __name__ == "__main__":
    CityOfHoldingApp().run()
