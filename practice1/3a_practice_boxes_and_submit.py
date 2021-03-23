import sys

import numpy as np
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

n = 4
x = np.zeros(n)


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        self.top_grid = GridLayout()
        self.top_grid.cols = 5

        self.w1 = TextInput(multiline=False)
        self.top_grid.add_widget(self.w1)

        self.x1 = TextInput(multiline=False)
        self.top_grid.add_widget(self.x1)

        self.y1 = TextInput(multiline=False)
        self.top_grid.add_widget(self.y1)

        self.z1 = TextInput(multiline=False)
        self.top_grid.add_widget(self.z1)

        self.r1 = TextInput(multiline=False)
        self.top_grid.add_widget(self.r1)

        self.w2 = TextInput(multiline=False)
        self.top_grid.add_widget(self.w2)

        self.x2 = TextInput(multiline=False)
        self.top_grid.add_widget(self.x2)

        self.y2 = TextInput(multiline=False)
        self.top_grid.add_widget(self.y2)

        self.z2 = TextInput(multiline=False)
        self.top_grid.add_widget(self.z2)

        self.r2 = TextInput(multiline=False)
        self.top_grid.add_widget(self.r2)

        self.w3 = TextInput(multiline=False)
        self.top_grid.add_widget(self.w3)

        self.x3 = TextInput(multiline=False)
        self.top_grid.add_widget(self.x3)

        self.y3 = TextInput(multiline=False)
        self.top_grid.add_widget(self.y3)

        self.z3 = TextInput(multiline=False)
        self.top_grid.add_widget(self.z3)

        self.r3 = TextInput(multiline=False)
        self.top_grid.add_widget(self.r3)

        self.w4 = TextInput(multiline=False)
        self.top_grid.add_widget(self.w4)

        self.x4 = TextInput(multiline=False)
        self.top_grid.add_widget(self.x4)

        self.y4 = TextInput(multiline=False)
        self.top_grid.add_widget(self.y4)

        self.z4 = TextInput(multiline=False)
        self.top_grid.add_widget(self.z4)

        self.r4 = TextInput(multiline=False)
        self.top_grid.add_widget(self.r4)

        self.add_widget(self.top_grid)
        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        a = [list(map(float, [self.w1.text, self.x1.text, self.y1.text, self.z1.text, self.r1.text])),
             list(map(float, [self.w2.text, self.x2.text, self.y2.text, self.z2.text, self.r2.text])),
             list(map(float, [self.w3.text, self.x3.text, self.y3.text, self.z3.text, self.r3.text])),
             list(map(float, [self.w4.text, self.x4.text, self.y4.text, self.z4.text, self.r4.text]))]
        for i in range(n):
            if a[i][i] == 0.0:
                sys.exit('Divide by zero detected!')

            for j in range(n):
                if i != j:
                    ratio = a[j][i] / a[i][i]

                    for k in range(n + 1):
                        a[j][k] = a[j][k] - ratio * a[i][k]
        for i in range(n):
            x[i] = a[i][n] / a[i][i]
        res = ''
        for i in range(n):
            res += 'X%d = %0.2f |' % (i, x[i])

        self.add_widget(
            Label(text=res))


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
