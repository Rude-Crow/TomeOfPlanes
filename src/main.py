from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file("tome_style.kv")


class OpenBookLayout(BoxLayout):
    pass


class TomeOfPlanes(App):
    def build(self):
        return OpenBookLayout()


if __name__ == "__main__":
    TomeOfPlanes().run()
