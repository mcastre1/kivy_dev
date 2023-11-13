from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from plyer import vibrator


class MainWidget(GridLayout):
    text = StringProperty('')
    operation = []
    operators = ['+', '-', '*', '/']  # List of available and usable operators

    # Available fractions
    fractions = {'.0625': '1/16',
                 '.125': '1/8',
                 '.1875': '3/16',
                 '.25': '1/4',
                 '.3125': '5/16',
                 '.375': '3/8',
                 '.4375': '7/16',
                 '.5': '1/2',
                 '.5625': '9/16',
                 '.625': '5/8',
                 '.6875': '11/16',
                 '.75': '3/4',
                 '.8125': '13/16',
                 '.875': '7/8',
                 '.9375': '15/16'}

    # Colors
    operand_bg = .08, .5, .8, 1
    equal_bg = .26, .78, .08, 1
    backspace_bg = .6, .5, .05, 1

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

        self.vibrate()

    # Function checks if vibrator exists in device, if so, vibrate.
    def vibrate(self):
        try:
            if vibrator.exists():
                vibrator.vibrate(.1)
        except:
            print('vibrate')

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

        self.vibrate()
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

                print(f'here. {self.operation}')
                digit_op.append(f'.{str(eval(op.strip())).split(".")[1]}')
            else:  # Append anything else
                digit_op.append(op.strip())

        self.clear_operation()

        val = str(eval(''.join(digit_op)))
        print(val)

        val = self.convert_fraction(val)
        val_split = val.split(' ')
        print(val_split)

        # Making sure returned value is in the same format as _, _, _ first self.operation format
        if len(val_split) == 2:
            self.operation.append(val_split[0])
            self.operation.append(' ' + val_split[1])
        else:
            self.operation.append(val)
        self.update_text()

    # Converts decimal points into available fractions
    def convert_fraction(self, val):
        if '.' in val:
            dec = f'.{val.split(".")[1]}'
            if dec in self.fractions.keys():
                if not val.split(".")[0] == 0:
                    val = val.split(".")[0] + ' ' + self.fractions[dec]
                else:
                    val = self.fractions[dec]

        return val


# Base Class of app, it should always inherit App
class ImperialCalculator(App):
    def build(self):
        return MainWidget()


if __name__ == "__main__":
    ImperialCalculator().run()
