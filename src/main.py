from kivy.app import App
from data.tables_and_relations import init_db
from ui.open_book_ui import OpenBookLayout

class TomeOfPlanes(App):
    def build(self):
        init_db()  # Ensure DB tables are created
        return OpenBookLayout()

if __name__ == "__main__":
    TomeOfPlanes().run()
