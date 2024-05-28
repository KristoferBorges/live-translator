from kivymd.uix.screen import MDScreen
from kivy.clock import Clock

class Loading(MDScreen):
    
    def on_enter(self):
        # Schedule a function to be called after a certain delay
        Clock.schedule_once(self.change_to_main_screen, 3.26)  # Change to main screen after 5 seconds

    def change_to_main_screen(self, dt):
        # alterar para a tela principal
        self.manager.current = "tela_principal"
        