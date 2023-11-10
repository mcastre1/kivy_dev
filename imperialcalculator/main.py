from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class MainWidget(GridLayout):
    text = StringProperty('')

    def btn_pressed(self, btn):
        self.text += f'{btn}'


# Base Class of app, it should always inherit App
class ImperialCalculator(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    ImperialCalculator().run()
