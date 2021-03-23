from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

Builder.load_file('6_kivy_gui.kv')

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    level = ObjectProperty(None)

    def press(self):
        name = self.name.text
        age = self.age.text
        level = self.level.text

        print(f'Mi nombre es {name}, mi edad es {age} y mi nivel actual es {level}')


class PruebaKvApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    PruebaKvApp().run()
