<CityManager>:
    orientation: 'vertical'
    padding: 20
    spacing: 10

    city_name_input: city_name
    population_input: population
    faction_input: faction

    Label:
        text: "City of Holding"
        font_size: '24sp'
        size_hint_y: None
        height: '40dp'
        bold: True

    BoxLayout:
        size_hint_y: None
        height: "30dp"
        spacing: 10

        TextInput:
            id: city_name
            hint_text: "City Name"

        TextInput:
            id: population
            hint_text: "Population"

        TextInput:
            id: faction
            hint_text: "Faction"

    Button:
        text: "Add City"
        size_hint_y: None
        height: "40dp"
        on_press: root.add_city()

    Label:
        text: "City Roster"
        size_hint_y: None
        height: "30dp"

    ScrollView:
        GridLayout:
            id: city_list
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            row_default_height: "30dp"
            row_force_default: True
