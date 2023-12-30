from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class BlueBook(App):
    def build(self):
        # Layout
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # Contents
        self.home_title = Label(text="Welcome to Blue Book", font_size=30, color="#00FFCE")
        self.button = Button(text="HOME", font_size=30, size_hint=(1, 0.5), bold=True, 
                             background_color="#CEFF00")
        self.button.bind(on_press=self.callback)

        # Widgets
        self.window.add_widget(Image(source="media/images/bluebook_main.jfif"))
        self.window.add_widget(self.home_title)
        self.window.add_widget(self.button)

        return self.window
    

    def callback(self, instance):
        self.home_title.text = "Loading"

if __name__ == "__main__":
    BlueBook().run()