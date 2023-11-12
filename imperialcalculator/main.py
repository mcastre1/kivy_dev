from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout


class MainWidget(GridLayout):
    text = StringProperty('')
    operation = []
    operators = ['+', '-', '*', '/']  # List of available and usable operators

    # Function called when Buttons in MainWidget widget are pressed
    def btn_pressed(self, btn):
        if btn == 'c':
            self.clear_operation()
        elif btn == '=':  # Using the built-in function eval to evaluate an operation in string format
            self.evaluate()
        else:
            if '/' in btn and len(btn) > 1:
                if len(self.operation) > 0:
                    if not '/' in self.operation[-1]:
                        if self.operation[-1].strip() in self.operators:
                            self.operation.append(btn)
                        else:
                            self.operation.append(f' {btn}')
                else:
                    self.operation.append(btn)

            elif btn in self.operators:
                if len(self.operation) > 0:
                    if not self.operation[-1].strip() in self.operators:
                        self.operation.append(f' {btn} ')
            else:
                self.operation.append(btn)

        self.update_text()

    # Function called when operation list and display need to be cleared.
    def clear_operation(self):
        self.operation.clear()

    # Turns the operation list into a string and displays it on the main widget text box
    def update_text(self):
        self.text = ''.join(self.operation)

    # Remove the last item in the list, if the list has more than one item.
    def backspace(self):
        if len(self.operation) > 0:
            self.operation.pop()
        self.update_text()

    # Translates fraction format numbers to actual decimals
    def evaluate(self):
        digit_op = []

        if len(self.operation) == 0:
            return
        if self.operation[-1].strip() in self.operators:
            return

        for op in self.operation:
            print(op.strip())
            if '/' in op and len(op.strip()) > 2:  # Here is where we translate the fraction format number to decimal

                digit_op.append(f'.{str(eval(op.strip())).split(".")[1]}')
            else:  # Append anything else
                digit_op.append(op.strip())

        self.clear_operation()
        self.operation.append(str(eval(''.join(digit_op))))
        self.update_text()
        print(eval(''.join(digit_op)))


# Base Class of app, it should always inherit App
class ImperialCalculator(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    ImperialCalculator().run()
