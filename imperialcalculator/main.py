from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class MainWidget(GridLayout):
    text = StringProperty('')
    operation = ['', '', '']
    left_side = True

    # Function called when Buttons in MainWidget widget are pressed
    def btn_pressed(self, btn):
        if btn == 'c':
            self.clear_text()
        elif btn == '=':  # Using the built-in function eval to evaluate an operation in string format
            print(eval(' '.join(self.operation)))
        elif btn == '+' or btn == '-':
            if self.operation[0] == '':
                self.operation[0] = '0'
            self.operation[1] = btn
            self.left_side = False

        else:  # When a number is pressed
            op = str(eval(btn))
            if self.left_side:
                self.operation[0] += f'.{op.split(".")[1]}' if '0' in op else op
            else:
                self.operation[2] += f'.{op.split(".")[1]}' if '0' in op else op

        self.update_text()

    # Function called when operation list and display need to be cleared.
    def clear_text(self):
        self.operation = ['', '', '']
        self.left_side = True

    # Turns the operation list into a string and displays it on the main widget text box
    def update_text(self):
        self.text = ' '.join(self.operation)


# Base Class of app, it should always inherit App
class ImperialCalculator(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    ImperialCalculator().run()
