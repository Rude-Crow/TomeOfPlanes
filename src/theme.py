from kivy.properties import ColorProperty, StringProperty

class Theme:
    # Font paths (make sure these fonts exist in your app's directory)
    HeaderFont = StringProperty("fonts/UncialAntiqua-Regular.ttf")
    BodyFont = StringProperty("fonts/EBGaramond-Regular.ttf")

    # Colors (RGBA format)
    BackgroundColor = ColorProperty([0.93, 0.89, 0.82, 1])   # #EDE3D2
    PrimaryTextColor = ColorProperty([0.17, 0.11, 0.06, 1])  # #2C1B0F
    AccentGlow = ColorProperty([0.0, 1.0, 0.89, 1])           # #00FFE4
    ButtonBackground = ColorProperty([0.55, 0.35, 0.23, 1])   # #8C5A3A
    BorderColor = ColorProperty([0.66, 0.45, 0.31, 1])        # #A9744F
    Highlight = ColorProperty([1.0, 0.84, 0.44, 1])           # #FFD56F
    MutedText = ColorProperty([0.71, 0.66, 0.59, 1])          # #B4A996
    Error = ColorProperty([0.7, 0.21, 0.21, 1])               # #B23535