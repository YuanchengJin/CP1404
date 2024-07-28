from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.core.audio import SoundLoader
import os

class GuitarsApp(App):
    def build(self):
        self.sound = None

        layout = BoxLayout(orientation='vertical')

        # Add a label
        label = Label(text='Welcome to GuitarsApp', font_size='20sp')
        layout.add_widget(label)

        # Add a spinner for selecting guitars
        self.spinner = Spinner(
            text='Select Guitar',
            values=('Acoustic', 'Electric', 'Bass'),
            size_hint=(1, 0.2))
        self.spinner.bind(text=self.show_guitar)
        layout.add_widget(self.spinner)

        # Add an image placeholder
        self.guitar_image = Image(source=self.get_image_path('guitar.png'))  # Default image
        layout.add_widget(self.guitar_image)

        # Add a button
        button = Button(text='Play Guitar', size_hint=(1, 0.2))
        button.bind(on_press=self.play_guitar)
        layout.add_widget(button)

        return layout

    def get_image_path(self, filename):
        # Define the path to your images directory
        return os.path.join(os.path.dirname(__file__), filename)

    def show_guitar(self, spinner, text):
        guitar_images = {
            'Acoustic': self.get_image_path('acoustic_guitar.png'),
            'Electric': self.get_image_path('electric_guitar.png'),
            'Bass': self.get_image_path('bass_guitar.png')
        }
        self.guitar_image.source = guitar_images.get(text, self.get_image_path('guitar.png'))

    def play_guitar(self, instance):
        if self.sound:
            self.sound.stop()

        guitar_sounds = {
            'Acoustic': 'acoustic_sound.mp3',
            'Electric': 'electric_sound.mp3',
            'Bass': 'bass_sound.mp3'
        }
        sound_file = guitar_sounds.get(self.spinner.text, None)

        if sound_file:
            self.sound = SoundLoader.load(sound_file)
            if self.sound:
                self.sound.play()
            else:
                print(f"Error loading sound: {sound_file}")
        else:
            print("Select a guitar to play sound")

if __name__ == '__main__':
    GuitarsApp().run()
