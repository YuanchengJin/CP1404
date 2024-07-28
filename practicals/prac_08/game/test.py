# from kivy.app import App
# from kivy.app import Widget
# class HelloWorld(App):
#     def build(self):
#         self.root = Widget()
#         return self.root
# HelloWorld().run()

# from kivy.app import App
# from kivy.app import Builder
# class HelloKv(App):
#     def build(self):
#         self.title = "Hello world!"
#         self.root = Builder.load_file('widget.kv')
#         return self.root
# HelloKv().run()


# from kivy.app import App
# from kivy.lang import Builder
# # class ButtonEventDemo(App):
#     def build(self):
#         self.title = "Button Event Demo"
#         self.root = Builder.load_file('button_event.kv')
#         return self.root
#
#     def press_button(self):
#         print("ouch!")
#
# ButtonEventDemo().run()
#
# class ButtonEvent(App):
#     def build(self):
#         self.title = "Button Event Demo"
#         self.root = Builder.load_file("test1.kv")
#         return self.root
#
#     def press_button(self):
#         print("Ouch!")

from kivy.app import App
from kivy.lang import Builder

class ButtonEvent(App):
    def build(self):
        self.title = "Button Event Demo"
        self.root = Builder.load_file("test3.kv")
        return self.root

    def press_button(self):
        print("Ouch!")

# Run the app
ButtonEvent().run()
