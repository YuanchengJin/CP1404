from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    """Main Kivy app to demonstrate dynamic Label creation."""

    def __init__(self, **kwargs):
        """Initialize the app."""
        super().__init__(**kwargs)
        # Define a list of names (data model)
        self.names = ["Alice", "Bob", "Charlie", "David"]

    def build(self):
        """Build the Kivy app."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the list of names and add them to the GUI."""
        for name in self.names:
            label = Label(text=name)
            self.root.ids.labels_box.add_widget(label)

DynamicLabelsApp().run()
