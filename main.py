from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class VoiceAppLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', spacing=20, padding=20, **kwargs)

        self.label = Label(text="Voice Pro", font_size=24)
        self.add_widget(self.label)

        self.record_btn = Button(text="Start Recording")
        self.add_widget(self.record_btn)

        self.stop_btn = Button(text="Stop Recording")
        self.add_widget(self.stop_btn)

        self.robot_btn = Button(text="Robot Effect")
        self.add_widget(self.robot_btn)

        self.deep_btn = Button(text="Deep Voice")
        self.add_widget(self.deep_btn)

        self.high_btn = Button(text="High Pitch")
        self.add_widget(self.high_btn)

class VoiceProApp(App):
    def build(self):
        return VoiceAppLayout()

if __name__ == "__main__":
    VoiceProApp().run()