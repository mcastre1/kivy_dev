from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class MainWidget(GridLayout):
    text = StringProperty('')
    operation = []
    left_side = ''
    operator = ''
    right_side = ''

# Function called when Buttons in MainWidget widget are pressed
    def btn_pressed(self, btn):
        if btn == 'c':
            self.clear_text()
        elif btn == '=':
            pass
        else:
            self.operation.append(btn)

        self.update_text()

    def clear_text(self):
        self.operation.clear()

    def update_text(self):
        self.text = ' '.join(self.operation)


# Base Class of app, it should always inherit App
class ImperialCalculator(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    ImperialCalculator().run()
