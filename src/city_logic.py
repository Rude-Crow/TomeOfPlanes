from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty

class City:
    def __init__(self, name, population="Unknown", faction="None"):
        self.name = name
        self.population = population
        self.faction = faction

    def to_dict(self):
        return {
            "name": self.name,
            "population": self.population,
            "faction": self.faction
        }

class CityManager(BoxLayout):
    city_name_input = ObjectProperty(None)
    population_input = ObjectProperty(None)
    faction_input = ObjectProperty(None)
    cities = ListProperty([])

    def add_city(self):
        name = self.city_name_input.text.strip()
        pop = self.population_input.text.strip()
        faction = self.faction_input.text.strip()

        if name:
            new_city = City(name, pop or "Unknown", faction or "None")
            self.cities.append(new_city.to_dict())
            self.clear_inputs()
            self.update_city_list()

    def clear_inputs(self):
        self.city_name_input.text = ""
        self.population_input.text = ""
        self.faction_input.text = ""

    def update_city_list(self):
        self.ids.city_list.clear_widgets()
        for city in self.cities:
            self.ids.city_list.add_widget(
                self._create_city_label(city)
            )

    def _create_city_label(self, city):
        from kivy.uix.label import Label
        return Label(
            text=f"{city['name']} | Pop: {city['population']} | Faction: {city['faction']}",
            size_hint_y=None,
            height=30
        )
