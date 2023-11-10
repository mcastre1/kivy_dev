from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class NumPad(GridLayout):
    pass


class MainWidget(GridLayout):
    pass


# Base Class of app, it should always inherit App
class ImperialCalculator(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    ImperialCalculator().run()
